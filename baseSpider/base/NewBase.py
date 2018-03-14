from scrapy import Spider, Request
from baseSpider.items import BasespiderItem
from baseSpider.utils.tools import getUUID
'''
新闻抓取类
---
直接荣start_urls开始遍历
在该函数中直接遍历页面
例如：

'''

class Base(Spider):
    name = ''
    allowed_domains = []
    start_urls = []

    ## 配置其中的标签
    # 获取的每个url中如果不含域名，则在次添加上
    item_list_base_url = ''
    # 获取每个新闻的url的xpath
    item_list_xpath = ''
    ## title 对应的xpath
    title_xpath = ''
    ## content对应的xpath ,写出content所在的div即可，可以获取到下面的所有text
    content_xpath = ''
    ## time对应的xpath
    time_xpath = ''


    # 获取每个页面所对应的所有新闻链接
    def parse(self, response):
        item_list = response.xpath(self.item_list_xpath).extract()
        for item in item_list:
            url = self.item_list_base_url + item
            print(url)
            yield Request(url=url, callback=self.parse_page_1)

    # 获取每个新闻链接的title,content,time
    def parse_page_1(self,response):
        item = BasespiderItem()
        item['id'] = getUUID()
        item['title'] = response.xpath(self.title_xpath).extract_first()
        item['content'] = response.xpath(self.content_xpath).xpath('string(.)').extract_first()
        item['time'] = response.xpath(self.time_xpath).extract_first()
        print(item)
        yield item

