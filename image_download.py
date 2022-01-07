import requests
from bs4 import BeautifulSoup as bs

url = "https://s.pstatic.net/static/www/img/uit/sp_main_6f9b98.png"
r = requests.get(url)
f = open("naver_main.png", "wb")
f.write(r.content)
f.close
