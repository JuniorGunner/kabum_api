default: run

# Build Docker image
build:
	docker-compose build

# Run application using Docker
run-docker:
	docker-compose up

# Stop application
stop:
	docker-compose down


# Run Flask application directly (not using Docker)
run:
	python run.py

# Run unittests
test:
	python -m unittest discover -s tests

# Run unittests with detailed logging output
test-verbose:
	python -m unittest discover -s tests -v
