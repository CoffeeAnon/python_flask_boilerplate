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
export FLASK_APP=my_app.app
poetry run flask db check -d my_app/migrations_prod
```
