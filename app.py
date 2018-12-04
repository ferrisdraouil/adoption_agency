from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def display_homepage():
    """Function to query db and display info on all pets"""

    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """Handle adding a pet using the add pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_add_form.html', form=form)


@app.route('/<int:pid>', methods=['GET', 'POST'])
def display_data_for_one_pet(pid):
    pet = Pet.query.get_or_404(pid)

    form = AddPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect(f'/{pid}')
    else:
        return render_template('single_pet.html', pet=pet)