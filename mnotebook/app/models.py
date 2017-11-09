# -*- coding: utf-8 -*-

from datetime import datetime

from passlib.apps import custom_app_context as pwd_context

from . import db
from .utils import utc2local
from .utils import get_container_status
from .utils import get_container_name


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    users = db.relationship('User', backref='admin', lazy='dynamic')
    timestamp = db.Column(db.DateTime,
                          default=datetime.utcnow,
                          onupdate=datetime.utcnow)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)
    
    def __repr__(self):
        return "<User '{}'>".format(self.nickname)

    def hash_passwd(self, passwd):
        self.password_hash = pwd_context.encrypt(passwd)

    def verify_passwd(self, passwd):
        return pwd_context.verify(passwd, self.password_hash)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.DateTime,
                          default=datetime.utcnow,
                          onupdate=datetime.utcnow)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    description = db.Column(db.String(100))

    container_id = db.Column(db.String(100))
    server_url = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))

    def container_name(self):
        return get_container_name(self.container_id)

    def local_time(self):
        return utc2local(self.timestamp)

    def admin_name(self):
        return Admin.query.filter().first().nickname

    def container_status(self):
        return get_container_status(self.container_id)
    
    def __repr__(self):
        return "<User '{}'>".format(self.name)

    @property
    def is_authenticated(self):
        return True

    def hash_passwd(self, passwd):
        self.passwd_hash = pwd_context.encrypt(passwd)

    def verify_passwd(self, passwd):
        return pwd_context.verify(passwd, self.passwd_hash)

