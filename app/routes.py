from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import PostForm, LoginForm, RegisterForm
from app.models import Post, User
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index')
@app.route('/index/<header>', methods=['GET'])
def index(header=''):
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    heading = 'Sign In'
    # if user is logged in already, redirect them to home page
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('index'))


    form = LoginForm()

    # check if form is submitted - if so, log user in
    if form.validate_on_submit():

        # query the database for the user trying to log in
        user = User.query.filter_by(username=form.username.data).first()

        # if user doesn't exist, reload page and flash message
        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect.')
            return redirect(url_for('login'))

        # if user does exist, and credentials are correct, log them in
        login_user(user, remember=form.remember_me.data)
        flash('You are now logged in!')
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form, heading=heading)

@app.route('/register', methods=['GET', 'POST'])
def register():
    heading = 'Sign In'
    # if user is logged in already, do not let them access this page
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data
        )

        # set the password hash
        user.set_password(form.password.data)

        # add to stage and commit to db, then flash and return
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form, heading=heading)


@login_required
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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
