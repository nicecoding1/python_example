# https://github.com/firebase/firebase-admin-python/blob/master/snippets/messaging/cloud_messaging.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred_path = "coupang-b83fe-firebase-adminsdk-7mcpg-0967b8e8cd.json"
cred = credentials.Certificate(cred_path)
default_app = firebase_admin.initialize_app(cred)

registration_token = 'fMtg9MuSTBi80CWFjH3ShU:APA91bFwQlHt_Ratbt2CwjBi4coEFFj3IoY5xGZbcU_mBANs-cH4001Dg1H_jadQumV3bixqlAClmuTevP6ZvvtpZqXLO79x6Jw4edz7pY9DiK1u9BWenlUz196vTcZsksypJpA-QumC'
# registration_token = 'f1jcyan9RLWLKa77ZFvVaz:APA91bGTmueB6iQFyKkaWJqI9xnIbMZ_qp2S0tR7hkMvERE4VCyag5tZPgybeRTnb3R7ai6pj8zDXLxHyUu9qzrQWSmoQVjEcKunvSvs1CkGXU2dkGm7SEL_PtX2XByJYtlM0k8MyoFW'

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
    token=registration_token,
)
response = messaging.send(message)
print('Successfully sent message:', response)