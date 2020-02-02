
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
# from flask_heroku import Heroku
# heroku = Heroku(app)

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

@app.route("/results")
def results():
    plain_json = get_all_valid_recipes(INGREDIENTS_LIST)
    clean_ads(plain_json)
    #clean_ads(plain_json)
    #clean_ads(example)
    #print(type(example))
    #print(type(plain_json))
    if len(INGREDIENTS_LIST) < 7:
        return render_template('error.html')
    return render_template('results.html', recipes=plain_json)

@app.route("/error")
def error():
    return render_template('error.html')
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
