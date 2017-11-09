# -*- coding: utf-8 -*-

from datetime import datetime
import pytz
import tzlocal
from flask import request
from yapf.yapflib.yapf_api import FormatCode

import docker
client = docker.from_env()
container_fields_of_interest = ('name', 'id', 'status', 'image')

def utc2local(u_time):
    l_tz = tzlocal.get_localzone()
    l_time = u_time.replace(tzinfo=pytz.utc).astimezone(l_tz)
    return l_time.strftime("%Y-%m-%d %H:%M:%S %Z")


def to_dict(d):
    ret = {}
    for k,v in d.items():
        try:
            ret[k] = float(v)
        except:
            ret[k] = v
    return ret


def get_container_status(cid):
    try:
        return client.containers.get(cid).status
    except:
        return "Unknown"


def get_container_name(cid):
    try:
        return client.containers.get(cid).name
    except:
        return "Unknown"


def request_json():
    best = request.accept_mimetypes \
            .best_match(['application/json', 'text/html'])
    return best == 'application/json'


def validate_container(cid):
    try:
        container = client.containers.get(cid)
        return container, {k:getattr(container, k) for k in container_fields_of_interest}
    except:
        return None, False


def get_container(cid):
    try:
        return client.containers.get(cid)
    except:
        return None
