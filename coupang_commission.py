import hmac
import hashlib
import requests
import json
from time import gmtime, strftime
import smssend

TODAY = strftime('%Y%m%d')
REQUEST_METHOD = "GET"
DOMAIN = "https://api-gateway.coupang.com"
URL = "/v2/providers/affiliate_open_api/apis/openapi/v1/reports/commission?startDate="+TODAY+"&endDate="+TODAY+"&page=0"

# Replace with your own ACCESS_KEY and SECRET_KEY
ACCESS_KEY = ""
SECRET_KEY = ""

def generateHmac(method, url, secretKey, accessKey):
    path, *query = url.split("?")
    datetimeGMT = strftime('%y%m%d', gmtime()) + 'T' + strftime('%H%M%S', gmtime()) + 'Z'
    message = datetimeGMT + method + path + (query[0] if query else "")

    signature = hmac.new(bytes(secretKey, "utf-8"),
                         message.encode("utf-8"),
                         hashlib.sha256).hexdigest()

    return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(accessKey, datetimeGMT, signature)


authorization = generateHmac(REQUEST_METHOD, URL, SECRET_KEY, ACCESS_KEY)
url = "{}{}".format(DOMAIN, URL)
response = requests.request(method=REQUEST_METHOD, url=url,
                            headers={
                                "Authorization": authorization,
                                "Content-Type": "application/json"
                            },
                            
                            )

data = response.json()

for row in data['data']:
    uid = ""
    upw = ""
    subject = "쿠팡파트너스"
    content = "쿠팡파트너스 \n날짜: {} \n커미션: {}원".format(row['date'], row['commission'])
    hpno = ""
    callback = ""

    jphone = smssend.JmunjaPhone(uid, upw)
    presult = jphone.send(subject, content, hpno)
