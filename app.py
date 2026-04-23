from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "traffic_secret_key"


# ---------------- LOGIN PAGE ----------------
@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")


# ---------------- REGISTER PAGE ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        session["user"] = request.form["username"]
        session["pass"] = request.form["password"]
        return redirect(url_for("home"))

    return render_template("register.html")


# ---------------- LOGIN PROCESS ----------------
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if "user" in session and "pass" in session:
        if username == session["user"] and password == session["pass"]:
            return redirect(url_for("dashboard"))

    return "Invalid credentials"


# ---------------- DASHBOARD (MAP PAGE) ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


# ---------------- GRAPH PAGE ----------------
@app.route("/graph")
def graph():
    return render_template("traffic_hour_graph.html")


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)