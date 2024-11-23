EXAMPLES_DIR = ./examples
PYTHON = python
SERVICE_NAME = logger_service.py
SHELL := /bin/bash
REQ_FILE = ./requirements.txt


requirements:
	pip install -r $(REQ_FILE)

# must be run first
service:
	$(PYTHON) $(EXAMPLES_DIR)/service/$(SERVICE_NAME)
signal-client:
	$(PYTHON) $(EXAMPLES_DIR)/signal_client/signal_example.py
client:
	$(PYTHON) $(EXAMPLES_DIR)/logger_client/client.py
