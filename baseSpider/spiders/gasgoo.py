

from baseSpider.base.Base import Base


class gasgoo(Base):
    name = 'gasgoo'
    total_num = 10
    page_num = 1
    base_url = 'http://auto.gasgoo.com/nev/C-501/%d'
    ## 配置其中的标签
    item_list_base_url = 'http://auto.gasgoo.com'
    item_list_xpath = '/html/body/div[4]/div/div[1]/div/h2/a/@href'
    ## title
    title_xpath = '/html/body/div[5]/div[1]/div[3]/h1/text()'
    ## content
    content_xpath = '//*[@id="ArticleContent"]'
    ## time
    time_xpath = '/html/body/div[5]/div[1]/div[3]/div[1]/span[1]/text()'
