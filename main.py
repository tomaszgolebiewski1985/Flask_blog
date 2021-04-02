from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# create flask instance
app = Flask(__name__)

app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

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
	favorite = ['Pepperoni', 'Cheese', 'Tuna', 'Hawaii']
	return render_template("index.html", first_name=first_name, stuff=stuff, favorite=favorite)

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
