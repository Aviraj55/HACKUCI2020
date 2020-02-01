# -*- coding: utf-8 -*-
from wtforms import Form, StringField, validators


class IngredientsForm(Form):
    ingredient = StringField('Ingredient:', validators=[validators.required(), validators.Length(min=1, max=30)])
    
