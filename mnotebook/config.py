import os

DEBUG = True
#SERVER_NAME = '127.0.0.1:5050'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_DATABASE_URI = \
#    'mysql+pymysql://{username}:{password}@{host}/unicorn'.format(
#        username='dev',
#        password='dev',
#        host='localhost')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
