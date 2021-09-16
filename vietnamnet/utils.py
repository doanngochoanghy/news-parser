import requests
import json


def query_count_comment(news_ids):
    result = {}
    url = "https://i.vietnamnet.vn/jsx/interaction/getListTotalComments/data.jsx"
    objkeys = ';'.join(news_ids)
    response = requests.get(url, params={'objkeys': objkeys})
    data = json.loads(response.text[7:])
    for news in data.get('data'):
        result[news['objkey']] = news['count']
    return result


def query_comments(news_id):
    url = "https://i.vietnamnet.vn/jsx/interaction/getInteraction/data.jsx"
    params = {'objkey': news_id}
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
