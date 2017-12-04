import os

DEBUG = True
#SERVER_NAME = '127.0.0.1:5050'

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# MySQL
SQLALCHEMY_DATABASE_URI = \
    'mysql+pymysql://{username}:{password}@{host}/phyapps_cloud'.format(
        username='dev',
        password='dev',
        host='localhost')

SQLALCHEMY_TRACK_MODIFICATIONS = False
