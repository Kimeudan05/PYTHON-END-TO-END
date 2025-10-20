from flask import Flask, render_template

from blueprint8 import blue_print


app = Flask(__name__)
app.register_blueprint(
    blue_print, url_prefix="/admin"
)  # we can only access the defined blueprint routes using the /admin


@app.route("/home")
@app.route("/")
def home():
    return "<h1>Test Application using blueprints</h1>"


if __name__ == "__main__":
    app.run(debug=True)
