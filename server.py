from flask import Flask, redirect, session, render_template, request, flash

app = Flask(__name__)

app.secret_key = "SECRETSHIT"



@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/", methods =["POST"])
def submitForm():
    
    session["firstName"] = request.form["firstname"]
    print(session["firstName"])
    
    return redirect("/newuser")

@app.route("/newuser")
def submitted():
    return render_template("newuser.html")

app.run(debug=True)