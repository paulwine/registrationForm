from flask import Flask, redirect, session, render_template, request, flash
import re

app = Flask(__name__)

app.secret_key = "SECRETSHIT"

EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
NAME_REGEX = re.compile(r"^[a-zA-z]")


@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/", methods =["POST"])
def submitForm():
    if 'error' in session:
        session.pop("error")
    
    
    session["first"] = request.form["firstname"]
    print(session["first"])

    session["last"] = request.form["lastname"]
    print(session["last"])

    session["email"] = request.form["email"]
    print(session["email"])

    session["password"] = request.form["password"]
    print session["password"]

    session["confirm"] = request.form["confirm"]
    print session["confirm"]

    if len(session["first"]) < 1 or len(session["last"]) < 1 or len(session["email"]) < 1 or len(session["password"]) < 1 or len(session["confirm"]) < 1:
        flash("INPUT ALL FIELDS DUMMY")
        
    if not NAME_REGEX.match(session["first"]):
        flash("NAMES CANNOT CONTAIN NUMBERS OR SYMBOLS")
        session["error"] = 1
        
    if not NAME_REGEX.match(session["first"]):
        flash("NAMES CANNOT CONTAIN NUMBERS OR SYMBOLS")
        session["error"] = 1
        
        
    if not EMAIL_REGEX.match(session["email"]):
        flash("EMAIL NOT FORMATTED CORRECTLY")
        session["error"] = 1

    if len(session["password"]) < 8:
        flash("PASSWORDS MUST BE LONGER THAN 8 CHARACTERS")
        session["error"] = 1

    if session["password"] != session["confirm"]:
        flash("PASSWORDS DID NOT MATCH")
        session["error"] = 1

    # if session[""]
        
        session["error"] = 1

    
    
    if 'error' in session:
        return redirect("/")
    else:
        return redirect("/newuser")

    
    

@app.route("/newuser")
def submitted():
    return render_template("newuser.html")

app.run(debug=True)