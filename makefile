run:
		python3 main.py

all: dependencies run

dependencies:
		pip3 install -r dependencies.txt