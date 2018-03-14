# 本包介绍
本包中主要编写的是没一特定网站的抓取基础类
相同的网站的抓取可以直接继承本类进行编码

# 文件说明
 - Base.py
新闻抓取类
---
函数解析
start_requests
直接进入这个函数，
在该函数中直接遍历页面
例如网站：
http://auto.gasgoo.com/nev/C-501/1
http://auto.gasgoo.com/nev/C-501/2

 - NewBase.py
这一个和上一个其实差别不大
从一个住url开始爬取
地址书写而在 start_urls 中
例如网站：
http://www.find800.cn/ ,获取该网站下面的焦点新闻

