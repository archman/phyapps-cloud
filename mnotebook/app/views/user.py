# -*- coding: utf-8 -*-

from flask import abort
from flask import render_template
from flask import Response

from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal
from flask_restful import reqparse

from ..models import User, Admin
from ..models import db
from ..auth import auth
from ..utils import request_json


user_fields = {
    'name': fields.String,
    'admin': fields.String(attribute=lambda x: x.admin_name()),
    'uri': fields.Url('user', absolute=False),
    'timestamp': fields.String(attribute=lambda x:x.local_time()),
    'description': fields.String,
    'container_id': fields.String,
    'container_name': fields.String(attribute=lambda x:x.container_name()),
    'server_url': fields.String,
    'container_status': fields.String(attribute=lambda x:x.container_status()),
}


class UserAPI(Resource):
    #decorators = [auth.login_required]
    def __init__(self):
        self.rp = reqparse.RequestParser()
        self.rp.add_argument('name', type=str, location='json')
        self.rp.add_argument('description', type=str, location='json')
        self.rp.add_argument('container_id', type=str, location='json')
        self.rp.add_argument('container_name', type=str, location='json')
        self.rp.add_argument('server_url', type=str, location='json')
        super(UserAPI, self).__init__()

    def get(self, name):
        user = User.query.filter(User.name==name).first()
        if user is None:
            abort(404)

        if request_json():
            return {'user': marshal(user, user_fields)}
        return Response(
                    render_template('show_item.html',
                        item=marshal(user, user_fields),
                        title="Inspection of {}".format(name)),
                    mimetype='text/html')
    
    @auth.login_required
    def put(self, name):
        # todo: handle admin?
        user = User.query.filter(User.name==name).first()
        if user is None:
            abort(404)
        args = self.rp.parse_args()
        print(args.items())
        for k, v in args.items():
            if v is not None:
                setattr(user, k, v)

        db.session.commit()
        return {'user': marshal(user, user_fields)}

    @auth.login_required
    def delete(self, name):
        user = User.query.filter(User.name==name).first()
        if user is None:
            abort(404)
        db.session.delete(user)
        db.session.commit()
        return {'result': True}


class UserListAPI(Resource):
    #decorators = [auth.login_required]
    def __init__(self):
        self.rp = reqparse.RequestParser()
        self.rp.add_argument('name', type=str, required=True,
                help='No user name provided', location='json')
        self.rp.add_argument('description', type=str, default='TBA',
                location='json')
        self.rp.add_argument('admin', type=str, default='',
                location='json')
        self.rp.add_argument('container_id', type=str, default='',
                location='json')
        self.rp.add_argument('server_url', type=str, default='',
                location='json')
        super(UserListAPI, self).__init__()

    def get(self):
        users = User.query.all()
        print users
        if request_json():
            return {'users': [marshal(u, user_fields) for u in users]}
        return Response(
                    render_template('show_items.html',
                        items=[marshal(u, user_fields) for u in users]),
                        mimetype='text/html')

    @auth.login_required
    def post(self):
        user = self.rp.parse_args()
        u_name = user.get('name')
        if u_name is None or u_name == '':
            abort(400)

        u = User.query.filter(User.name==u_name).first()
        if u is not None:
            return {'error': 'user exists'}, 400
        else:
            admin = Admin.query.filter(Admin.nickname==user.get('admin')).first()
            if admin is None:
                if user.get('admin') == '':
                    admin = Admin.query.all()[0]
                else: # does not work
                    admin = Admin(nickname=user.get('admin'), email='TBA')
                    db.session.add(admin)
                
            new_u = User(name=u_name, 
                         admin=admin,
                         description=user.get('description'),
                         container_id=user.get('container_id'),
                         server_url=user.get('server_url'),
                    )
            db.session.add(new_u)
            db.session.commit()
            return {'user': marshal(new_u, user_fields)}, 201
