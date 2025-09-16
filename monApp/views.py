from .app import app 
from flask import render_template,request
from monApp.models import Auteur
@app.route('/')
def index():
    if len(request.args)==0:
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name="Cricri")
    else :
        param_name = request.args.get('name')
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name=param_name)
@app.route('/about')
def about():
    return render_template("about.html",title ="à propos",name="Magomed")

@app.route('/contact')
def contact():
    return render_template("contact.html",name ="Magomed",contact = "magomed.arsamerzoev@etu.univ-orleans.fr",age = "19")

@app.route('/auteurs/')
def getAuteur():
    lesAuteurs = Auteur.query.all().join().A 
    return render_template('auteurs_list.html', title="R3.01 Dev Web avec Flask", auteurs=lesAuteurs)

if __name__== "__main__" :
    app.run()
