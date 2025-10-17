import pytest
from monApp import app, db, commands
from monApp.models import Auteur, Livre, User


@pytest.fixture
def testapp():
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False
    })
    with app.app_context():
        db.create_all()
        # Ajouter un auteur de test
        auteur = Auteur(Nom="Victor Hugo")
        livre = Livre(Prix=9.99,
                      Titre="Les Misérables",
                      Url="",
                      Img="",
                      auteur_id=auteur.idA)
        from hashlib import sha256
        pwd = "AIGRE"
        m = sha256()
        m.update(pwd.encode())
        user = User(Login="CDAL", Password=m.hexdigest())
        db.session.add(auteur)
        db.session.add(user)
        db.session.add(livre)
        db.session.commit()
    yield app
    # Cleanup après les tests
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(testapp):
    return testapp.test_client()
