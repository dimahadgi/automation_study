import psycopg2
from src.config_parser import Config


class DbConnect:
    def __init__(self):
        self.user = Config.db_user
        self.password = Config.db_password
        self.host = Config.db_host
        self.port = Config.db_port
        self.database = Config.db_database
        self.cursor = self.postgress_conn()

    def postgress_conn(self):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)
            cursor = connection.cursor()
            return cursor

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def fetch_all(self, sql_query):
        self.cursor.execute(sql_query)
        record = self.cursor.fetchall()
        return record

    def fetch_one(self, sql_query):
        self.cursor.execute(sql_query)
        record = self.cursor.fetchone()
        return record

    def write_to_db(self, sql_query):
        self.cursor.execute(sql_query)
        self.cursor.connection.commit()
