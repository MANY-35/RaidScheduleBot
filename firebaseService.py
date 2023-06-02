import os
import models
import firebase_admin
from firebase_admin import credentials, db

class FirebaseAction() :
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        cred = credentials.Certificate(path + '/raidschedulebot-b29f0-firebase-adminsdk-1vkfy-88ad7f499f.json')
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://raidschedulebot-b29f0-default-rtdb.firebaseio.com'} )

    def initGuild(self, guild_id:str):
        dir = db.reference('guild_id')
        if guild_id not in dir.get().keys():
            print('new guild')
            dir.update({guild_id:{'userid':'data'}})
        return dir.child(str(guild_id))
    
    def initMember(self, user_id:str, dir):
        if user_id not in dir.get().keys():
            print('new user')
            dir.update({user_id:{'key':{'classname':'contentscode'}}})
        return dir.child(str(user_id))
    
    def createCharacter(self, guild_id:str, user_id:str, data):
        dir = self.initGuild(guild_id=guild_id)
        dir = self.initMember(user_id=user_id, dir=dir)
        dir.push({data['class']:data['code']})
        dir.update({'key':None})
        dir.parent.update({'userid':None})
        
    def getGuildMemberIdList(self, guild_id:str):
        dir = self.initGuild(guild_id=guild_id)
        return list(dir.get().keys())
    
    def getMemberData(self, guild_id:str, user_id:str):
        dir = self.initGuild(guild_id=guild_id) 
        return dir.child(user_id).get()
        