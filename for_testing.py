from src.utils.db_postgress_helper import Db_connect


cursor = Db_connect.postgress_conn()
test = Db_connect.fetch_all("select email from worker;", cursor)
print(test)