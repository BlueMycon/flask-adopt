import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
from models import connect_db, db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


# Routes
@app.get("/")
def show_homepage():
    """Show Pets Listing"""
    pets = Pet.query.all()

    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Show add pet form and validate the inputs."""

    form = AddPetForm()
    # lookup form.populate_obj
    if form.validate_on_submit():
        # pet = Pet(**form.data)

        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def display_or_edit_pet(pet_id):
    """Pet detail page with edit options."""

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        # pet.photo_url = form.photo_url.data
        # pet.notes = form.notes.data
        # pet.available = form.available.data

        db.session.commit()

        return redirect("/")
    else:
        return render_template("pet_detail.html", form=form, pet=pet)
