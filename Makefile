PYTHON = python3
VENV_DIR = venv
VENV_BIN = $(VENV_DIR)/bin
PY = $(VENV_BIN)/python
PIP = $(VENV_BIN)/pip
FLAGS = --warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs
MYPY = mypy
MAP = maps/easy/easy_map.txt
FLAKE8 = flake8 . --exclude venv
CLEAN_FILES = .mypy_cache __pycache__ *.pyc *.pyo

run:
	$(PY) main.py $(MAP)

install:
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

debug:
	$(PY) -m pdb main.py $(MAP)

clean:
	rm -rf $(CLEAN_FILES)

lint:
	$(FLAKE8) && $(MYPY) $(FLAGS) --exclude venv .

lint-strict:
	$(FLAKE8) && $(MYPY) . --strict
