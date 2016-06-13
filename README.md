# cartodb-sql-cli

CLI application to interact with CartoDB SQL API

## Installation

Create a [virtual environment]():

```bash
virtualenv -p python3 env
```

And once activated install the requirement libraries with these two commands:

```bash
$ pip install -e git+git://github.com/CartoDB/cartodb-python.git#egg=cartodb
$ pip install -r requirements.text
```

## Usage

Run `python cartodb-cli.py` to see the options and arguments, they should
be quite straight forward. You can set these environment variables so you don't need to put your credentials from the command line:

* `CARTODB_USER_NAME`
* `CARTODB_API_KEY`

