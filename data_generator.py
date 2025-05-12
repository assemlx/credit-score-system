# import random
# from datetime import date, timedelta
# from engines import Sessions
# from models.user_db import User
# from models.payments_db import Payment
# from models.debt_db import Debt
# from models.history_db import History
# from models.mix_db import CreditMix

# # Create and insert a user
# user_session = Sessions["user_db"]()
# user = User(name="Ali Amr", email="AliAmr@gmail.com")
# user_session.add(user)
# user_session.commit()
# user_id = user.id


# # Payment history
# pay_session = Sessions["payments_db"]()
# for _ in range(20):
#     pay_session.add(Payment(user_id=user_id, on_time=random.random() > 0.2))

# # Debt
# debt_session = Sessions["debt_db"]()
# debt = Debt(user_id=user_id, credit_limit=10000, amount_used=random.randint(1000, 9000))
# debt_session.add(debt)

# # History
# history_session = Sessions["history_db"]()
# start_date = date.today() - timedelta(days=random.randint(1, 10) * 365)
# history_session.add(History(user_id=user_id, start_date=start_date))


# # Credit Mix
# mix_session = Sessions["mix_db"]()
# mix = CreditMix(user_id=user_id, types_used=random.randint(1, 4), total_types=4)
# mix_session.add(mix)

# # Commit all
# pay_session.commit()
# debt_session.commit()
# history_session.commit()
# mix_session.commit()

# print("Sample data inserted for user_id:", user_id)
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