from flask import Flask, render_template, redirect, request
# from flask_session import Session
from cs50 import SQL


app = Flask(__name__)
db = SQL("sqlite:///lecture.db")

# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)


@app.route("/")
def tasks():
    rows = db.execute("SELECT * FROM registrants")
    return render_template("index.html", rows=rows)


#     if "todos" not in session:
#         session["todos"] = []
#     return render_template("tasks.html", todos=session["todos"])


@app.route("/register", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        if not name:
            return render_template("sorry.html", message="You must provide a name")
        email = request.form.get("email")
        if not email:
            return render_template("sorry.html", message="You must provide an email")
        db.execute(
            "INSERT INTO registrants (name, email) VALUES (:name, :email)",
            name=name, email=email)
        return redirect("/")
