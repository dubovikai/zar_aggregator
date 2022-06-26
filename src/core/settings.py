# coding: utf-8
from pydantic import BaseSettings


class Settings(BaseSettings):
    environment = 'local'
    is_debug = True

    project_title = 'ZarAgg'
    project_version = 0

    api_token = 'secret'

    db_string = "mysql+mysqlconnector://API:123@localhost/api"

    class Config:
        env_file = '.env'
