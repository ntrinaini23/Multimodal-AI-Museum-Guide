from flask import Flask, render_template, request, redirect, session
import sqlite3
import json
from models.ai_chatbot import ask_ai
from flask import jsonify

app = Flask(__name__)
app.secret_key = "secret123"


def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.close()


init_db()


@app.route("/")
def home():
    return redirect("/login")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        conn.execute("INSERT INTO users VALUES (?,?)", (username, password))
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("signup.html")


@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")

        # check if username exists
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()

        conn.close()

        # if user does not exist → signup page
        if not user:
            return redirect("/signup")

        # if user exists but password wrong → stay on login
        if user[1] != password:
            return render_template("login.html")

        # correct login
        session["user"] = username
        return redirect("/dashboard")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    with open("data/artifacts.json") as f:
        artifacts = json.load(f)

    return render_template("dashboard.html", artifacts=artifacts)


@app.route("/artifact/<id>")
def artifact(id):

    if "user" not in session:
        return redirect("/login")

    with open("data/artifacts.json") as f:
        artifacts = json.load(f)

    artifact = None

    for a in artifacts:
        if a["id"] == id:
            artifact = a
            break

    if artifact is None:
        return "Artifact not found"

    return render_template("artifact.html", artifact=artifact)


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question")
    context = data.get("context")

    answer = ask_ai(question, context)

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)