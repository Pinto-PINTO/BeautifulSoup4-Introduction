import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('multi-asset-analyzer-firebase-adminsdk-1os8a-a801228422.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://multi-asset-analyzer-default-rtdb.firebaseio.com'
})


ref = db.reference('COT').child("Currency")
data = {'symbol': 'USD', 'long_percent': '19.3%', 'short_percent': '88.3%'}
ref.set(data)







