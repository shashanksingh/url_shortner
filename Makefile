install:
	PIP_CONFIG_FILE=pip.conf pip install -r requirements.txt

install-dev:
	PIP_CONFIG_FILE=pip.conf pip install -r requirements-dev.txt

# ugly hack : https://github.com/QMSTR/pyqmstr/commit/0c6eb5b6e3d812607dd557e50ddf48b5f4ca379c
# Issue : https://github.com/grpc/grpc/issues/9575
proto:
	python -m grpc_tools.protoc --proto_path=src/proto/  --python_out=src/generated/ --grpc_python_out=src/generated/ url_shortner_service.proto
	2to3 src/generated -w -n

build:
	docker-compose -f docker-compose.dev.yml up

clean:
	docker-compose -f docker-compose.dev.yml down --remove-orphans
	docker volume rm url_shortner_db-volume

rebuild_db:
	docker-compose -f docker-compose.dev.yml  down
	docker volume rm url_shortner_db-volume
	docker-compose -f docker-compose.dev.yml  up

test:
	pytest -sv tests/

black:
	black --target-version py38 src/ tests/ clients/ main.py

fix:
	black -l 120 src/ tests/

run_server:
	python -m main

run_redirection_service:
	export FLASK_ENV=development && export FLASK_APP=clients/redirection_service.py && python -m flask run

run_client:
	python -m clients.examples.create_short_urls
	python -m clients.examples.get_short_url_details
	python -m clients.examples.get_all_short_urls

.PHONY: freeze clean
.SILENT: src_package