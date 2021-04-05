from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Creating Secret Key (in real project dont push this to repository)
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know" 

db = SQLAlchemy(app)

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(200), nullable=False, unique=True)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Name %r>' % self.name

class User_form(FlaskForm):
	name = StringField("Your Name:", validators=[DataRequired()])
	email = StringField("Your Email Adress:", validators=[DataRequired()])
	submit = SubmitField("Submit")


# create form class
class Namer_form(FlaskForm):
	name = StringField("What's Your Name?", validators=[DataRequired()])
	submit = SubmitField("Submit")

# create a route decorator
@app.route('/')

# def index():
#    return "<h1>Hello World</h1>"

def index():
	first_name = "Tomasz"
	stuff = "This is bold text"
	favorite = ["Pepperoni", "Cheese", "Hawaii"]
	return render_template("index.html", first_name=first_name, stuff=stuff, favorite=favorite)

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
	name = None
	form = User_form()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user is None:
			user = Users(name=form.name.data, email=form.email.data)
			db.session.add(user)
			db.session.commit()
		name = form.name.data
		form.name.data = ''
		form.email.data = ''
		flash("User added successfully!!!")
	our_users = Users.query.order_by(Users.date_created)
	return render_template("add_user.html", form=form, name=name, our_users=our_users)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Create Custom Error Pages

# Iinvalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal serwer error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
	name = None
	form = Namer_form()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("Form Submitted Succesfully!")
	return render_template("name.html", name=name, form=form)
