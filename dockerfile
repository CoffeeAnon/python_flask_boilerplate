###########################################
# base
###########################################
ARG BASE_IMAGE=python:3.9.17-slim-buster
FROM "${BASE_IMAGE}" as base

ENV PYTHONUNBUFFERED=True
ENV PIP_NO_CACHE_DIR=True

# Install the python package managers.
RUN pip install -U \
    pip \
    setuptools \
    wheel \
    poetry

# Set this folder at the system root and then cd into it.
ENV HOME=/usr/src/app
RUN mkdir -p $HOME
WORKDIR $HOME

ENV POETRY_VIRTUALENVS_IN_PROJECT=True

# Copy poetry's package list
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --without=dev

# Override the CMD because we don't really need to run anything here
CMD ["python3"]

###########################################
# dev
###########################################
FROM base as dev

WORKDIR /usr/src/app

COPY my_app ./my_app
# Install everything including dev dependencies because this is dev
RUN poetry install --extras=type_tests

ENV FLASK_APP=my_app.app
ENV FLASK_ENV=development


EXPOSE 5000
CMD poetry run flask run


###########################################
# build
###########################################
FROM base as build

WORKDIR /usr/src/app

# Copy the contents of the project root directory to the app directory in the container
COPY . .

RUN poetry build --format wheel | grep "Built" | sed 's/^.*\s\(.*\.whl\)/\1/' > package_name

# Override the CMD because we don't really need to run anything here
CMD ["python3"]

###########################################
# production
###########################################

FROM base

# ==> Add user code layer
ENV HOME=/usr/src/app
RUN mkdir -p $HOME
WORKDIR $HOME

# Copy our python package (wheel file, output of `poetry build`) and install it
COPY --from=build /usr/src/app/dist repo_package
COPY --from=build /usr/src/app/package_name package_name
RUN pip install --no-cache-dir repo_package/$(cat package_name)

# docker-compose will override the CMD
CMD ["python3"]

