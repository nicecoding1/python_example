import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred_path = "firebase-adminsdk-myproject.json"
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

registration_token = 'user_token'

message = messaging.Message(
    notification=messaging.Notification(
        title='test',
        body='python push test'
    ),
    token=registration_token,
)
response = messaging.send(message)
print('Successfully sent message:', response)
