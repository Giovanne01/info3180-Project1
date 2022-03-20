from . import db

class AddProperty(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(255))
    bednum= db.Column(db.String(255))
    bathnum= db.Column(db.String(255))
    location= db.Column(db.String(255))
    price= db.Column(db.String(255))
    type= db.Column(db.String(255))
    description= db.Column(db.String(255))
    photo= db.Column(db.String(255))
