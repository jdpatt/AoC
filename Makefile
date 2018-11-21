.PHONY: python cpp

all: python cpp

python:
	$(MAKE) -C python

cpp:
	$(MAKE) -C cpp