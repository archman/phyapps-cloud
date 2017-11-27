.PHONY: deploy clean

#TOKEN=$(head -c 30 /dev/urandom | xxd -p)
TOKEN = 0b20cdf3c951d25936d27fc4405eb23e2e29790b00

deploy:
	docker stack deploy -c docker-compose.yml phyapps

clean:
	docker stack rm phyapps
	docker container stop $$(docker ps -aq)
	docker container rm $$(docker ps -aq)

proxy:
	docker run -e CONFIGPROXY_AUTH_TOKEN=$(TOKEN) \
		--name=proxy \
		--net=host \
		-v $(shell pwd)/ssl:/ssl \
		jupyter/configurable-http-proxy \
		--log-level debug \
		--ssl-key /ssl/key.pem \
		--ssl-cert /ssl/cert.pem \
		--ip 35.9.58.117 \
		--default-target http://127.0.0.1:5050

stop-proxy:
	docker container stop proxy
	docker container rm proxy

post-routes:
	curl -H "Authorization: token $(TOKEN)" \
		-d '{"target":"http://127.0.0.1:31002"}' \
		-X POST http://127.0.0.1:8001/api/routes/user1/

get-routes:
	curl -H "Authorization: token $(TOKEN)" \
		http://127.0.0.1:8001/api/routes

orch:
	export CONFIGPROXY_AUTH_TOKEN=$(TOKEN) && \
	python tmpnb/orchestrate.py \
		--pool-size=1 \
		--port=5001 \
		--use-tokens=True
