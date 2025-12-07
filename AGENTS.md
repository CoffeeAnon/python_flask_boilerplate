# AGENTS.md

## Build/Test Commands
- **Install deps**: `poetry install`
- **Run all tests**: `pytest my_app/tests/`
- **Run single test**: `pytest my_app/tests/test_routes.py::test_hello_world -v`
- **Lint**: `tox -e lint` or `pylint -v -j 0 --rcfile=pylintrc my_app`
- **Type check**: `tox -e mypy` or `mypy --config-file mypy.ini my_app/`
- **All checks**: `tox` (runs lint, mypy, py39)

## Code Style
- **Python version**: 3.9
- **Formatter**: Black (via isort profile=black)
- **Max line length**: 100 characters
- **Naming**: snake_case (functions, variables, methods), PascalCase (classes), UPPER_CASE (constants)
- **Imports**: Sorted with isort (black profile). Standard library → third-party → local
- **Types**: Use type hints. Mypy strict mode. Add type stubs for untyped packages
- **Docstrings**: Not required for modules/functions (disabled: C0114, C0116)
- **Error handling**: Avoid catching base Exception. Use specific exception types

## Key Files
- Config: `pyproject.toml`, `tox.ini`, `pylintrc`, `mypy.ini`
- Tests: `my_app/tests/` (pytest with fixtures in `conftest.py`)
- App entry: `my_app/app.py`, Flask app in `my_app/flask_app/`
