from monApp.models import Livre
def test_livre_init(): 
	liv = Livre(0,"Foo Bar","","",0)
	assert liv.Titre == "Foo Bar"
 
def test_livre_repr(testapp): #testapp est la fixture définie dans conftest.py
	with testapp.app_context():
		liv = Livre.query.get(1)
		assert repr(liv) == "<Livre (1) Les Misérables>"