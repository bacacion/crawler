import time
import re

import pyquery
import requests
def getContent(url,title):
    print('Downloading: '+title)
    response = requests.get(url)
    response.encoding = 'big5'
    if response.status_code != 200:
        print(f'status is not 200 ({response.status_code})')
        return
    dom = pyquery.PyQuery(response.text)
    content1 = str(dom('div.content_ad~br')).replace('<br />', '').encode()

    with open(f'tryHome/222/{title}.txt', 'wb') as f:
        f.write(content1) 


def getNovel(storyNum):
    response = requests.get(f'https://www.wfxs.org/html/{storyNum}/')
    response.encoding = 'big5'
    if response.status_code != 200:
        print(f'status is not 200 ({response.status_code})')
        return
    dom = pyquery.PyQuery(response.text)
    storyTitle = dom('h1').text()
    chs = dom('dd>a')
    urlMatch = re.findall(r'\/html\/\d*\/\d*\.html', str(chs))
    print(urlMatch)
    chTitle = chs.text()
    titleMatch = re.findall(r'第.{1,3}章', chTitle)
    i = 0
    for ch in chs:
        url1 = 'https://www.wfxs.org' + urlMatch[i]
        getContent(url1,titleMatch[i])
        i += 1
        time.sleep(1)

if __name__ == '__main__':
    getNovel(417584)
    # getContent('https://www.wfxs.org/html/417584/93141248.html','111')