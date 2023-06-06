# substitute function/script

## Problem statement:

- Please refer: https://docs.google.com/document/d/1-yGXfDcEeOYhQwtyW9Avoqh_ko7lptp0s2wBLpFfhyE/

## Setup

- Since the script/function is implemented using native python modules, no setup/installation is
  required
- Though recommend to use virtualenv for the project to keep future modules localized to the project for ease of debugging
- To spinup virtual env, please run the following command:

```
  $ python3 -m venv venv
  $ source venv/bin/activate
```

## substiute script usage

- Please run following to check command line arguments necessary

```
$ python3 substitute/substitute.py -h
```

- For e.g. running with test input data

```
$ python3 substitute/substitute.py ./testdata/input.json 3 ./testdata/output.json
```

## Unittests

- The "tests" directory contains simple unittests implemented to test error and success
  cases.

## Makefile usage

(Make sure you have Python 3.11.3 or higher)

- Execute the following command to see all makefile options

```
$ make help
```

## How to test against the input data

- Run the following commands:

```
  $ make test-input
```

- The above command will run substitute.py and
  test with the `input.json` in `testdata` directory
- The output file `output.json` is saved in the `testdata` directory too

## How to run unittests

- Run the following commands:

```
  $ make run-test
```

## Flake8 conventions

- The main file(substitute.py) follow flake8's conventions
- It can be checked using the following command:

```
  $ make run-flake8
```

- Please make sure flake8 is installed by running the following command:

```
  $ pip3 install flake8
```

## Release instructions

- We will use poetry python module to manage dependencies (no dependencies for now) and build/distribution of our package, due to it's ease of use and rich features
- Please install potery for the relevant system by referring the official link: https://python-poetry.org/docs/#installing-with-the-official-installer

- To install dependencies in future, please use the following command:

```
$ poetry add some_dependency
```

- To build python package:

```
$ poetry build
```

Built packages are available under `dist` directory

- Publish python package:

```
$ poetry publish
```
