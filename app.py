from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"

users = {
    "alice": {"id": "1", "name": "Alice", "email": "alice@example.com", "password": "pass1"},
    "bob": {"id": "2", "name": "Bob", "email": "bob@example.com", "password": "pass2"},
    "charlie": {"id": "3", "name": "Charlie", "email": "charlie@example.com", "password": "pass3"},
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].lower()
        password = request.form["password"]
        user = users.get(username)
        if user and user["password"] == password:
            session["user_id"] = user["id"]
            return redirect(url_for("user_profile"))
        return "Invalid credentials"
    return render_template("login.html")

@app.route("/user")
def user_profile():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    for user in users.values():
        if user["id"] == user_id:
            return render_template("user.html", user=user)
    return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
