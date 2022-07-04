# Makefile for python executing

### Python Package Management ###
REQUIREMENTS = requirements.txt

### Project Information ###
PROJECT_NAME = This Project
PROJECT_VERS = v[Major].[Minor].[Patches]-[Release]

### Project Structure ###
BUILD_DIR = build/exe/
SRC_DIR = src/

### Development Environment ###
CC = pyinstaller --onefile
VENV = env
SRC = src/main.py
DST = build/exe/project-name.exe

setup: $(REQUIREMENTS)
	## Setup python environment
	# Create virtual environment
	@test -d $(VENV) || python -m venv $(VENV)
	
	# Create project folders
	@test -d $(BUILD_DIR) || mkdir -p $(BUILD_DIR)
	@test -d $(SRC_DIR) || mkdir -p $(SRC_DIR)

	## Install packages into python virtual environment	
	. $(VENV)/bin/activate; pip install -Ur $(REQUIREMENTS)
	
start: setup 
	## Start python script
	# Activate Virtual Environment
	. $(VENV)/bin/activate; python $(SRC)

build: setup
	## Build and make/compile python application
	$(CC) $(SRC) --out $(DST)

install: setup
	## Install and place the files at the appropriate locations	

backup: setup  
	## Backup python requirements into requirements.txt
	# Activate Virtual Environment
	. $(VENV)/bin/activate; pip freeze > $(REQUIREMENTS)

clean: ## Clean up temporary files
	rm -rf $(VENV)
