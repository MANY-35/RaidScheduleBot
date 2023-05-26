import firebaseService as fs

fsManager = fs.FirebaseAction()
if fsManager.initFirebase():
    print("success")

fsManager.initTeam()