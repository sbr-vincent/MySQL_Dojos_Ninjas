from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = Dojo.get_all()
    print(users)
    return render_template("index.html", all_users = users)

# relevant code snippet from server.py

@app.route("/dojos")
def all_users():
    # call the get all classmethod to get all users
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)

@app.route("/ninjas")
def ninja_form():
    # call the get all classmethod to get all users
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("new_ninjas.html", all_dojos = dojos)

@app.route('/dojo/<dojo_id>')
def one_dojo(dojo_id):
    data = {
        'id': dojo_id
    }

    this_dojo = Dojo.get_dojo_with_ninjas(data)
    print(this_dojo)
    return render_template('show_Dojo.html', this_dojo=this_dojo)

@app.route("/dojo_ninjas", methods=["POST"])
def dojo_ninjas():
    # call the get all classmethod to get all users
    
    data = {
        "dojo_id": request.form["dojo_id"],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"]
    }
    new_Ninja_id = Ninja.save(data)
    print(new_Ninja_id)

    return redirect(f"/dojo/{data['dojo_id']}")
