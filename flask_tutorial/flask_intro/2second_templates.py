from flask import Flask ,redirect,url_for,render_template

#create an instance 
app = Flask(__name__)

#define a route
@app.route("/")
def home():
    return render_template("index.html", message = "Masila you are starting flask")

# parsing parameters
@app.route("/<name>")
def user(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.debug = True
    app.run()