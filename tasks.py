import sqlite3
from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

def create_connection(db):
    conn = None

    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e :
        print(e)

    return conn

@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def retrieve_data_by_species(species):
    DATABASE = "iris-data.sqlite"

    conn = create_connection(DATABASE)

    c = conn.cursor()

    # print(type(cur.execute("SELECT * FROM Iris WHERE Species is ?", (species,))))
    result = c.execute("SELECT * FROM Iris WHERE Species is ?", (species,))
    
    return result.fetchmany(5)

