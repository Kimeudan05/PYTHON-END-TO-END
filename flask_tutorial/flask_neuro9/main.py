from flask import (
    Flask,
    render_template,
    request,
    Response,
    send_from_directory,
    jsonify,
)
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder="templates")


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


if __name__ == "__main__":
    app.run(debug=True)
