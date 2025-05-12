import mysql.connector
from config import DB_CONFIG


db_names = ['user_db', 'payments_db', 'debt_db', 'history_db', 'mix_db']

def connect_to_db(db_name):
    return mysql.connector.connect(database=db_name, **DB_CONFIG)


