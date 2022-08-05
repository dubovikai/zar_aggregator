FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

RUN pip install -U pip
RUN pip install -U setuptools

COPY ./app /app

RUN pip install -r /app/requirements/production_freeze.txt

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then pip install -r requirements/develop.txt ; fi"

ENV PYTHONPATH=/app
