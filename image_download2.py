import requests
from bs4 import BeautifulSoup as bs
import os.path

url = "http://urll.kr"
r = requests.get(url)
html = r.text
soup = bs(html, 'html.parser')

imgs = soup.find_all('img')
for i in imgs:
    # base_url = "http://urll.kr"
    f_path = i.get("src")
    img_url = f_path    
  
    r = requests.get(img_url)
    f_name = os.path.basename(f_path)
    print(f_name)
    try:
        with open("images/"+f_name, "wb") as f:
            f.write(r.content)
    except:
        pass

