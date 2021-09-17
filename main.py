from utils import query_news
from dantri import utils as dantri_utils
from vnexpress import utils as vnexpress_utils
from vietnamnet import utils as vietnamnet_utils
import sys
import json
from multiprocessing import Pool


solr_url = 'http://localhost:8983/solr/'


def parse_news(index, extension, start, end):
    rows = 100
    data = []
    q = 'url:{0} AND url:{1}'.format(index, extension)
    print('start crawl from %s to %s' % (start, end))
    while True:
        result = query_news(solr_url, index, q, rows=rows, start=start, sort='_version_ asc')
        response = result['response']
        numFound = response['numFound']
        print('crawl from %s to %s of %s' % (start, start + rows, numFound))
        docs = response['docs']
        news_ids = []
        for doc in docs:
            url = doc['url']
            news_id = utils.get_news_id(url)
            doc['news_id'] = news_id
            if news_id:
                news_ids.append(news_id)
        count_comments = utils.query_count_comment(news_ids)
        for doc in docs:
            if 'news_id' not in doc:
                continue
            if count_comments.get(doc['news_id'], 0):
                news = utils.get_all_info(**doc)
                news['count_comments'] = count_comments[doc['news_id']]
                data.append(news)
        start += rows
        if start >= end:
            break
    with open('./data/%s/news-%s.json' % (index, end), 'w') as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False))
        print("Save file %s-%s", end)


if __name__ == "__main__":
    index = sys.argv[1]
    extension = sys.argv[2]
    start = int(sys.argv[3])
    args = sys.argv[1:]
    q = 'url:{0} AND url:{1}'.format(*args)
    rows = 1000
    if index == 'dantri':
        utils = dantri_utils
    elif index == 'vnexpress':
        utils = vnexpress_utils
    # elif index == 'vietnamnet':
    #     utils = vietnamnet_utils
    else:
        raise Exception('Index not valid')
    data = []
    args = []
    result = query_news(solr_url, index, q, sort='_version_ asc')
    response = result['response']
    numFound = response['numFound']
    while True:
        args.append((index, extension, start, start + rows))
        start += rows
        if start >= numFound:
            break
    print(args)
    with Pool(processes=20) as pool:
        result = pool.starmap_async(parse_news, args)
        result.get()
    # if data:
    #     with open('./data/%s/news-%s.json' % (index, start), 'w') as f:
    #         f.write(json.dumps(data, indent=2, ensure_ascii=False))
    #         print("Save file %s" % start)
