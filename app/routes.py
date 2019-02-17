from app import app, db
from flask import render_template, url_for, redirect
from app.forms import PostForm
from app.models import Post


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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    heading = 'Contact'
    form = PostForm()

    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        msg = form.msg.data
        post = Post(name=name, phone=phone, email=email, msg=msg)

        # add post variable to database stage, then commit
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('contact'))

    contact_info = Post.query.all()

    return render_template('contact.html', title='Contact', form=form, contact_info=contact_info, heading=heading)
