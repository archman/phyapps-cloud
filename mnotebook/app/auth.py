from flask_httpauth import HTTPBasicAuth
from flask import make_response
from flask import jsonify

from passlib.apps import custom_app_context

from .models import User
from .models import Admin

auth = HTTPBasicAuth()

users = {
    'compdev': '$6$rounds=656000$PGX0OHSnmJYvJgUQ$riSaArDbDYQCKcsyy03./jt6seAlSh7jmlF3JhXSITXI8m8gRXqx4yT.M9Poao6CL8vRq/ECnehLbTsfhtbcf0',
}

@auth.verify_password
def verify_password(username, password):
    # user or admin
    u = Admin.query.filter(Admin.nickname==username).first()
    if not u:
        return False
    return u.verify_passwd(password)
    #return custom_app_context.verify(password, users.get(username))

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
