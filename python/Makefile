.PHONY: tox run clean
CURDIR = $(shell pwd)
challenge?=example

all: tox run

tox:
	./venv/bin/python ./venv/bin/tox -c $(CURDIR) -- $(challenge)

run:
	./venv/bin/python ./venv/bin/tox -c $(CURDIR) -e run -- $(challenge)

clean:
	rm -rf .tox .tmp .pytest_cache .mypy_cache __pycache__
