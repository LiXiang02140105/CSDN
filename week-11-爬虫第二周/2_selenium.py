from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests,os,urllib

def scrayHTML():
    driver = webdriver.Chrome()

    driver.get("https://image.baidu.com")
    searchInput = driver.find_element_by_id("kw")
    searchInput.clear()
    searchInput.send_keys("街拍")
    searchInput.send_keys(Keys.RETURN) # keys 对象
    return driver

def parseHTML(driver):
    img_urls = []
    for index in range(0,1200,200):
        # temp_url: 暂时的存储当前队列中的图片
        # postion() : 跳过已经爬取过的图片
        print(index)
        temp_urls = []
        soup = BeautifulSoup(driver.page_source,"lxml") # 解析网页
        imgpage = soup.find_all(name="div", attrs={"class":"imgpage"})
        
        imgpage = imgpage[0]
        li_list = imgpage.select("ul li")
        for li in li_list:
            img_attrs = li.find(name="img").attrs
            if "data-imgurl" in img_attrs.keys():
                url = img_attrs["data-imgurl"]
            else:
                url = img_attrs["src"]
            #if index > 0:
                #print("url",url)
            if url not in img_urls:
                temp_urls.append(url)
                print("temp_urls",temp_urls)
        
        #img_urls.extend(temp_urls)
        img_urls += temp_urls
        print("img_urls",len(img_urls))
        driver.execute_script("window.scrollTo(0,%d)"%index)
        time.sleep(1)
    return img_urls

def saveImg(img_urls):
    for img in img_urls:
        urllib.request.urlretrieve(img,os.path.join('image',str(int(time.time()))+".jpg"))

if __name__ == "__main__":
    img_urls = []
    driver = scrayHTML() # 获取网页
    img_urls = parseHTML(driver) # 获取urls
    saveImg(img_urls)
    #driver.quit()

