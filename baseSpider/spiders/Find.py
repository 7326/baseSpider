
from ..base.NewBase import Base



class Find(Base):
    name = 'find'
    start_urls = ['http://www.find800.cn/']

    ## 配置其中的标签
    # 获取的每个url中如果不含域名，则在次添加上
    item_list_base_url = ''
    # 获取每个新闻的url的xpath,这里直接获取到url
    item_list_xpath = '/html/body/div[7]/div[7]/div[3]/ol/li/a/@href'
    ## title 对应的xpath,这里也直接获取到text
    title_xpath = '/html/body/div[7]/div[4]/div[1]/h1/text()'
    ## content对应的xpath ,写出content所在的div即可，可以获取到下面的所有text
    content_xpath = '//*[@id="dddss"]'
    ## time对应的xpath
    time_xpath = '/html/body/div[7]/div[4]/div[2]/text()[2]'
