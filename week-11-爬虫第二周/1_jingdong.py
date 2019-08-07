# 爬取京东的图片信息案例
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
url = "https://list.jd.com/list.html?cat=9987,653,655"

# 爬取数据
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

imlist = soup.find_all(name="img", attrs={"width":"220","height":"220"})
m = 1
for im in imlist:
    if "src" in im.attrs : 
        imurl = "https:" + im.attrs["src"]
    else:
        imurl = "https:" + im.attrs["data-lazy-img"]

    # 存储图片 - stram
    with requests.get(imurl, stream=True) as imgstream:
        with open("./mypics/stream/stram_%d.jpg" % m, "wb") as fp:
            for chunk in imgstream:
                fp.write(chunk)
    print("stram_%d.jpg" % m)
    

    # 存储图片 - urlretrieve
    urlretrieve(imurl,"./mypics/urlretrieve/urlretrieve_%d.jpg" % m)
    m += 1