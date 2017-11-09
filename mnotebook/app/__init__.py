# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '../templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          '../static')

app = Flask(__name__,
            template_folder=template_dir,
            static_folder=static_dir)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)


from .views import UserAPI
from .views import UserListAPI
from .views import ContainerAdminAPI
from .views import UserAdminAPI
from .views import UserLoginAPI

from flask import Response, render_template

@app.route('/')
def index():
    return Response(
            render_template('index.html', title="Computing Platform"),
            mimetype="text/html")


api.add_resource(UserAPI, '/users/<string:name>',
                 endpoint='user')
api.add_resource(UserListAPI, '/users',
                 endpoint='users')
api.add_resource(ContainerAdminAPI, '/containers/<string:cid>',
                 endpoint='cid_admin')
api.add_resource(UserAdminAPI, '/users/admin',
                 endpoint='u_admin')
api.add_resource(UserLoginAPI, '/users/login',
                 endpoint='u_login')
