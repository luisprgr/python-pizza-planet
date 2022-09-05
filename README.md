<h1 align="center"> Python Pizza Planet </h1>

![python-badge](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

This is an example software for a pizzeria that takes customizable orders.

## Table of Contents

- [Getting started](#getting-started)
- [Running the backend project](#running-the-backend-project)
- [Running the frontend](#running-the-frontend)
- [Testing the backend](#testing-the-backend)

## Getting started

You will need the following general tools:

- A Python interpreter installed. [3.9.13](https://www.python.org/downloads/release/python-3913/) is preffered.

- A text editor: preferably [Visual Studio Code](https://code.visualstudio.com/download)

- Extensions such as [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

## Running the backend project

- Clone the repo

```bash
git clone https://github.com/luisprgr/python-pizza-planet.git
```

- Create a virtual environment in the root folder of the project

```bash
make create-venv
```

- Activate the virtual environment (In vscode if you select the virtual env for your project it will activate once you open a new console window)

_For linux/MacOS users:_

```bash
source venv/bin/activate 
```

_For windows users:_

```cmd
\path\to\env\Scripts\activate
```

- Install all necessary dependencies:

```bash
make install-requirements
```


- Start the database (Only needed for the first run):

```bash
make start-database
```

- Seed the database (Only needed for the first run):

```bash
make seed-database
```

- Run the project with:

```bash
make start-server
```

- Run the project with hot reload:

```bash
make start-hot-reload
```

## Running the frontend

- Clone git UI submodule

```bash
git submodule update --init
```

- Install Live Server extension if you don't have it from [here](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) on VSCode Quick Open (`Ctrl + P`)

```bash
ext install ritwickdey.LiveServer
```

- To run the frontend, start `ui/index.html` file with Live Server (Right click `Open with Live Server`)

- **Important Note** You have to open vscode in the root folder of the project.

- **To avoid CORS errors** start the backend before the frontend, some browsers have CORS issues otherwise

### Testing the backend

- Run the test command

```bash
make run-tests
```

- Run the test command with coverage report

```bash
make test-coverage-report
```

### Check backend for linting errors

- Run the linters command

```bash
make run-linters
```

- if you want to reformat the code using black run:
    
```bash
make format-code
```

### Other commands

- In case that you need to delete the database:

```bash
make delete-database
``` 

### Deploy in local:

- you will need to have:
    - python 3.9.13 installed
    - your aws credentials configured
    - docker installed with rootless mode

- install sam cli:

```bash
pip install aws-sam-cli
```

- build the lambda function:

```bash
sam build
```

- (to test the lambda function locally) run the lambda function:

```bash
sam local start-api
```

- deploy the lambda function:

```bash
sam deploy --guided
```
