from flask import Flask, request, render_template

app = Flask(__name__)

users = {
    "1": {"name": "Alice", "email": "alice@example.com"},
    "2": {"name": "Bob", "email": "bob@example.com"},
    "3": {"name": "Charlie", "email": "charlie@example.com"},
}

@app.route("/user")
def user_profile():
    user_id = request.args.get("id")
    user = users.get(user_id)
    if user:
        return render_template("user.html", user=user)
    return "User not found", 404

if __name__ == "__main__":
    app.run(debug=True)