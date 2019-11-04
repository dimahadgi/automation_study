import psycopg2
from src.config_parser import Config

class Db_connect:
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

cursor = Db_connect.postgress_conn()
test = Db_connect.fetch_all("select email from worker;", cursor)

