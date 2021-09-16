from vietnamnet import utils


def test_query_count_comment():
    news_ids = ['vietnamnet.vn_3_774279',
                'vietnamnet.vn_3_774273',
                'vietnamnet.vn_3_774221',
                'vietnamnet.vn_141_773928',
                'vietnamnet.vn_143_774244',
                'vietnamnet.vn_143_773773',
                'vietnamnet.vn_141_774175',
                'vietnamnet.vn_143_773729',
                'vietnamnet.vn_141_774286',
                'vietnamnet.vn_141_774015', ]
    result = utils.query_count_comment(news_ids)
    assert result


def test_get_comments():
    news_id = 'vietnamnet.vn_tuanvietnam_774076'
    comments = utils.query_comments(news_id)
    assert comments
