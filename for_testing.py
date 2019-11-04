from src.utils.db_postgress_helper import DbConnect


query = "select email from worker;"
test = DbConnect()
print(test.fetch_one(query))
