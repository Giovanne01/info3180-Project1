from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import StringField, SelectField,TextAreaField, FileField, IntegerField,DecimalField
from wtforms.validators import InputRequired

class CreateProperties(FlaskForm):
    title= StringField('Property Title', validators=[InputRequired()])
    bednum = StringField('No. of Rooms', validators=[InputRequired()])
    bathnum= StringField('No. of Bathrooms', validators=[InputRequired()])
    location= StringField('Location', validators=[InputRequired()])
    price= StringField('Price', validators=[InputRequired()])
    type= SelectField('Property Type', choices=['House','Apartment'], validators=[InputRequired()])
    description= TextAreaField('Description', validators=[InputRequired()])
    photo= FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'])])
