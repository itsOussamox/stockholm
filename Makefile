VENV       = .venv
PYTHON     = $(VENV)/bin/python3
PIP        = $(VENV)/bin/pip3
MAIN       = src/stockholm.py
PY_VERSION = $(shell python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")

.PHONY: run install clean help version

# Install system venv package, create the virtual environment, install dependencies
install:
	@if [ -d "$(VENV)" ]; then \
		echo "[!] Virtual environment already exists. Run 'make clean' to reset it."; \
	else \
		echo "[*] Installing python$(PY_VERSION)-venv..."; \
		sudo apt install -y python$(PY_VERSION)-venv; \
		echo "[*] Creating virtual environment..."; \
		python3 -m venv $(VENV); \
		echo "[*] Installing dependencies..."; \
		$(PIP) install --quiet cryptography; \
		echo "[+] Done. Run 'make run' to start."; \
	fi

# Remove the virtual environment
clean:
	@rm -rf $(VENV)
	@echo "[-] Virtual environment removed."

# Run the program — pass extra arguments with ARGS=
# Examples:
#   make run
#   make run ARGS="-s"
#   make run ARGS="-r YOUR_KEY_HERE"
ARGS ?=
run: $(VENV)
	@$(PYTHON) $(MAIN) $(ARGS)

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