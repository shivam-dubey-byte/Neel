from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY']='afasdfasdfadfasdfad#'

@app.route("/")
def index():
    return render_template('home.html',home='active',about='',contact='',donate="")
@app.route("/1")
def index1():
    return render_template('index.html',home='active',about='',blog='',contact='',donate="")
@app.route("/about")
def about1():
    return render_template('AboutUs.html',home='',about='active',donate="")

@app.route("/about1")
def about():
    return render_template('about.html',home='',about='active',donate="")
    #,home='active',about='',blog='',contact='',donate=""
@app.route("/blog")
def blog():
    return render_template("blog.html",home='',about='',blog='active',contact='',donate="")
@app.route("/contact")
def contact():
    return render_template("contact.html",home='',about='',contact='active',donate="")
@app.route("/donate")
def donate():
    return render_template("donate.html",home='',about='',contact='',donate="active")
@app.route("/donate1")
def donate1():
    return render_template("donate1.html",home='',about='',contact='',donate="active")
