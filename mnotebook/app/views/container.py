# -*- coding: utf-8 -*-


from flask import abort
from flask import request
from flask import Response
from flask import redirect
from flask import url_for
from flask import render_template
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal

from ..utils import validate_container
from ..utils import request_json


container_fields = {
    'name': fields.String,
    'id': fields.String(attribute='id'),
    'image': fields.String,
    'status': fields.String,
}


class ContainerAdminAPI(Resource):
    def __init__(self):
        super(ContainerAdminAPI, self).__init__()
    
    def get(self, cid):
        """
        Parameters
        ----------
        cid : str
            Container id or name.
        """
        _, container = validate_container(cid)
        if not container:
            abort(404)

        if request_json():
            return {'container': marshal(container, container_fields)}
        return Response(
                render_template('show_container.html',
                    item=marshal(container, container_fields)),
                mimetype='text/html')

    def post(self, cid):
        container, _ = validate_container(cid)
        if not container:
            abort(404)
        op = request.get_json().get('op')
        if op == "stop":
            if container.status == 'running':
                return self._stop(container)
        elif op == "pause":
            if container.status == 'running':
                return self._pause(container)
        elif op == "start":
            if container.status == 'exited':
                return self._start(container)
        elif op == "resume":
            if container.status == 'paused':
                return self._resume(container)
        
        #print(url_for('cid_admin', cid=cid, _scheme="https", _external=True))
        #return redirect(url_for('cid_admin', cid=cid))
        
    def _stop(self, c):
        print("{} has just been stopped.".format(c.id))
        c.stop()
        return {"status": "exited"}

    def _start(self, c):
        print("{} has just been started.".format(c.id))
        c.start()
        return {"status": "running"}

    def _resume(self, c):
        print("{} has just been resumed.".format(c.id))
        c.unpause()
        return {"status": "running"}

    def _pause(self, c):
        print("{} has just been paused.".format(c.id))
        c.pause()
        return {"status": "paused"}
