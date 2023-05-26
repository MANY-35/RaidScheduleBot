import os
import firebase_admin
from firebase_admin import credentials, db

class FirebaseAction() :
    def __init__(self):
        self.root = None

    def initFirebase(self):
        path = os.path.dirname(os.path.abspath(__file__))
        cred = credentials.Certificate(path + '/raidschedulebot-b29f0-firebase-adminsdk-1vkfy-88ad7f499f.json')
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://raidschedulebot-b29f0-default-rtdb.firebaseio.com'} )
        self.root = db.reference()
        if self.root == None:
            return False
        return True

    def initTeam(self, code=""):
        t = self.root.get()
        print(t['team'])