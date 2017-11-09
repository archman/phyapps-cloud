# -*- coding: utf-8 -*-

from flask import render_template
from flask import Response
from flask import request
from flask import abort
from flask_restful import Resource
from flask_restful import marshal

from ..models import User
from ..models import db
from .user import user_fields
from ..utils import request_json


class UserLoginAPI(Resource):
    def __init__(self):
        super(UserLoginAPI, self).__init__()

    def get(self):
        return Response(
                render_template('login.html',),
                mimetype="text/html")

    def post(self):
        form_input = request.form
        username = form_input.get('username')
        password = form_input.get('password')
        if username is None or password is None:
            abort(400)

        reg = form_input.get('register')
        if reg == 'login':
            user = User.query.filter(User.name==username).first()
            if user is None:
                abort(404)
                
            # authenticate user info
            print(user.is_authenticated)
            #if user.is_authenticated:
            #    return Response(
            #            render_template(),
            #            mimetype='text/html')
            #else:
            #    abort(401)
        elif reg == 'signup':
            if User.query.filter(User.name==username).first() is not None:
                abort(400)
            # register new user
            user = User(name=username)
            user.hash_passwd(password)
            db.session.add(user)
            db.session.commit()
            if request_json():
                return {'User account': user.name}, 201
            return Response(
                    render_template('show_item.html',
                        item=marshal(user, user_fields)),
                    mimetype='text/html')
        

