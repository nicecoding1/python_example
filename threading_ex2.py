import threading, requests, time

class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    
    def run(self):
        resp = requests.get(self.url)
        time.sleep(3)
        print("Sub Thread", self.url, len(resp.text), 'chars')

t = HtmlGetter('https://www.naver.com')
t.start()

print("Main Thread")