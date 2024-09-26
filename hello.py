from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class Form(FlaskForm):
    name=StringField('What is your name?', validators=[DataRequired(message="Name is required.")])
    submit=SubmitField('Submit')
    email=StringField('What is your UofT Email address?', validators=[DataRequired("Email is required."), 
                                                                      Email(message="Please include an '@' in the email address.")])
    submit=SubmitField('Submit')

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/', methods=['GET', 'POST'])
def index(): 
    form = Form()
    if form.validate_on_submit(): 
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data: 
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['email'] = form.email.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'), current_time=datetime.now())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.now())

@app.errorhandler(404)
def page_not_found(e): 
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500