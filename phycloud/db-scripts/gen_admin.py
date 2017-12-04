# -*- coding: utf-8 -*-

from passlib.apps import custom_app_context as pwd_context



admin_name = 'compadmin'

phash = pwd_context.encrypt('todayisthu')

print {'name': admin_name, 'hash': phash}

