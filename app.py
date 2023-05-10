from flask import Flask, request, render_template, redirect, flash, session, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "petsarecool21123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()


@app.route('/')
def root():
    return redirect("/pets")


@app.route('/pets')
def list_pets():
    """List all pets"""
    pets = Pet.query.all()
    return render_template("home.j2", pets=pets)


@app.route('/add', methods=["GET"])
def show_form():
    """ View Pet Form """
    form = AddPetForm()
    return render_template("form.j2", form=form)


@app.route('/add', methods=["POST"])
def create_pet():
    """ Create Pet """
    form = AddPetForm()

    # if form.validate_on_submit():
    #     name = form.name.data
    #     species = form.species.data
    #     photo_url = form.photo_url.data
    #     age = form.age.data
    #     notes = form.notes.data
    #     available = form.available.data
    #     flash(f"{name} has been Added")
    #     return redirect("/pets")
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))

    else:
        return render_template("form.j2", form=form)


@app.route('/<int:pid>', methods=["GET"])
def show_pet(pid):
    """handles show pet request"""
    form = EditPetForm()
    pet = Pet.query.get_or_404(pid)
    return render_template("details.j2", form=form, pet=pet)


@app.route('/<int:pid>', methods=["POST"])
def edit_pet(pid):
    """Show Details/Edit Form of Specific Pet"""
    pet = Pet.query.get_or_404(pid)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f" Pet {pid} updated!")
        return redirect(f"/{pid}")
    else:
        return render_template("details.j2", form=form)
