from monApp.models import User ,load_user

def testuser(testapp):
    with testapp.app_context():
        user = User(Login="CDAL",Password="AIGRE")
        assert user == load_user("CDAL")