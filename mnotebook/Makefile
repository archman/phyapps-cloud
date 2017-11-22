.PHONY: #env pack

FLASK_APP = $(shell pwd)/run.py

#env:
#	virtualenv env
#
SHELL := /bin/bash

ENV_PATH = $(HOME)/mnb-env

#PROXY_TOKEN = $(PROXY_TOKEN)

PROXY_TOKEN = '0b20cdf3c951d25936d27fc4405eb23e2e29790b00'
PROXY_BASE = 'http://127.0.0.1:8001/api/routes'

env:
	virtualenv $(ENV_PATH)

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
	source $(ENV_PATH)/bin/activate && \
		export FLASK_APP=$(FLASK_APP) && \
		rm -rf app.db migrations && \
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
