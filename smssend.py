import requests


class JmunjaPhone:
    def __init__(self, uid, upw):
        self.uid = uid
        self.upw = upw
        self.url = "http://jmunja.com/sms/app/api.php"
        self.subject = ""
        self.content = ""
        self.hpno = ""

    def send(self, subject, content, hpno):
        self.subject = subject
        self.content = content
        self.hpno = hpno

        dict_data = {'mode': 'send', 'id': self.uid, 'pw': self.upw, 'title': self.subject,
                     'message': self.content, 'reqlist': self.hpno}
        response = requests.post(url=self.url, data=dict_data,
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
        gubun = ":header_stop:"
        result = response.text.replace(gubun, "")
        return result


class JmunjaWeb:
    def __init__(self, uid, upw):
        self.uid = uid
        self.upw = upw
        self.url = "http://jmunja.com/sms/web/api.php"
        self.subject = ""
        self.content = ""
        self.hpno = ""
        self.callback = ""

    def send(self, subject, content, hpno, callback):
        self.subject = subject
        self.content = content
        self.hpno = hpno
        self.callback = callback

        dict_data = {'mode': 'send', 'id': self.uid, 'pw': self.upw, 'title': self.subject,
                     'message': self.content, 'reqlist': self.hpno, 'callback': self.callback}
        response = requests.post(url=self.url, data=dict_data,
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
        gubun = ":header_stop:"
        result = response.text.replace(gubun, "")
        return result


