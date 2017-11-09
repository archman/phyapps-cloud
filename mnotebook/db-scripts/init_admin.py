#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Initialize user
"""

import sys
sys.path.insert(0, '../')

from app.models import User
from app.models import db


u1 = User(nickname='dev1', email='dev1@localhost', id=1)

# users:
db.session.add(u1)
db.session.commit()
