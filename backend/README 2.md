# evecontrol-api

## Running the App

We are using Python 3.9.10 If using [docker](https://www.docker.com/), you can build and run your image of mysql 5.7 using:

```bash
docker-compose up -d
```

You'll need [Python 3.8](https://www.python.org/downloads/), [virtualenv](https://virtualenv.pypa.io/en/latest) and mysql-client lib install in your system. After installing, create the .env file with the settings at the root of the project (look at the env_sample file) and run:

example macos:
```bash
brew install mysql-client
```

```bash
source <your-path-to-venv>/bin/activate
pip install -U pip
pip install pip-tools
make requirements-dev-install
make run
```

## If you need upgrade the requirements dev-packages

```bash
source <your-path-to-venv>/bin/activate
make requirements-update
make requirements-dev-install
```

## If you need upgrade the requirements packages

```bash
source <your-path-to-venv>/bin/activate
make requirements-update
```

## Testing this app

We are using [pytest](https://docs.pytest.org/en/latest/).

```bash
source <your-path-to-venv>/bin/activate
make test
```

## Running the linter

```bash
source <your-path-to-venv>/bin/activate
make lint
```

## How to Contribute

[CONTRIBUTING](CONTRIBUTING.md).

