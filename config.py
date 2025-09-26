import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')

SECRET_KEY='grbS>}U&oU&S/JK]_9X Ep%O'
ABOUT = "Bienvenue sur la page à propos de Flask !"
INFOS = "ARSAMERZOEV Magomed, 18 ans, célibataire et libre comme l'air"
BOOTSTRAP_SERVE_LOCAL = True
             