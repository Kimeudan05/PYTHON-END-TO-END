from flask import Blueprint, render_template

blue_print = Blueprint(
    "blue", __name__, static_folder="static", template_folder="templates"
)


@blue_print.route("/home")
@blue_print.route("/")  # if thie does not exist we will go to the test app
def home():
    return render_template("blue.html")


@blue_print.route("/test")
def test():
    return "<h1>Test Blueprint</h1>"
