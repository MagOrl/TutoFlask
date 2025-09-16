from .app import app 
from flask import render_template
@app.route('/')
def index():
    return render_template("index.html",title ="R3.01 Dev Web avec Flask",name="Cricri")
@app.route('/about')
def about():
    return render_template("about.html",title ="à propos",name="Magomed")

@app.route('/contact')
def contact():
    return render_template("contact.html",name ="Magomed",contact = "magomed.arsamerzoev@etu.univ-orleans.fr",age = "19")

if __name__== "__main__" :
    app.run()
