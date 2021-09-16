import re
from datetime import datetime

import requests

from vnexpress.schema import VnexpressCommentSchema

comment_schema = VnexpressCommentSchema()
re_count_comment = re.compile('([0-9]+?)-1\', ([0-9]+)')
re_news_id = re.compile('([0-9]{7}).htm')
re_datetime = re.compile('([0-9]+/[0-9]+/[0-9]{4}, [0-9]{2}:[0-9]{2})')
re_abstract = re.compile('([0-9]+/[0-9]+/[0-9]{4}, [0-9]{2}:[0-9]{2})(.*?\\n){2}(.*\\n)')
re_category = re.compile('Trở lại .*?\\n(.*?\\n)(.*?\\n)?')


def query_count_comment(news_ids):
    result = {}
    url = 'https://usi-saas.vnexpress.net/widget/index/'
    cid = ';'.join([new_id+'-1' for new_id in news_ids])
    params = {'cid': cid}
    response = requests.get(url, params=params)
    data = response.text
    matches = re_count_comment.finditer(data)
    for match in matches:
        result[match[1]] = int(match[2])
    return result


def query_comments(news_id):
    url = 'https://usi-saas.vnexpress.net/index/get'
    params = {'objectid': news_id, 'objecttype': 1, 'siteid': 1000000, 'limit': 1000}
    response = requests.get(url, params=params)
    data = response.json()
    comments = data['data']['items']
    return comment_schema.load(comments, many=True)


def get_news_id(url):
    match = re_news_id.findall(url)
    if match:
        return match[0]


def get_timestamp(content):
    match = re_datetime.findall(content)
    try:
        if match:
            return int(datetime.strptime(match[0], '%d/%m/%Y, %H:%M').timestamp())
    except Exception as e:
        print(e)


def get_title(title):
    return title.split('-')[0].strip()


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
