.PHONY: deploy stop proxy mnb routes

#
# !! Change this every time before deployment !!
# e.g.: TOKEN=$(head -c 30 /dev/urandom | xxd -p)
# if needs to get routes later, use static string for TOKEN.
#
#TOKEN := $(shell head -c 30 /dev/urandom | xxd -p)
TOKEN ?= 6520fbd2223339e729c99b4f1730f1dd2098b57c3f3d692a37ba6fecc553
ETH0  ?= wlp58s0 #enx9cebe85fe8aa
IPNOW := $(shell ip address show $(ETH0) | \
		  /bin/grep "\<inet\>" | \
		  awk '{print $$2}' | \
		  awk -F'/' '{print $$1}')

IMAGE_GW := "tonyzhang/phyapps-gateway:latest"
IMAGE_PROXY := "jupyterhub/configurable-http-proxy"
DPATH := $(shell pwd)

deploy: proxy gateway
stop: stop-proxy stop-gateway

IP:
	echo $(IPNOW)

proxy:
	@docker run -d \
		-e CONFIGPROXY_AUTH_TOKEN=$(TOKEN) \
		--name=proxy \
		--net=host \
		-v $(shell pwd)/ssl:/ssl \
		$(IMAGE_PROXY) \
		--log-level debug \
		--ssl-key /ssl/key.pem \
		--ssl-cert /ssl/cert.pem \
		--ip $(IPNOW) \
		--port 8000 \
		--default-target http://127.0.0.1:5050

gateway:
	@docker run -t -d \
		-e PROXY_TOKEN=$(TOKEN) \
		-e PROXY_BASE="http://127.0.0.1:8001/api/routes" \
		-e DPATH=$(DPATH) \
		-p 5050:5050 \
		--name=gateway \
		--net=host \
		-v /var/run/docker.sock:/var/run/docker.sock \
		$(IMAGE_GW)

stop-proxy:
	@docker container stop proxy
	@docker container rm proxy

stop-gateway:
	@docker container stop gateway
	@docker container rm gateway

routes:
	curl -H "Authorization: token $(TOKEN)" -X GET \
		http://127.0.0.1:8001/api/routes

update:
	docker pull tonyzhang/phyapps-gateway
	docker pull tonyzhang/notebook
