from flask import (
    Flask,
    render_template,
    request,
    Response,
    send_from_directory,
    jsonify,
    session,
    make_response,
    flash,
    redirect,
    url_for,
)
import pandas as pd
import os
import uuid

app = Flask(
    __name__, template_folder="templates", static_folder="static", static_url_path="/"
)

# set a secret key for dealing with sessions and cookies
app.secret_key = "MASILA_SECTRET"


# routes
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form.get("name")
        password = request.form.get("password")

        if name == "masila" and password == "1234":
            return "<p>Login success</p>"
        else:
            return "<p>Invalid credentials</p>"


@app.route("/file_upload", methods=["POST", "GET"])
def file_upload():

    if request.method == "GET":
        render_template("index.html")
    else:
        file = request.files.get("file")
        if not file:
            return "file not uploaded"
        if file.content_type == "text/plain":
            return file.read().decode()
        elif (
            file.content_type
            == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            df = pd.read_excel(file)
            return df.to_html(index=False)


@app.route("/convert_csv", methods=["POST", "GET"])
def convert_csv_two():

    if request.method == "GET":
        render_template("index.html")
    else:
        file = request.files.get("file")
        if not file:
            return "file not uploaded"

        df = pd.read_excel(file)
        response = Response(
            df.to_csv(index=False),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment;filename=results.csv"},
        )
        return response


@app.route("/convert_csv_two", methods=["POST", "GET"])
def convert_csv():

    if request.method == "GET":
        render_template("index.html")
    else:
        file = request.files.get("file")
        if not file:
            return "file not uploaded"
        df = pd.read_excel(file)
        if not os.path.exists("masilacsvs"):
            os.mkdir("masilacsvs")
        filename = f"{uuid.uuid4()}.csv"
        df.to_csv(os.path.join("masilacsvs", filename), index=False)
        return render_template("downloads.html", filename=filename)


@app.route("/downloads/<filename>")
def downloads(filename):
    return send_from_directory("masilacsvs", filename, download_name="results.csv")


@app.route("/home/<name>")
def cld(name):
    return f"<p>My name is {name}</p>"


@app.template_filter("filter_reverse")
def filter_reverse(s):
    return s[::-1]


@app.route("/handle_post", methods=["POST"])
def handle_post():
    greeting = request.json["greeting"]
    name = request.json["name"]

    with open("file.txt", "w") as f:
        f.write(f"{greeting}, {name}")

    return jsonify({"message": "successiful writen"})


# sessions and cookies
# sessions are stored in the server while cookies are in the browser and can be manipulated any time
@app.route("/set_data")
def set_data():
    session["name"] = "Masila"
    session["other"] = "Other data"
    return render_template("index.html", message="Session data set")


@app.route("/get_data")
def get_data():
    if "name" in session.keys() and "other" in session.keys():
        name = session["name"]
        other = session["other"]
        return render_template("index.html", message=f" Name : {name}, Other : {other}")
    else:
        return render_template("index.html", message="No session data set")


@app.route("/clear_session")
def clear_session():
    session.clear()
    return render_template("index.html", message="Session data cleared")


@app.route("/clear_one")
def clear_one():
    name = session.get("name", "Unknown")
    if "other" in session.keys():
        session.pop("other", None)  # remove if exists
        message = f"Name :{name},Other : Cleared"
    else:
        message = f"Name : {name} Other : Not Found"
    return render_template("index.html", message=message)


# cookies


@app.route("/set_cookie")
def set_cookie():
    response = make_response(
        render_template("index.html", message="Cookie has been set")
    )
    response.set_cookie("agenda", "Learn and build with flask")
    response.set_cookie("games", "Games help us unite and do some practice")

    return response


@app.route("/get_cookie")
def get_cookie():
    agn = request.cookies.get("agenda")
    return render_template("index.html", message=f"Cooking value :{agn}")


@app.route("/remove_cookie")
def remove_cookie():
    response = make_response(
        render_template("index.html", message="Cookie has been cleared")
    )
    response.delete_cookie("agenda")
    return response


@app.route("/show_all_cookies")
def show_cookies():
    cookies = request.cookies
    if not cookies:
        message = "No cookies found"
    else:
        for name, value in cookies.items():
            print(f"Cookie :{name} -> {value}")
        cookie_names = list(cookies.keys())
        message = f"Cookies found : {cookie_names}"
    return render_template("index.html", message=message)


# flashed Messages
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        render_template("login.html")
    else:
        name = request.form.get("name")
        password = request.form.get("password")

        if name == "mas" and password == "jan":
            flash("login success")
            return redirect(url_for("get_cookie"))  # go to to the index form
        else:
            flash("Wrong credentials")
            return redirect(url_for("login"))
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
