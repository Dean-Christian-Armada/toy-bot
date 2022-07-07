# Toy Bot Exam by Iress

## Step by Step Procedure for Running
1. Ensure that python3 is available in your computer.
2. Run the Console Application with `$ cd toy-bot && python3 main.py`
3. Follow and Enter the inputs being asked

## Step by Step Procedure for Running with Docker
1. Assuming that Docker is installed in your computer. Please follow bullets below for containerization setup.
    - `$ cd toy-bot`
    - `$ docker run -it -v=$(pwd):/usr/src/app --workdir=/usr/src/app --name=toy-bot python:3.10.1 bash`
    - `$ python main.py`
2. Run the Console Application with `python main.py`
3. Follow and Enter the inputs being asked

## Step by Step Procedure for Executing Unit Testing Script
1. Current directory should be the same directory where `main.py` is located
2. Run `$ python tests.py`**(if not containerized)** or `$ python3 tests.py`**(if containerized)**
