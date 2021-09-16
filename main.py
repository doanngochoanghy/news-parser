from utils import query_news
from dantri import utils as dantri_utils
from vnexpress import utils as vnexpress_utils
import sys
import json


if __name__ == "__main__":
    solr_url = 'http://localhost:8983/solr/'
    index = sys.argv[1]
    args = sys.argv[1:]
    q = 'url:{0} AND url:{1}'.format(*args)
    start = 0
    rows = 100
    data = []
    if index == 'dantri':
        utils = dantri_utils
    elif index == 'vnexpress':
        utils = vnexpress_utils
    else:
        raise Exception('Index not valid')
    while True:
        news_ids = []
        print('crawl from %s to %s' % (start, start+rows))
        result = query_news(solr_url, index, q, rows=rows, start=start, sort='_version_ desc')
        response = result['response']
        numFound = response['numFound']
        docs = response['docs']
        for doc in docs:
            url = doc['url']
            if len(url) < 60:
                print(url)
                continue
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
        if start >= 300:
            break
    with open('./data/'+index+'/news.json', 'w') as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False))
