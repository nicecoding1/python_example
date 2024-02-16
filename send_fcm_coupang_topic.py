# https://github.com/firebase/firebase-admin-python/blob/master/snippets/messaging/cloud_messaging.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred_path = "coupang-b83fe-firebase-adminsdk-7mcpg-0967b8e8cd.json"
cred = credentials.Certificate(cred_path)
default_app = firebase_admin.initialize_app(cred)

topic = 'testTopic'

message = messaging.Message(
    notification=messaging.Notification(
        title='test',
        body='python push test',
        image='https://icnu.kr/coupang/logo.png'
    ),
    data = {
        'title':'test',
        'message':'python fcm test',
        'mode':'test',
        'data':'12345'
    },
    topic=topic,
)
response = messaging.send(message)
print('Successfully sent message:', response)