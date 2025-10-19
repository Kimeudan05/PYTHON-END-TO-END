from flask import Flask ,redirect,url_for,render_template

#create an instance 
app = Flask(__name__)

#define a route
@app.route("/")
def home():
    return render_template("test.html")

# parsing parameters
@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/kasongo")
def kasongo():
    return render_template("mukui.html")

if __name__ == "__main__":
    app.debug = True
    app.run()