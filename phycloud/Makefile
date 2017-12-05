.PHONY: #env pack

FLASK_APP = $(shell pwd)/run.py

#env:
#	virtualenv env
#
SHELL := /bin/bash

ENV_PATH = $(HOME)/mnb-env

#PROXY_TOKEN = $(PROXY_TOKEN)

IPNOW := $(shell ip address show enx18dbf2615ea9 | \
		  /bin/grep "\<inet\>" | cut -c10-20)

PROXY_TOKEN = '6520fbd2223339e729c99b4f1730f1dd2098b57c3f3d692a37ba6fecc553'
PROXY_BASE = 'http://127.0.0.1:8001/api/routes'

env:
	virtualenv $(ENV_PATH)

proxy:
	docker run \
		-e CONFIGPROXY_AUTH_TOKEN=$(TOKEN) \
		--name=proxy \
		--net=host \
		-v $(shell pwd)/../ssl:/ssl \
		jupyter/configurable-http-proxy \
		--log-level debug \
		--ssl-key /ssl/key.pem \
		--ssl-cert /ssl/cert.pem \
		--ip $(IPNOW)\
		--port 8000 \
		--default-target http://127.0.0.1:5050

env_pkg:
	source $(ENV_PATH)/bin/activate && \
		pip install -r requirements.txt

run:
	source $(ENV_PATH)/bin/activate && \
		PROXY_TOKEN=$(PROXY_TOKEN) \
		PROXY_BASE=$(PROXY_BASE) \
		./run.py

server:
	uwsgi --socket 0.0.0.0:5005 \
		  --protocol http \
		  --manage-script-name \
		  --mount /=app:app

clean:
	find . -iname '*.pyc' -exec rm {} \;
	docker rm $(docker ps -q -f "status=created")

#1
init_db:
	# rm -rf app.db
	rm -rf migrations
	source $(ENV_PATH)/bin/activate && \
		export FLASK_APP=$(FLASK_APP) && \
		flask db init && \
		flask db migrate && \
		flask db upgrade && \
		./db-scripts/init_admin.py

#1.1
restore_db:
	./db-scripts/db_restore.py

#2
migrate_db:
	source $(ENV_PATH)/bin/activate && \
		export FLASK_APP=$(FLASK_APP) && \
		flask db migrate

#3
upgrade_db:
	source $(ENV_PATH)/bin/activate && \
		export FLASK_APP=$(FLASK_APP) && \
		flask db upgrade

init_user:
	source $(ENV_PATH)/bin/activate && \
		./db-scripts/init_admin.py
