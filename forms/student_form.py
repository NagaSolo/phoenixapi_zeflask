from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField

from wtforms.validators import InputRequired

class StudentForm(FlaskForm):
   name = TextField("Name Of Student", validators=[InputRequired(message="Please enter your name.")])
   city = TextField('City', validators=[InputRequired(message="E.g: Kingston")])
   address = TextAreaField("Address", validators=[InputRequired(message="E.g: Lot 777")])
   pin = TextAreaField("PIN", validators=[InputRequired(message="E.g: 789654")])

   submit = SubmitField("Submit")