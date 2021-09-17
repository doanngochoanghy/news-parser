import requests
import json
import re
from datetime import datetime
re_news_id = re.compile('-([0-9]{6}).htm')
re_datetime = re.compile('([0-9]{2}/[0-9]{2}/[0-9]{4}) .* ([0-9]{2}:[0-9]{2}) ')
re_abstract = re.compile('([0-9]{2}/[0-9]{2}/[0-9]{4}).*([0-9]{2}:[0-9]{2}).*?\\n(.*\\.\\n)')

re_category = re.compile('\\n(.*?\\n)❯ (.*?\\n)')


def query_count_comment(news_ids):
    result = {}
    url = "https://i.vietnamnet.vn/jsx/interaction/getListTotalComments/data.jsx"
    objkeys = ';'.join(['vietnamnet.vn__' + news_id for news_id in news_ids])
    response = requests.get(url, params={'objkeys': objkeys})
    data = json.loads(response.text[7:])
    for news in data.get('data'):
        result[news['objkey'][-6:]] = news['count']
    return result


def query_comments(news_id):
    url = "https://i.vietnamnet.vn/jsx/interaction/getInteraction/data.jsx"
    params = {'objkey': 'vietnamnet.vn__'+news_id}
    comments = []
    response = requests.get(url, params=params)
    data = json.loads(response.text[7:])
    comments.extend(data['comments'])
    while data['currentpage'] < data['totalpage']:
        params['page'] = data['currentpage'] + 1
        response = requests.get(url, params=params)
        data = json.loads(response.text[7:])
        comments.extend(data['comments'])
    return comments


def get_news_id(url):
    match = re_news_id.findall(url)
    if match:
        return match[0]


def get_timestamp(content):
    match = re_datetime.findall(content)
    try:
        if match:
            return int(datetime.strptime(match[0][0]+match[0][1], '%d/%m/%Y%H:%M').timestamp())
    except Exception as e:
        print(e)


def get_title(title):
    return title.rsplit('-')[0].strip()


def get_abstract(content):
    match = re_abstract.findall(content)
    if match:
        return match[0][2]


def get_category_subcategory(content):
    match = re_category.finditer(content)
    if match:
        try:
            return next(match).groups()
        except Exception:
            pass
    return None, None


def get_all_info(**news):
    category, sub_category = get_category_subcategory(news['content'])
    if sub_category:
        sub_category = sub_category.strip()
    else:
        sub_category = 'unknown'
    if category:
        category = category.strip()
    else:
        category = 'unknown'
    news_id = get_news_id(news['url'])
    if news_id:
        return {
            'news_id': news_id,
            'url': news['url'],
            'timestamp': get_timestamp(news['content']),
            'title': get_title(news['title']),
            'abstract': get_abstract(news['content']),
            'category': category,
            'sub_category': sub_category,
            'comments': query_comments(news_id)
        }
