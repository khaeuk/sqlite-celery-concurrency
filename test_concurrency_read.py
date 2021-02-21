from celery import group
from tasks import retrieve_data_by_species


def create_connection(db):
    conn = None

    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e :
        print(e)

    return conn

def main():
    species_type = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

    # Perform single task
    c = retrieve_data_by_species(species_type[0])
    print("Single task example result :")
    print(c)

    # Perform concurrent tasks
    result = group(retrieve_data_by_species.s(spec) for spec in species_type)().get()
    print("Multiple parallel tasks example result :")
    print(result)
    
    
if __name__ == "__main__":
    main()