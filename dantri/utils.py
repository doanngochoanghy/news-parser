import requests
import re
from datetime import datetime
from dantri.schema import DantriCommentSchema
re_news_id = re.compile('([0-9]{17}).htm')
re_datetime = re.compile('([0-9]{2}/[0-9]{2}/[0-9]{4} - [0-9]{2}:[0-9]{2})')
re_abstract = re.compile('([0-9]{2}/[0-9]{2}/[0-9]{4} - [0-9]{2}:[0-9]{2})\\n([^\\.]*?\\n)(.*\\.\\n)')
re_category = re.compile('\nDân Trí\\n(.*?\\n)([^0-9]*?\\n)?')
comment_schema = DantriCommentSchema()


def query_count_comment(news_ids):
    url = 'https://apicomment.dantri.com.vn/Api/Comment/aj-GetTotalCommentByNewsId'
    arrnewsid = ','.join(news_ids)
    params = {'arrnewsid': arrnewsid}
    response = requests.get(url, params=params)
    result = {}
    data = response.json()
    for news in data:
        result[news['ObjectId']] = news['CommentCount']
    return result


def query_comments(news_id):
    url = 'https://apicomment.dantri.com.vn/api/comment/list/1-%s-0-0-1000.htm' % news_id
    response = requests.get(url)
    comments = response.json()
    for comment in comments:
        if comment.get('Replies'):
            comments.extend(comment['Replies'])
    return comment_schema.load(comments, many=True)


def get_news_id(url):
    match = re_news_id.findall(url)
    if match:
        return match[0]


def get_timestamp(content):
    match = re_datetime.findall(content)
    try:
        if match:
            return int(datetime.strptime(match[0], '%d/%m/%Y - %H:%M').timestamp())
    except Exception as e:
        print(e)


def get_title(title):
    return title.split('|')[0].strip()


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
