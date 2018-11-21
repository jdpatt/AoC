CURDIR = $(shell pwd)
challenge?=example

all: tox run

.PHONY: tox
tox:
	./venv/bin/python ./venv/bin/tox -c $(CURDIR) -- $(challenge)

.PHONY: run
run:
	./venv/bin/python ./venv/bin/tox -c $(CURDIR) -e run -- $(challenge)
