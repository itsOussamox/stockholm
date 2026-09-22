VENV    = .venv
PYTHON  = $(VENV)/bin/python3
PIP     = $(VENV)/bin/pip3
MAIN    = src/stockholm.py

.PHONY: run install help version

# Create the virtual environment and install dependencies
install:
	@python3 -m venv $(VENV)
	@$(PIP) install --quiet cryptography
	@echo "Dependencies installed inside $(VENV)."

# Run the program (silent — command itself won't be echoed)
run: $(VENV)
	@$(PYTHON) $(MAIN)

# Show the program's help
help: $(VENV)
	@$(PYTHON) $(MAIN) --help

# Show the program's version
version: $(VENV)
	@$(PYTHON) $(MAIN) --version

# Guard: remind the user to run make install if .venv is missing
$(VENV):
	@echo "[!] Virtual environment not found. Run 'make install' first."
	@exit 1