from flask import Flask ,redirect,url_for

#create an instance 
app = Flask(__name__)

#define a route
@app.route("/")
def home():
    return "<p>Hello kasongo <a href= 'https://google.com'>google here</a></p>"

# parsing parameters
@app.route("/<name>")
def user(name):
    return f"Hello {name}"

#redirecting
@app.route("/teacher")
def teacher():
    return  redirect(url_for("home")) # parse the actual function not the path

@app.route("/admin")
def admin():
    return  redirect(url_for("user",name = "Admin")) # parse the actual function not the path that takes an arguement
    

if __name__ == "__main__":
    app.debug = True
    app.run()