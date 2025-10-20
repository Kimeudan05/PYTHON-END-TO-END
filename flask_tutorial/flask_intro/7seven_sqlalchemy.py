from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

# create an instance  and set some session data
app = Flask(__name__)
app.secret_key = "2013@Wewe"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TARCK_MODIFICATIONS"] = False
# we are preventing a session from being deleted when we close the browser
app.permanent_session_lifetime = timedelta(minutes=5)


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email


# define a route
@app.route("/")
def home():
    return render_template("test.html")


# a login that sends the name and redirects to the user page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # it will last for the time defined (By default is false) and deletes session when we close the browser
        session.permanent = True
        # get the data send from the form
        user = request.form["name"]
        session["user"] = user

        found_user = User.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = User(user, "")
            db.session.add(usr)
            db.session.commit()
        flash("login successiful")
        return redirect(url_for("user"))
    else:
        # when you retry /login when logged in , you will be redirected to the /user
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user"))
        return render_template("login.html")


# this redirects to the user when we enter a name and keep it in session
@app.route("/user", methods=["GET", "POST"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = User.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()

            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        # if not logged in and try /user you will be redirected to login
        flash("you are not logged in. Login!!")
        return redirect(url_for("login"))


# clear sessions
@app.route("/logout")
def logout():
    # show message only if we had a user in session
    if "user" in session:
        user = session["user"]
    session.pop("user", None)
    session.pop("email", None)
    flash(f"You have been logged out", "info")
    return redirect(url_for("login"))


@app.route("/view", methods=["POST", "GET"])
def view():
    return render_template("view.html", values=User.query.all())


if __name__ == "__main__":
    with app.app_context():  # app.app_context() provides the necessary con
        db.create_all()
    app.debug = True
    app.run()
