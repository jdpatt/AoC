CURDIR = $(shell pwd)
DOCKER=docker run -it -v $(CURDIR):/root:rw advent-cpp	
CXX=$(DOCKER) g++-7
FLAGS := -g -std=c++17 -Werror -Wall -Wextra -pedantic -MMD -Ishared/

TARGET?= example
BUILD_DIR := build
SRCS= $(wildcard **/*.cc)
OBJS= $(patsubst %.cc, $(BUILD_DIR)/%.o, $(notdir $(SRCS)))

all: run

run: $(TARGET)
	$(DOCKER) ./$(BUILD_DIR)/$<

$(TARGET): $(OBJS)
	@echo Linking $@...
	$(CXX) -o $(BUILD_DIR)/$@ $(TARGET).cc $(OBJS) $(FLAGS)
	chmod a+x $(BUILD_DIR)/$@

$(BUILD_DIR)/%.o: $(SRCS)
	@echo Compiling $<...
	$(CXX) $(FLAGS) -c -o $@ $<

lint:
	@echo Linting...
	$(DOCKER) cppcheck --std=c++11 $(TARGET).cc $(SRCS) --enable=all -q -Ishared/ --error-exitcode=1
	$(DOCKER) clang-tidy $(TARGET).cc $(SRCS) --checks="*" --warnings-as-errors="*" -- -Ishared/ -std=c++1z

docker:
	docker build -t advent-cpp .

shell:
	$(DOCKER) /bin/bash

clean:
	rm -rf $(BUILD_DIR)/*

.PHONY: lint docker shell clean