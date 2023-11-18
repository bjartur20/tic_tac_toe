# Tic Tac Toe

This tic tac toe game is a simple Player vs Player game written using Python.

The project is a coding assignment given by Lucinity for an application for the Associate Software Engineer position.

## Prerequisites

These instructions assume MacOS or Linux operating systems
Python >= 3.10
Pip package manager

## Installation

Create and activate a virtual environment

```zsh
python -m venv venv
source venv/bin/activate
```

Install requirements

```zsh
pip install -r requirements.txt
```

## Running The Game

```zsh
python main.py
```

## Running Tests

```zsh
python -m pytest tests
```

## Run in docker container

Build the docker image

```zsh
docker build . -t tic-tac-toe
```

Run the container in interactive mode with a pseudo terminal

```zsh
docker run -it tic-tac-toe
```
