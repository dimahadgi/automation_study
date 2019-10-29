import psycopg2

query = "select email from worker;"

def postgress_conn(record):
    try:
        connection = psycopg2.connect(user="qcmaster",
                                      password="roo7IaquieTiem",
                                      host="worker-search-qc.cbqlnvvoalu1.eu-central-1.rds.amazonaws.com",
                                      port="5432",
                                      database="qc2_employer")
        cursor = connection.cursor()
        cursor.execute(record)
        record = cursor.fetchall()
        return record

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

if __name__ == "__main__":
    print(postgress_conn(query))

