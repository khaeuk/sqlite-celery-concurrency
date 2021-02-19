import sqlite3


def create_connection(db):
    conn = None

    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e :
        print(e)

    return conn

def main():
    DATABASE = "iris-data.sqlite"
    
    conn = create_connection(DATABASE)

    c = conn.cursor()

    c.execute('''SELECT * FROM Iris''')

    print(c.fetchmany(5))

if __name__ == "__main__":
    main()