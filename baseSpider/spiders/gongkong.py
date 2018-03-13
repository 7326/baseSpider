
from baseSpider.base.Base import Base

class gongkong(Base):
    name = 'gongkong'
    total_num = 10
    page_num = 1
    base_url = 'http://www.gongkong.com/news/list/0_%d.html'
    ## 配置其中的标签
    item_list_base_url = 'http://www.gongkong.com'
    item_list_xpath = '/html/body/div/div[4]/table/tbody/tr/td[1]/a/@href'
    ## title
    title_xpath = '//*[@id="Rtitle_D"]/text()'
    ## content
    content_xpath = '//*[@id="article"]'
    ## time
    time_xpath = '//*[@id="grey6"]/span[3]/text()'
