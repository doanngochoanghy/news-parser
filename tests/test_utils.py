from utils import query_news


url = 'http://localhost:8983/solr/'


def test_query_news():
    index = 'dantri'
    result = query_news(url, index, q='url:dantri AND url:htm', rows=10)
    print(result)
    assert result
