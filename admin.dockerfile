FROM python:3-alpine

# Create app directory
WORKDIR /app

# Bundle app source
COPY ./app /app

RUN pip install -U pip
RUN pip install setuptools==58
RUN pip install -r /app/requirements/production_freeze.txt

ENV FLASK_APP=app/admin/start_admin.py

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]