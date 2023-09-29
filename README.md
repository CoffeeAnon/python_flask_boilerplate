# python_flask_boilerplate

Run with:

```
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

#### Decisions around pyproject, tox, and poetry:

##### Requirements

- Install dev dependencies and test dependencies locally
- Install test dependencies from circleci
- NOT install test and dev dependencies in production

Tox can run tests locally and also runs tests in circleci

- Use extras to install test dependencies
- Use dev for anything needed for running locally but not needed for testing (e.g. debugpy)
- Install extras in tox, and in the local dev environment
- Exclude dev from docker compose

From Poetry docs re groups: "Installing (groups) is only possible by using Poetry."
