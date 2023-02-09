# Grasp Adventure

A simple adventure game demonstrating GRASP (and other) patterns

## Versions

### V1

- `World` and `Location` classes
- Worlds can be created from location descriptions
- No notion of connections between locations

### V2a

- Add connections between locations
- Connections are stored in `World` class according to Information Expert

### V2b

- Store connections in `Location` class to improve cohesion

### V2c

- Move creation of worlds to `WorldFactory`

### V3a

- Add `Pawn` class with `move()` method

### V3b

- Generalize `move()` method to `perform_action()` using `Action` enum

### V3c

- Change `Action` into an ABC according to Polymorphism/OCP pattern

### V4

- Move ABCs to `base_classes` module to reduce coupling
- Add `Game` class (Controller pattern)
- Add `Player` class
  - Uses Strategy pattern to choose action
  - Uses Template Method pattern to take a turn
- Rename `WorldFactory` to `GameFactory`
- Output methods are hardcoded in `Game`

### V5

- Adds `GameObject` class and `TreasureChest`, `Torch` subclasses
- Adds `InsepectAction` class
- TODO: Create objects in locations
- TODO: Introduce observer for player instead of hard-coded output

## Installation

To build the project use

```shell script
python -m build
```
in the root directory (i.e., the directory where `pyproject.toml` and
`setup.cfg` live).

After building the package you can install it with pip:
```shell script
pip install dist/grasp_adventure-0.0.1-py3-none-any.whl
```

To install the package so that it can be used for development purposes
install it with
```shell script
pip install -e .
```
in the root directory.

## Working with the project

The project is configured to run `pytest` tests and doctests. Source code for
tests is in the `tests` directory, outside the main package directory. Therefore,
you have to make sure that your python interpreter can resolve the imports for
the tests. The easiest way to ensure this is to install the package. You can run
the tests from the root directory as follows:

```shell script
$ pytest
```

*Note:* If you install the package from a wheel, the tests will run against the
installed package; install in editable mode (i.e., using the `-e` option) to
test against the development package.

To check that the package works correctly with different Python versions by executing

```shell script
$ tox
```

from the project's root directory. Currently, Python versions 3.8 to 3.11
are tested. Dependencies for `tox` are installed using `tox-conda`; remove the
corresponding entry in the `tox.ini` file if you want to use `virtualenv`
instead.
