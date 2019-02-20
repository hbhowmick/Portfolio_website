import os

# root/base of this project folder
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # SQLite database URI, which is the location of database file/server
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(BASEDIR, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # uri for postgres local database
    # not for Heroku usage yet
    # SQLALCHEMY_DATABASE_URI = 'postgresql://<admin>:<password>@<ip_address>:<port_number>/<server_name>'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Then1rb@nd@localhost:5432/portfolio'
