# zar_aggregator

*this will apply previous migrations*
cd app
PYTHONPATH=. alembic upgrade head

*this will generate new migration (Python venv must be active)*
PYTHONPATH=. alembic revision --autogenerate -m "Added account table"

