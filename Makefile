# Variables
PYTHON := python
LINT_FILES := .

# Targets
.PHONY: help format lint test all

help:  ## Show help
	@echo "Usage: make <TARGET>"
	@echo ""
	@echo "Targets:"
	@echo "  format    - Run code formatters (black, isort)"
	@echo "  lint      - Run linters (flake8)"
	@echo "  test      - Run tests (pytest)"
	@echo "  all       - Run formatters, linters, and tests"

format:  ## Run code formatters (black, isort)
	@echo "Running black..."
	black $(LINT_FILES)
	@echo "Running isort..."
	isort $(LINT_FILES)

lint:  ## Run linters (flake8)
	@echo "Running flake8..."
	flake8 $(LINT_FILES)

test:  ## Run tests (pytest)
	@echo "Running tests..."
	pytest

all: format lint test  ## Run all checks: format, lint, and test

setup:  ## Initial setup
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt