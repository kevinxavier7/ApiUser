from sqlalchemy import URL
from os import environ

db_url = URL.create(
    "mysql",
    username=environ.get('DB_USERNAME'),
    password=environ.get('DB_PASSWORD'),
    host=environ.get('DB_HOST'),
    #port=environ.get('DB_PORT'),
    database=environ.get('DB_NAME')
    
)