from vnexpress import utils


def test_get_comments():
    news_id = '4355380'
    comments = utils.get_comments(news_id)
    assert comments


def test_count_comment():
    news_ids = ['4355380', '4357582', '4355549']
    result = utils.query_count_comment(news_ids)
    assert result


def test_get_news_id():
    url = 'https://vnexpress.net/tuoi-34-song-u-ly-vi-duoc-thua-ke-hai-day-phong-tro-4355396.html'
    news_id = utils.get_news_id(url)
    assert news_id == '4355396'
    url = 'https://vnexpress.net/annihilation-phim-vien-tuong-dep-dang-so-cua-natalie-portman-3725959.html'
    news_id = utils.get_news_id(url)
    assert news_id == '3725959'


def test_get_datetime():
    content = 'inh doanh\nKinh doanh\nDoanh nghiệp\nThứ hai, 10/5/2021, 14:30 (GMT+7)\n3 yếu tố tạo môi trường làm việc cân bằng tại Tiki'
    result = utils.get_timestamp(content)
    print(result)
    assert result


def test_get_title():
    title = "Bất động sản trong vòng xoáy bất định - VnExpress Kinh doanh"
    assert utils.get_title(title) == "Bất động sản trong vòng xoáy bất định"


def test_get_abstract():
    content = "Bất động sản trong vòng xoáy bất định - VnExpress Kinh doanh\nThứ ba, 14/9/2021\nMới nhất\nInternational\nMới nhất\nThời sự\nGóc nhìn\nThế giới\nVideo\nKinh doanh\nKhoa học\nGiải trí\nThể thao\nPháp luật\nGiáo dục\nSức khỏe\nĐời sống\nDu lịch\nSố hóa\nXe\nÝ kiến\nTâm sự\nHài\nTất cả\nTrở lại Kinh doanh\nKinh doanh\nBất động sản\nChủ nhật, 2/8/2020, 14:00 (GMT+7)\nBất động sản trong vòng xoáy bất định\nCovid-19 quay lại, các kênh tài chính khác biến động mạnh đang tạo ra nhiều thách thức, khó khăn cho thị trường địa ốc.\nSau nhiều tháng đầu năm thấm đòn đại dịch, tháng 5 và 6 được xem là cột mốc tái khởi động của ngành địa ốc khi cả nước kiểm soát tốt dịch bệnh và các hoạt động mua bán hồi phục tích cực. Thế nhưng, làn sóng Covid-19 thứ hai ập đến vào tháng 7 khiến thị trường bất động sản một lần nữa rơi vào vòng xoáy bất định.\nĐiều khiến các chuyên gia quan n"
    abstract = utils.get_abstract(content)
    print(abstract)
    assert abstract


def test_get_category_subcategory():
    content = '12 năm ở nhà thuê vì không muốn sống cảnh nợ nần\nThứ ba, 14/9/2021\nMới nhất\nInternational\nMới nhất\nThời sự\nGóc nhìn\nThế giới\nVideo\nKinh doanh\nKhoa học\nGiải trí\nThể thao\nPháp luật\nGiáo dục\nSức khỏe\nĐời sống\nDu lịch\nSố hóa\nXe\nÝ kiến\nTâm sự\nHài\nTất cả\nTrở lại Ý kiến\nÝ kiến\nĐời sống\n'
    category, sub_category = utils.get_category_subcategory(content)
    assert category.strip() == "Ý kiến"
    assert sub_category.strip() == "Đời sống"
