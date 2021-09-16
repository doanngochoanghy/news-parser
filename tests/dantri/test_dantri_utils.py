from dantri import utils


def test_count_comment():
    news_ids = ['20210912080014281', '20210912080014282', '20210912080014284', '20210912080014283', '20210912193043318']
    result = utils.query_count_comment(news_ids)
    assert result['20210912193043318'] > 0


def test_get_comments():
    news_id = '20210912193043318'
    comments = utils.query_comments(news_id)
    assert comments


def test_get_news_id():
    url = 'https://tuoitre.vn/yeu-roi-lay-xe-be-gai-o-long-an-va-tp-hcm-tach-hay-gop-vu-an-20210223223157153.htm"'
    news_id = utils.get_news_id(url)
    assert news_id == '20210223223157153'
    url = 'https://amp.dantri.com.vn/su-kien.htm'
    news_id = utils.get_news_id(url)
    assert news_id is None
    url = 'https://tuoitre.vn/yeu-roi-lay-xe-be-gai-o-long-an-va-tp-hcm-tach-hay-gop-vu-an-123.htm"'
    news_id = utils.get_news_id(url)
    assert news_id is None


def test_get_timestamp():
    content = "Thứ năm, 02/07/2020 - 14:13\nVì sao Chủ tịch tỉnh Lâm Đồng"
    datetime = utils.get_timestamp(content)
    assert datetime


def test_get_title():
    title = "Điều gì khiến thực khách “ngây ngất” trước kiệt tác ẩm thực Kaiseki Nhật Bản tại Yen Sushi Premium |"
    title = utils.get_title(title)
    assert title


def test_get_abstract():
    content = "Vì sao Chủ tịch tỉnh Lâm Đồng bị yêu cầu kiểm điểm trách nhiệm? | Báo Dân trí\nVideo\nSự kiện\nXã hội\nChính trị\nMôi trường\nGiao thông\nNóng trên mạng\nChuyện ngày mới\nThế giới\nQuân sự\nHồ sơ - Phân tích\nThế giới đó đây\nKiều bào\nKinh doanh\nTài chính\nChứng khoán\nDoanh nghiệp\nKhởi nghiệp\nTiêu dùng\nBất động sản\nDự án\nThị trường\nNhịp sống đô thị\nSống xanh\nNội thất\nThể thao\nBóng đá trong nước\nBóng đá Châu Âu\nTennis\nGolf\nVõ thuật\nCác môn Thể thao khác\nHậu trường\nViệc làm\nChính sách\nViệc làm\nĐưa nghị quyết 68 vào cuộc sống\nXuất khẩu lao động\nChúng tôi nói\nNhân ái\nDanh sách ủng hộ\nDanh sách kết chuyển\nHoàn cảnh\nSức khỏe\nUng thư\nVắc xin Covid-19\nKiến thức giới tính\nTư vấn\nKhỏe đẹp\nĐại dịch Covid-19\nVăn hóa\nĐời sống văn hóa\nĐiện ảnh\nÂm nhạc\nVăn học\nHạt giống tâm hồn\nHương vị Việt\nGiải trí\nHậu trường\nThời trang\nTVshow\nXe ++\nThị trường xe\nĐánh giá\nCộng đồng xe\nKinh nghiệm - Tư vấn\nĐua xe\nBảng giá ô tô\nSức mạnh số\nSản phẩm\nDi động - Viễn thông\nPhần mềm - Bảo mật\nCộng đồng mạng\nGiáo dục\nGóc phụ huynh\nKhuyến học\nGương sáng\nGiáo dục - Nghề nghiệp\nDu học\nTuyển sinh\nAn sinh\nPháp luật\nHồ sơ vụ án\nPháp đình\nDu Lịch\nĐời sống\nTình yêu\nNhịp sống trẻ\nKhoa học\nBlog\nBạn đọc\nEmagazine\nPhoto Story\nInfographic\nDân Trí\nXã hội\nChính trị\nThứ năm, 02/07/2020 - 14:13\nVì sao Chủ tịch tỉnh Lâm Đồng bị yêu cầu kiểm điểm trách nhiệm?\nDân trí\nChủ tịch tỉnh Lâm Đồng nghiêm túc kiểm điểm trách nhiệm của UBND tỉnh và cá nhân Chủ tịch UBND tỉnh, các Phó Chủ tịch UBND tỉnh về những thiếu sót, vi phạm trong quản lý, điều hành.\nSau khi chỉ ra hàng loạt vi phạm trong việc quản lý, sử dụng đất đai và đầu tư xây dựng trên địa bàn tỉnh Lâm Đồng, Tổng Thanh tra Chính phủ đã kiến nghị Thủ tướng Chính phủ yêu cầu Chủ tịch UBND tỉnh Lâm Đồng nghiêm túc kiểm điểm trách nhiệm của UBND tỉnh và cá nhân Chủ tịch UBND tỉnh, các Phó Chủ tịch UBND tỉnh về những thiếu sót, tồn tại, vi phạm liên quan đến trách nhiệm quản lý, điều hành.\nĐồng thời chỉ đạo cơ quan chức năng xử lý số tiền phát hiện qua thanh tra trên 386 tỷ đồng. Chấm dứt hoạt động, thu hồi đất của 3 dự án d"
    abstract = utils.get_abstract(content)
    assert abstract


def test_get_category_subcategory():
    content = "Vì sao Chủ tịch tỉnh Lâm Đồng bị yêu cầu kiểm điểm trách nhiệm? | Báo Dân trí\nVideo\nSự kiện\nXã hội\nChính trị\nMôi trường\nGiao thông\nNóng trên mạng\nChuyện ngày mới\nThế giới\nQuân sự\nHồ sơ - Phân tích\nThế giới đó đây\nKiều bào\nKinh doanh\nTài chính\nChứng khoán\nDoanh nghiệp\nKhởi nghiệp\nTiêu dùng\nBất động sản\nDự án\nThị trường\nNhịp sống đô thị\nSống xanh\nNội thất\nThể thao\nBóng đá trong nước\nBóng đá Châu Âu\nTennis\nGolf\nVõ thuật\nCác môn Thể thao khác\nHậu trường\nViệc làm\nChính sách\nViệc làm\nĐưa nghị quyết 68 vào cuộc sống\nXuất khẩu lao động\nChúng tôi nói\nNhân ái\nDanh sách ủng hộ\nDanh sách kết chuyển\nHoàn cảnh\nSức khỏe\nUng thư\nVắc xin Covid-19\nKiến thức giới tính\nTư vấn\nKhỏe đẹp\nĐại dịch Covid-19\nVăn hóa\nĐời sống văn hóa\nĐiện ảnh\nÂm nhạc\nVăn học\nHạt giống tâm hồn\nHương vị Việt\nGiải trí\nHậu trường\nThời trang\nTVshow\nXe ++\nThị trường xe\nĐánh giá\nCộng đồng xe\nKinh nghiệm - Tư vấn\nĐua xe\nBảng giá ô tô\nSức mạnh số\nSản phẩm\nDi động - Viễn thông\nPhần mềm - Bảo mật\nCộng đồng mạng\nGiáo dục\nGóc phụ huynh\nKhuyến học\nGương sáng\nGiáo dục - Nghề nghiệp\nDu học\nTuyển sinh\nAn sinh\nPháp luật\nHồ sơ vụ án\nPháp đình\nDu Lịch\nĐời sống\nTình yêu\nNhịp sống trẻ\nKhoa học\nBlog\nBạn đọc\nEmagazine\nPhoto Story\nInfographic\nDân Trí\nXã hội\nChính trị\nThứ năm, 02/07/2020 - 14:13\nVì sao Chủ tịch tỉnh Lâm Đồng bị yêu cầu kiểm điểm trách nhiệm?\nDân trí\nChủ tịch tỉnh Lâm Đồng nghiêm túc kiểm điểm trách nhiệm của UBND tỉnh và cá nhân Chủ tịch UBND tỉnh, các Phó Chủ tịch UBND tỉnh về những thiếu sót, vi phạm trong quản lý, điều hành.\nSau khi chỉ ra hàng loạt vi phạm trong việc quản lý, sử dụng đất đai và đầu tư xây dựng trên địa bàn tỉnh Lâm Đồng, Tổng Thanh tra Chính phủ đã kiến nghị Thủ tướng Chính phủ yêu cầu Chủ tịch UBND tỉnh Lâm Đồng nghiêm túc kiểm điểm trách nhiệm của UBND tỉnh và cá nhân Chủ tịch UBND tỉnh, các Phó Chủ tịch UBND tỉnh về những thiếu sót, tồn tại, vi phạm liên quan đến trách nhiệm quản lý, điều hành.\nĐồng thời chỉ đạo cơ quan chức năng xử lý số tiền phát hiện qua thanh tra trên 386 tỷ đồng. Chấm dứt hoạt động, thu hồi đất của 3 dự án d"
    category, sub_category = utils.get_category_subcategory(content)
    assert category.strip() == 'Xã hội'
    assert sub_category.strip() == 'Chính trị'
