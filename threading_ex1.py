import threading
import requests
import time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(3)
    print("Sub Thread", url, len(resp.text), 'chars')

t = threading.Thread(target=getHtml, args=('https://www.naver.com',))
t.daemon = False
t.start()

print("Main Thread")