import requests
import chardet

def getGammerPage(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f'status is not 200 ({response.status_code})')
        return
    # print(response.content)

    det = chardet.detect(response.content)
    print(response.content.decode(det['encoding']))
    with open('gamer.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    getGammerPage('https://gnn.gamer.com.tw/detail.php?sn=189814')