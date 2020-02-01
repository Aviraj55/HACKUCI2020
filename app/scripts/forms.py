# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators
from wtforms.validators import NumberRange

class IngredientsForm(FlaskForm):
    ingredient = StringField('Ingredient:', validators=[validators.required()])
    time = IntegerField('Cooking Time: ', validators=[validators.required()])
    add = SubmitField('Add')
    
