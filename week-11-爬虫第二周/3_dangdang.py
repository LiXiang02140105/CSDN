'''
爬取当当图书网站中所有关于python关键字的图片信息。 
参考URL：http://search.dangdang.com/?key=python&act=input 
要求：将图书图片下载存储指定目录中，而图书信息写入到MongoDB数据库中。 
'''

import requests,re,time,os
from lxml import etree
from requests.exceptions import RequestException
from pyquery import PyQuery as pq
from urllib import request
import pymongo

def scrapyHTML(url):
    '''爬取器'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def parseHTML(content,index):
    '''解析器'''
    #parser = etree.HTML(content)
    #li_list = parser.xpath("//ul[@class='bigimg']/li")
    doc = pq(content)
    li_list = doc("ul.bigimg li")
    for li in li_list.items():

        img = li.find("a.pic img")
        if "data-original" in str(img):
            img_url = img.attr("data-original")
        else:
            img_url = img.attr("src")
        filename = str(index) + "_" + str(time.time()).replace('.','_')
        request.urlretrieve(img_url,os.path.join('image/dangdang',filename + '.jpg'))
        yield {
            "_id" : filename,
            "title" : li.find("a.pic").attr('title'),
            "price" : li.find("p.price span.search_now_price").text(),
            "introduct" : li.find("p.name a").attr('title') ,
            "recommend" : li.find("p.detail").text() ,
            "img_name" : filename + '.jpg',
        }

def saveHTML(book):
    '''存储器'''
    client = pymongo.MongoClient("localhost", 27017)
    db = client.demo
    cursor = db.dangdang # 文档叫当当, 是demo集合下的一个文档
    cursor.insert_one(book)

def main():
    '''主调度器 & url管理器'''
    #for index in range(1,11):
    index = 1
    url = "http://search.dangdang.com/?key=python&act=input&page_index=%d" % index
    content = scrapyHTML(url)
    books = parseHTML(content,index)
    for book in books:
        saveHTML(book)
    #break

if __name__ == "__main__":
    main()
