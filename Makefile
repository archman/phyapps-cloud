#
# Makefile for the deployment of phyapps cloud computing platform.
#
# Author: Tong Zhang <zhangt@frib.msu.edu>
#
# Usage:
# commands in the Terminal (after $)
# 1. Start deployment
# $ SRV_IP=10.20.30.40 make deploy
# 2. Stop deployment
# $ make stop
# 3. Clean all data, including database
# $ make purge
#

# stach name
STACK_NAME ?= phyapps_cloud

# The IP address of workstation as the service provider.
SRV_IP ?= 192.168.1.1

# secret string for authentication
TOKEN ?= $(shell head -c 30 /dev/urandom | xxd -p)

# MySQL configuration
# root password
MYSQL_ROOT_PASSWORD ?= 9db75011
# database name for phyapps-gateway
DATABASE_NAME ?= phyapps_cloud
# database user account name
DATABASE_USER ?= phyapps_admin
# DATABASE_USER's password
DATABASE_PASS ?= ebf39f78

deploy:
	@printf "TOKEN used: %s\n" $(TOKEN)
	@MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
	DATABASE_NAME=${DATABASE_NAME} \
	DATABASE_USER=${DATABASE_USER} \
	DATABASE_PASS=${DATABASE_PASS} \
	TOKEN=${TOKEN} \
	docker stack deploy -c compose.yml ${STACK_NAME}
	@printf "Platform address: %s\n" https://${SRV_IP}:8000
	@printf "Database configuration:\n"
	@printf "> root password: %s\n" ${MYSQL_ROOT_PASSWORD}
	@printf "> database name: %s\n" ${DATABASE_NAME}
	@printf "> database user name: %s\n" ${DATABASE_USER}
	@printf "> database user pass: %s\n" ${DATABASE_PASS}

stop:
	@docker stack rm ${STACK_NAME}

purge:
	@docker volume rm ${STACK_NAME}_db-data ${STACK_NAME}_portainer-data

update-images:
	@docker pull tonyzhang/phyapps-gateway:latest
	@docker pull tonyzhang/phyapps:nb
	@docker pull tonyzhang/phyapps:va

.PHONY: deploy stop purge
