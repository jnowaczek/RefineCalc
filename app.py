import bz2
import sqlite3
import requests
import tempfile

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return load_data()

def load_data():
    try:
        url = r'https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2'
        app.logger.info('Fetching SDE from Fuzzwork')
        r = requests.get(url)

        db = bz2.decompress(r.content)

        with open(r'sde-latest.sqlite', mode='w+b') as sde, open('ores.sql') as sql:
            sde.write(db)

            with sqlite3.connect(r'sde-latest.sqlite') as conn:
                c = conn.cursor()
                query = sql.read()
                c.execute(query)
                return str(c.fetchall())
    except:
        raise


if __name__ == '__main__':
    app.run()
