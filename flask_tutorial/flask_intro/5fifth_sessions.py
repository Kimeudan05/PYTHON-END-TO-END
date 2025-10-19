from flask import Flask ,redirect,url_for,render_template,request,session
from datetime import timedelta

#create an instance  and set some session data
app = Flask(__name__)
app.secret_key="2013@Wewe"
# we are preventing a session from being deleted when we close the browser
app.permanent_session_lifetime =timedelta(minutes=5)
#define a route
@app.route("/")
def home():
    return render_template("test.html")

# a login that sends the name and redirects to the user page
@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        # it will last for the time defined (By default is false) and deletes session when we close the browser
        session.permanent =True
        # get the data send from the form
        user = request.form["name"]
        session["user"]= user
        return redirect(url_for("user"))
    else:
        # when you retry /login when logged in , you will be redirected to the /user
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

# this redirects to the user when we enter a name and keep it in session
@app.route("/user")
def user():
    if "user" in session:
        user =session["user"]
        return f"Welcome <h1>{user}</h1> to the site visit"
    else:
        #if not logged in and try /user you will be redirected to login
        return redirect(url_for("login"))

# clear sessions
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

@app.route("/kasongo")
def kasongo():
    return render_template("mukui.html")

if __name__ == "__main__":
    app.debug = True
    app.run()