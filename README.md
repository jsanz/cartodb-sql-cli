# cartodb-sql-cli

Command line interface to interact with CartoDB SQL API. This is basically a
command line interface that wraps the [CartoDB python SDK] for your convenience.

## Installation

It's advised to create a [virtual environment]. Note that this code is only
tested with Python 3, it will probably work with version 2, though.

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


[CartoDB python SDK]: https://github.com/CartoDB/cartodb-python
[virtual environment]: https://docs.python.org/3/library/venv.html#module-venv