import time
import re

from pyquery import PyQuery as pq
import requests

def getImage(url, imgName):
    print(f'get Img: {imgName}')
    response = requests.get(
        url=url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
    )
    if response.status_code != 200:
        print(f'status is not 200 ({response.status_code})')
        return
    with open(f'tryHome/images/{imgName}.jpg', 'wb') as f:
        f.write(response.content)

def getGoogleImg(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'status is not 200 ({response.status_code})')
        return
    with open('tryHome/googleImg.html', 'w') as f:
        f.write(response.text)
    dom = pq(response.text)
    imgset = dom('td img')
    i=0
    # print(response.text)
    for img in imgset.items():
        getImage(img.attr('src'), i)
        i += 1
        time.sleep(1)
    print('Download Done!')
    

if __name__ == '__main__':
    getGoogleImg('https://www.google.com/search?q=%E8%98%8B%E6%9E%9C&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjz6rTP7qznAhXyxosBHcxiBA4Q_AUoAXoECAgQAw&biw=1920&bih=937')