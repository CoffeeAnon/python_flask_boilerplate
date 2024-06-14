# Readme

Run with:

```zsh
export FLASK_APP=my_app.app
poetry run flask run
```

Verify flask db script (dev):

```bash
export FLASK_APP=my_app.app
poetry run flask db check -d my_app/migrations_dev
```

Change the .env file value of FLASK_ENV to dev to verify flask db script (prod):

```bash
unset FLASK_ENV
export FLASK_APP=my_app.app
poetry run flask db check -d my_app/migrations_prod
```

## Environment management

This project uses tox and poetry, and if a dev machine is also using pyenv, the number of environments to manage gets pretty high.

You can use pyenv to manage the global python version, but this project works well with poetry set up to create project-specific environments.

### Dependencies

1. For local dev, install dev dependencies and test dependencies in the poetry environment. The test dependencies are useful for non-tox test running, like vscode runners.
2. For CI, install test dependencies.
3. For production, only install production dependencies

<!-- markdownlint-disable MD007 -->
<!-- prettier-ignore -->
!!! warning
    Do NOT install test and dev dependencies in production

<!-- markdownlint-enable MD007 -->

Tox can run tests locally and also runs tests in circleci

- Use extras to install test dependencies
- Use dev for anything needed for running locally but not needed for testing (e.g. debugpy)
- Install extras in tox, and in the local dev environment
- Exclude dev from docker compose

From Poetry docs re groups: "Installing (groups) is only possible by using Poetry."

To run tox 4:

```zsh
tox p -e ALL -c tox.ini --verbose
```

or

```zsh
tox r -e mypy -c tox.ini --verbose
```

### mkdocs

Deploy mkdocs with `poetry run mike deploy --push --update-aliases 0.1 latest`
Set default for mkdocs to `latest` with `poetry run mike set-default latest`