from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    property_title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Decription', validators=[InputRequired()])
    bedrooms = IntegerField('No. of Bedrooms', validators=[InputRequired()])
    bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    type = SelectField('Property Type', validators=[InputRequired()], choices= [('house', 'House'), ('apartment', 'Apartment')])
    location = StringField('Location', validators=[InputRequired()])
    image = FileField('Photo', validators=[FileRequired(message="Browse"), FileAllowed(['jpg', 'jpeg', 'png'], "Images Only") ], render_kw={"accept": "image/*"})
    add_property = SubmitField('Add Property')