.PHONY: clean-pyc run-test run-flake8 help

TOP_DIR=.
SCRIPT_DIR=.
TESTS_DIR=tests

help:
	@echo "make clean-pyc"
	@echo "    Remove python artifacts."
	@echo ""
	@echo "make run-test"
	@echo "    Run all test scripts."
	@echo ""
	@echo "make run-flake8"
	@echo "    Run flake8 on substitute.py."
	@echo ""
	@echo "make test-input"
	@echo "    Run substitute.py with input data"

clean-pyc:
	@find $(TOP_DIR) -name '*.pyc' -exec rm -rvf {} +
	@find $(TOP_DIR) -name '*.pyo' -exec rm -rvf {} +
	@find $(TOP_DIR) -name '__pycache*' -exec rm -rvf {} +
	@find $(TESTS_DIR)/ -name '__pycache*' -exec rm -rvf {} +

run-test: clean-pyc
	PYTHONPATH=$(TOP_DIR):$(PYTHONPATH) python3 -m unittest $(TESTS_DIR)/test_*

run-flake8: clean-pyc
	sh $(SCRIPT_DIR)/run_flake8.sh

test-input: clean-pyc
	rm -rvf ./testdata/output.json
	python3 substitute/substitute.py ./testdata/input.json 3 ./testdata/output.json