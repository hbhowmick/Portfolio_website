from app import app
from flask import render_template, url_for


@app.route('/')
@app.route('/index')
def index():
    heading = 'Home'
    return render_template('index.html', title='Home', heading=heading)


@app.route('/about')
def about():
    heading = 'About'
    return render_template('about.html', title='About', heading=heading)

@app.route('/portfolios')
def portfolios():
    heading = 'Portfolios'
    return render_template('portfolios.html', title='Portfolios', heading=heading)
