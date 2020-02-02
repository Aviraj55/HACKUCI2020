
# from scripts import forms
from flask import Flask, redirect, url_for, render_template, session, request
from scripts.forms import IngredientsForm
import json
import sys
import os
from get_valid_recipes import get_all_valid_recipes
from clean_advertisement import clean_ads
app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

# Heroku
#from flask_heroku import Heroku
#heroku = Heroku(app)

INGREDIENTS_LIST = []

# ======== Routing =========================================================== #
@app.route('/', methods=['GET', 'POST'])
@app.route('/home',  methods=['GET', 'POST'])
def home():
    form = IngredientsForm()
    # select = request.form.get('comp_select')
    print('form validate?', form.validate_on_submit())
    # if form.validate_on_submit():
    if request.method == 'POST':
        ingredient = form.ingredient.data
        time = form.time.data
        session['ingredients_list'] = ingredient.split(' ')
        global INGREDIENTS_LIST
        INGREDIENTS_LIST = session['ingredients_list']
        return redirect(url_for('results'))
    return render_template('home.html', form=form)


example = {
  "rmK12Uau.ntP510KeImX506H6Mr6jTu": {
    "title": "Slow Cooker Chicken and Dumplings",
    "ingredients": [
      "4 skinless, boneless chicken breast halves ADVERTISEMENT",
      "2 tablespoons butter ADVERTISEMENT",
      "2 (10.75 ounce) cans condensed cream of chicken soup ADVERTISEMENT",
      "1 onion, finely diced ADVERTISEMENT",
      "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.\nCover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center.\n",
    "picture_link": "55lznCYBbs2mT8BTx6BTkLhynGHzM.S"
  },
  "rmK12Uau.ntP510KeImX506H6Mr6Tu": {
    "title": "Chicken and Dumplings",
    "ingredients": [
      "4 skinless, boneless chicken breast halves ADVERTISEMENT",
      "2 tablespoons butter ADVERTISEMENT",
      "2 (10.75 ounce) cans condensed cream of chicken soup ADVERTISEMENT",
      "1 onion, finely diced ADVERTISEMENT",
      "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.\nCover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center.\n",
    "picture_link": "55lznCYBbs2mT8BTx6BTkLhynGHzM.S"
  },
  "rmK12Uau.ntP510KeImX506H6Mr6Tud": {
    "title": "Chicken and Dumplings",
    "ingredients": [
      "4 skinless, boneless chicken breast halves ADVERTISEMENT",
      "2 tablespoons butter ADVERTISEMENT",
      "2 (10.75 ounce) cans condensed cream of chicken soup ADVERTISEMENT",
      "1 onion, finely diced ADVERTISEMENT",
      "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.\nCover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center.\n",
    "picture_link": "55lznCYBbs2mT8BTx6BTkLhynGHzM.S"
  },
  "rmK12Uau.ntP510KeIddmX506H6Mr6Tu": {
    "title": "Chicken and Dumplings",
    "ingredients": [
      "4 skinless, boneless chicken breast halves ADVERTISEMENT",
      "2 tablespoons butter ADVERTISEMENT",
      "2 (10.75 ounce) cans condensed cream of chicken soup ADVERTISEMENT",
      "1 onion, finely diced ADVERTISEMENT",
      "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.\nCover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center.\n",
    "picture_link": "55lznCYBbs2mT8BTx6BTkLhynGHzM.S"
  },
  "rmK12Uau.ntP510KdsdeImX506H6Mr6Tu": {
    "title": "Chicken and Dumplings",
    "ingredients": [
      "4 skinless, boneless chicken breast halves ADVERTISEMENT",
      "2 tablespoons butter ADVERTISEMENT",
      "2 (10.75 ounce) cans condensed cream of chicken soup ADVERTISEMENT",
      "1 onion, finely diced ADVERTISEMENT",
      "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.\nCover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center.\n",
    "picture_link": "55lznCYBbs2mT8BTx6BTkLhynGHzM.S"
  }
}


@app.route("/results")
def results():
    plain_json = get_all_valid_recipes(INGREDIENTS_LIST)
    #clean_ads(plain_json)
    #clean_ads(example)
    #print(type(example))
    #print(type(plain_json))
    return render_template('results.html', recipes=plain_json)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
