# Crypto wallet
This project it's a dummy example in how to create a python API using: Docker, Python and Postgres. To run this project properly you will need to download poetry 1.5 or above and also docker to a proper and isolated deploy with all the package that you will need to install.

## thing you will need to install

[docker](https://docs.docker.com/engine/install/ubuntu)

[poetry](https://python-poetry.org/docs)

## thing you will need to install


``` bash
poetry config --list

cache-dir = "/home/user/.cache/pypoetry"
experimental.system-git-client = false
installer.max-workers = null
installer.modern-installation = true
installer.no-binary = null
installer.parallel = true
virtualenvs.create = true
virtualenvs.in-project = true
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}/virtualenvs"
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"
```
Check that in-project option is active if not, activate it using this line
``` bash
poetry config virtualenvs.in-project true
```

``` bash
cd python/crypto-wallet
poetry shell
poetry install --no-root
```
this will create a .env folder inside the project

## last update
Upload crypto-wallet