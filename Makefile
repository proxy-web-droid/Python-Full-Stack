VENV=.venv
PIP=$(VENV)/bin/pip
PY=$(VENV)/bin/python

.PHONY: venv install run clean

venv:
	python -m venv $(VENV)

install: venv
	$(PIP) install -r requirements.txt

run: install
	$(PY) "app. py"

clean:
	rm -rf $(VENV) __pycache__ *.pyc
