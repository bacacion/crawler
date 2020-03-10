import urllib.parse as UP

url = 'https://gnn.gamer.com.tw/detail.php?sn=189814'

res = UP.urlparse(url)

print(res)