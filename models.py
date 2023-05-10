from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Pet """
    __tablename__ = 'pets'

    def __repr__(self):
        p = self
        return f"<Pet id= {p.id} Pet name= {p.name} Pet species= {p.species} Pet image url= {p.photo_url} Pet age= {p.age} Pet notes= {p.notes} Pet availability= {p.available}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=False)
    available = db.Column(db.Boolean, unique=False,
                          nullable=False, default=True)
