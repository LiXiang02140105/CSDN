import requests
from pyquery import PyQuery as pq
'''
访问京东商城网址，选择多个商品放入购物车后查看自己的购物车。
请使用Python爬取京东商城网址购物车中的所有商品信息（输出即可） 
'''
def scrayHTML():
    headers = {
        "cookie": "shshshfpa=89692c45-6734-fab9-918d-a548eeb08ed0-1544429463; 3AB9D23F7A4B3C9B=O4X6HUPDD2MSBHAZ2N2NDZUQWSDI24CVBZB73ZH4BHGU53W2K65N6RNN6Q6AU3XDWIBBENXABONG4OVVEFCRVLBKTU; shshshfpb=vvyE5WT6denZqpjahuBtiyw%3D%3D; pinId=Mt2hzirCD2iNyozD0hKWCbV9-x-f3wj7; __jdu=1755552269; __jdv=122270672|www.google.com|-|referral|-|1564734448798; areaId=1; ipLoc-djd=1-2800-0-0; user-key=0f3626bc-db65-4158-9bfd-630128c8dd86; cd=0; cn=0; shshshfp=0f6ded2b7d5f3c7edd8d8ea011c036b1; shshshsID=96ccccbf397e9306df0e6ac03328ba71_1_1564968668148; __jda=122270672.1755552269.1544077463.1564734449.1564968668.7; __jdc=122270672; __jdb=122270672.3.1755552269|7.1564968668; wlfstk_smdl=ismsxke88irz8yf12fe0n5ljspgwh85z; TrackID=1Ph_hRKwYRI0B-q5arWb9Gpan7a0bEzeMa3HeHQhVoDUnqm51ZGzeymh--it8mbARLwjG1eYEPvEMiD1-oEoeT8GsWTxwwVmYpVEZQLVe7DM; thor=564987CCEECA7FCE7736D63B0C8D0B8409986268C8F1CA202C76FD18AAAEF3F2605DD918F10FC25705047C688DFA59D5D6CCFDD90489CE199BC9F02C8522447C7E39E33D1FE06E404F678C93456F995F3134A955E08C5473C2E6817026A89C1D9FEC1BC5763433DC393D508FB0D8BFF547A22102C911070E2C2D9E56AADE6237D590A3DB6FACFC196332EDD84B154E11D575E67CE7E9798F116D140D5DECC768; pin=jd_5fb01bac01b4e; unick=jd_5fb01bac01b4e; ceshi3.com=000; _tp=0nGRZpn7q18bge4SExodEUXKqF0JvrzvXhIJGh2aChw%3D; logining=1; _pst=jd_5fb01bac01b4e",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    }
    url = "https://cart.jd.com/cart.action"
    res = requests.get(url,headers=headers)
    return res

def parseHTML(res):
    doc = pq(res.text)
    goods = doc("div.item-form")
    for good in goods.items():
        yield {
            "title" : good.find("div.p-name a").text(),
            "image" : "https:" + good.find("div.p-img a img").attr("src"),
            "price" : good.find("p.plus-switch strong").text(),
            "number" : good.find("div.quantity-form input").attr("value"),
        }
if __name__ == "__main__":
    res = scrayHTML()
    items = parseHTML(res)
    for item in items:
        print(item)