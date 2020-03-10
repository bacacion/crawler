import time

from pyquery import PyQuery as pq
import requests

class TOKEN:
    playROM = 'C7Caokvitm1nSR8ntBSiNwAlM7IOY7Wzb7D0KLNZMZd'
    botTest = 'VOif9PU2Bhp4twTVD8sjA4nBpcRpAe6mpyG56SzLCA8'

def sendLineNotify(token, msg):
    response = requests.post(
        url='https://notify-api.line.me/api/notify',
        headers={
            'Authorization': f'Bearer {token}'
        },
        data={
            'message': msg
        }
    )

def getROMNews():
    response = requests.get('https://rom.gnjoy.com.tw/Notice/GetaNewsList?news_catalog_id=2&Page=1&Search=')
    with open('eventNumRecord.txt', 'r') as f:
        eventNumRecord = f.read()
        eventNumRecord = eventNumRecord.split(",")
    if response.status_code != 200:
        print(f'status is not 200 ({response.status_code})')
        return

    dom = pq(response.text)
    events = list(dom('ul > li.icoEvent').items())
    lastestNews = max(eventNumRecord)
    for event in events:
        evevtNum = event('span.no').text()
        evevtDate = event('span.date').text()
        evevtTitle = event('a').text()
        evevtUrl = 'https://rom.gnjoy.com.tw' + event('a').attr('href')
        print(evevtUrl)
        msg = f'{evevtDate}\n{evevtTitle}\n{evevtUrl}'
        if evevtNum not in eventNumRecord: 
            with open('eventNumRecord.txt', 'a+') as f:
                f.write(evevtNum + ',') 
            print(f'New Event! {evevtNum} {evevtTitle}')
            sendLineNotify(TOKEN.playROM, msg)
            
       



if __name__ == '__main__':
    getROMNews()
