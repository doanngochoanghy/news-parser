import requests
from urllib.parse import urljoin


def query_news(url, index, q='*:*', **kwargs):
    url = urljoin(url, index) + '/select'
    kwargs['q.op'] = 'OR'
    kwargs['q'] = q
    response = requests.get(url, params=kwargs, timeout=30)
    return response.json()
