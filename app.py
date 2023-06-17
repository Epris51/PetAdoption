from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)


@app.route('/')
def display_pets_list():
    """ Displays up-to-date list of pets. """
    pets = Pet.query.all()
    return render_template('pet_listing.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def display_add_pet_form():
    """ Displays form to add a new pet. """
    form = AddPetForm()

    if form.validate_on_submit():
        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data
        )
        db.session.add(pet)
        db.session.commit()
        flash(f"Added new pet: {pet.name}")
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def display_pet_details_and_edit_form(pet_id):
    """ Shows pet details and edit pet form """
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Edited pet: {pet.name}")
        return redirect(f"/{pet_id}")
    else:
        return render_template("edit_pet.html", form=form, pet=pet)


@app.route('/<int:pet_id>/delete', methods=["POST"])
def delete_pet(pet_id):
    """ Deletes a pet """
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    flash(f"Deleted pet: {pet.name}")
    return redirect("/")

