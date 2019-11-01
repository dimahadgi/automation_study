import psycopg2
from src.config_parser import Config

def postgress_conn():
    try:
        connection = psycopg2.connect(user=Config.user,
                                      password=Config.password,
                                      host=Config.host,
                                      port=Config.port,
                                      database=Config.database)
        cursor = connection.cursor()
        return cursor

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

def fetch_all(query, cursor):
    cursor.execute(query)
    record = cursor.fetchall()
    return record

if __name__ == "__main__":
    cursor = postgress_conn()
    test = fetch_all("select email from worker;", cursor)
    print(test)
