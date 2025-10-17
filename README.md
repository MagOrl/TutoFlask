# TutoFlask

- ARSAMERZOEV
- Magomed
- 2.3

#### Instruction d'installation

##### Dépendances : 
- Flask>=2.3
- Flask-Bootstrap5>=1.5.0
- Flask-Login>=0.6
- Flask-WTF>=1.1
- Flask-SQLAlchemy>=3.0
- SQLAlchemy>=2.0
- WTForms>=3.0
- python-dotenv>=1.0
- email-validator>=1.3

```
pip install -r ~/TutoFlask/requirements.txt
```
##### Création de la BD : 
```
flask loaddb monApp/data/data.yml
flask syncdb
```
##### Crée un utilisateur : 
```
flask newuser [Login] [Mdp]
```
##### Lancement du site : 
```
flask run
```