from flask import Flask, render_template

# create flask instance
app = Flask(__name__)

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