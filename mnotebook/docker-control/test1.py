#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docker


ports = [8888, 4810]
port_bindings = {8888:8887, 4810:4811}

volumes = ['/phyapps']
volume_bindings = {
    '/home/tong/Dropbox/FRIB/work/phyapps-docker/tests': {
        'bind': '/phyapps',
        'mode': 'rw',
    },
}

image_name = 'tonyzhang/phyapps:release-1.5-ss'

client = docker.APIClient(base_url='unix://var/run/docker.sock')
host_config = client.create_host_config(
    binds=volume_bindings, port_bindings=port_bindings,
)
container = client.create_container(
    image=image_name,
    ports=ports,
    volumes=volumes,
    host_config=host_config,
    stdin_open=True,
    tty=True,
#    network_mode='host',
)

client.start(container)
