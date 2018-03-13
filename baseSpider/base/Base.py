from scrapy import Spider, Request
from baseSpider.items import BasespiderItem
from baseSpider.utils.tools import getUUID
'''
新闻抓取类
---
函数解析
start_requests
直接进入这个函数，
在该函数中直接遍历页面
例如：
http://auto.gasgoo.com/nev/C-501/1
http://auto.gasgoo.com/nev/C-501/2
'''

class Base(Spider):
    name = ''
    allowed_domains = []
    start_urls = []
    # 总页数
    total_num = 1
    # 开始页数
    page_num= 1

    base_url = ''
    # 初始化遍历页面
    # 如果不是相同的url则要重写start_requests

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

    # 遍历页面
    def start_requests(self):
        while self.page_num <= self.total_num:
            url = self.base_url % self.page_num
            yield Request(url=url,callback=self.parse_page_1,dont_filter=True)
            self.page_num +=1

    # 获取每个页面所对应的所有新闻链接
    def parse_page_1(self,response):
        item_list = response.xpath(self.item_list_xpath).extract()
        for item in item_list:
            url = self.item_list_base_url + item
            print(url)
            yield Request(url=url, callback=self.parse_page_2)

    # 获取每个新闻链接的title,content,time
    def parse_page_2(self,response):
        item = BasespiderItem()
        item['id'] = getUUID()
        item['title'] = response.xpath(self.title_xpath).extract_first()
        item['content'] = response.xpath(self.content_xpath).xpath('string(.)').extract_first()
        item['time'] = response.xpath(self.time_xpath).extract_first()
        print(item)
        yield item

