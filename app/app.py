
# from scripts import forms
from flask import Flask, redirect, url_for, render_template, session, request
from scripts.forms import IngredientsForm
import json
import sys
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

# Heroku
#from flask_heroku import Heroku
#heroku = Heroku(app)

# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET', 'POST'])
@app.route('/home',  methods=['GET', 'POST'])
def home():
    # if not session.get('logged_in'):
    #     form = forms.LoginForm(request.form)
    #     if request.method == 'POST':
    #         username = request.form['username'].lower()
    #         password = request.form['password']
    #         if form.validate():
    #             if helpers.credentials_valid(username, password):
    #                 session['logged_in'] = True
    #                 session['username'] = username
    #                 return json.dumps({'status': 'Login successful'})
    #             return json.dumps({'status': 'Invalid user/pass'})
    #         return json.dumps({'status': 'Both fields required'})
    #     return render_template('login.html', form=form)
    # user = helpers.get_user()
    form = IngredientsForm()
    print('form validate?', form.validate_on_submit())
    # if form.validate_on_submit():
    if request.method == 'POST':
        ingredient = form.ingredient.data
        time = form.time.data
        session['ingredients_list'] = ingredient.split(' ')
        return redirect(url_for('results'))
    return render_template('home.html', form=form)


@app.route("/results")
def results():
    return render_template('results.html')


# -------- Signup ---------------------------------------------------------- #
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if not session.get('logged_in'):
#         form = forms.LoginForm(request.form)
#         if request.method == 'POST':
#             username = request.form['username'].lower()
#             password = helpers.hash_password(request.form['password'])
#             email = request.form['email']
#             if form.validate():
#                 if not helpers.username_taken(username):
#                     helpers.add_user(username, password, email)
#                     session['logged_in'] = True
#                     session['username'] = username
#                     return json.dumps({'status': 'Signup successful'})
#                 return json.dumps({'status': 'Username taken'})
#             return json.dumps({'status': 'User/Pass required'})
#         return render_template('login.html', form=form)
#     return redirect(url_for('login'))


# # -------- Settings ---------------------------------------------------------- #
# @app.route('/settings', methods=['GET', 'POST'])
# def settings():
#     if session.get('logged_in'):
#         if request.method == 'POST':
#             password = request.form['password']
#             if password != "":
#                 password = helpers.hash_password(password)
#             email = request.form['email']
#             helpers.change_user(password=password, email=email)
#             return json.dumps({'status': 'Saved'})
#         user = helpers.get_user()
#         return render_template('settings.html', user=user)
#     return redirect(url_for('login'))


# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
