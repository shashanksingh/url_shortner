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
	make proto
	docker-compose -f docker-compose.dev.yml up

clean_build:
	docker-compose -f docker-compose.dev.yml down --remove-orphans

test:
	pytest -sv tests/

black:
	black --target-version py38 src/ tests/ clients/ main.py

fix:
	black -l 120 src/ tests/

clean:
	rm -rf dist/ build/  || true

run_server:
	python -m main

run_client:
	python -m clients.examples.create_short_urls
	python -m clients.examples.get_short_url_details
	python -m clients.examples.get_all_short_urls

.PHONY: freeze clean
.SILENT: src_package