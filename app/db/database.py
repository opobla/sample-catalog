import psycopg2
from flask import g


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            user="dbuser",
            password="secreto",
            host="host.docker.internal",
            port="5432",
            database="db"
        )
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
