# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators
from wtforms.validators import NumberRange

class IngredientsForm(FlaskForm):
    ingredient = StringField('Ingredient:', validators=[validators.required(), validators.Length(min=1, max=30)])
    time = IntegerField('Cooking Time: ', validators=[NumberRange(min=5, max=600)])
    add = SubmitField('Add')
    
