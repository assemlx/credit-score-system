import random
from datetime import datetime, timedelta
from database_setup import connect_to_db

def insert_sample_data():
    user_conn = connect_to_db('user_db')
    cursor = user_conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ('Abdallah Gaber', 'Abdallah@gmail.com'))
    user_conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    user_conn.close()

    payments_conn = connect_to_db('payments_db')
    cursor = payments_conn.cursor()
    for _ in range(20):
        on_time = random.choice([1, 0])
        cursor.execute("INSERT INTO payment (user_id, on_time) VALUES (%s, %s)", (user_id, on_time))
    payments_conn.commit()
    cursor.close()
    payments_conn.close()

    debt_conn = connect_to_db('debt_db')
    cursor = debt_conn.cursor()
    credit_limit = 10000
    amount_used = random.randint(1000, 5000)
    cursor.execute("INSERT INTO debt (user_id, credit_limit, amount_used) VALUES (%s, %s, %s)", (user_id, credit_limit, amount_used))
    debt_conn.commit()
    cursor.close()
    debt_conn.close()

    history_conn = connect_to_db('history_db')
    cursor = history_conn.cursor()
    start_date = datetime.now() - timedelta(days=365 * random.randint(1, 10))
    cursor.execute("INSERT INTO history (user_id, start_date) VALUES (%s, %s)", (user_id, start_date.date()))
    history_conn.commit()
    cursor.close()
    history_conn.close()

    mix_conn = connect_to_db('mix_db')
    cursor = mix_conn.cursor()
    types_used = random.randint(1, 4)
    total_types = 4
    cursor.execute("INSERT INTO credit_mix (user_id, types_used, total_types) VALUES (%s, %s, %s)", (user_id, types_used, total_types))
    mix_conn.commit()
    cursor.close()
    mix_conn.close()

    print("Sample data inserted for user_id:", user_id)


insert_sample_data()