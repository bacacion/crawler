import pyquery
import requests

def getContent(url):
    print(url)
    response = requests.get(url)
    dom = pyquery.PyQuery(response.text)
    aaaa = dom('a')
    print(aaaa)





if __name__ == '__main__':
    # getNovel(417584)
    getContent('https://rom.gnjoy.com.tw/Notice/GetaNewsList?news_catalog_id=2&Page=1&Search=')