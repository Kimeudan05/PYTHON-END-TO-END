from flask import render_template, request, flash, redirect, url_for

from models import Person


def register_routes(app, db):

    @app.route("/", methods=["POST", "GET"])
    def index():
        if request.method == "POST":
            # handle form submission
            name = request.form.get("name")
            age = request.form.get("age")
            job = request.form.get("job")

            # avoid crushing if age is blank
            age = int(age) if age else None

            # create and save a new record
            person = Person(name=name, age=age, job=job)
            db.session.add(person)
            db.session.commit()

            flash("Person added successifully", "success")
            # redirect to avoid resubmission
            return redirect(url_for("index"))

        # get request -> display people
        people = Person.query.all()
        return render_template("index.html", people=people)

    @app.route("/delete/<int:pid>", methods=["DELETE"])
    def delete(pid):
        person = Person.query.get(pid)
        if person:
            db.session.delete(person)
            db.session.commit()
            flash(f"Deleted {person.name} successfully!", "danger")
            return ("", 204)  # ✅ empty response for JS fetch()
        else:
            return ("Not found", 404)

    @app.route("/details/<int:pid>")
    def details(pid):
        person = Person.query.filter(Person._id == pid).first()
        return render_template("details.html", person=person)
