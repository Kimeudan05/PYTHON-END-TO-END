from flask import (
    Flask,
    render_template,
    request,
    Response,
    send_from_directory,
)
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder="templates")


# routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        if name == "SavvySolveTech" and password == "2013@Wewe":
            return f" Success </br> Name: {name} password : {password}"
        else:
            return "Invalid credentials"


@app.route("/file_upload", methods=["GET", "POST"])
def file_upload():
    file = request.files.get("file")
    if not file:
        return "No file selected"

    if file.content_type == "text/plain":
        return file.read().decode()
    elif (
        file.content_type
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        df = pd.read_excel(file)
        return df.to_html(index=False, classes="table table bordered")


@app.route("/convert_csv", methods=["GET", "POST"])
def convert_csv():
    file = request.files.get("file")

    df = pd.read_excel(file)
    reponse = Response(
        df.to_csv(index=False),
        200,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=result.csv"},
    )
    return reponse


@app.route("/convert_csv_two", methods=["POST", "GET"])
def convert_csv_two():
    file = request.files.get("file")

    df = pd.read_excel(file)
    if not os.path.exists("downloads"):
        os.mkdir("downloads")
    filename = f"{uuid.uuid4()}.csv"
    df.to_csv(os.path.join("downloads", filename), index=False)
    return render_template("downloads.html", filename=filename)


@app.route("/downloads/<filename>")
def downloads(filename):
    return send_from_directory("downloads", filename, download_name="results.csv")


if __name__ == "__main__":
    app.run(debug=True)
