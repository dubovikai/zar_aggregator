# zar_aggregator

*init environment variables for using scripts, can be added to venv/bin/activate script*
export $(grep -v '^#' .env | xargs)
export PYTHONPATH=.

*working folder*
cd app

*init db for first launch*
source prestart.sh

*init environment variables for using scripts*
alembic upgrade head

*this will generate new migration (Python venv must be active)*
alembic revision --autogenerate -m "Added account table"

