import random
from datetime import date, timedelta
from engines import Sessions
from models.user_db import User
from models.payments_db import Payment
from models.debt_db import Debt
from models.history_db import History
from models.mix_db import CreditMix

# Create and insert a user
user_session = Sessions["user_db"]()
user = User(name="Ali Amr", email="AliAmr@gmail.com")
user_session.add(user)
user_session.commit()
user_id = user.id


# Payment history
pay_session = Sessions["payments_db"]()
for _ in range(20):
    pay_session.add(Payment(user_id=user_id, on_time=random.random() > 0.2))

# Debt
debt_session = Sessions["debt_db"]()
debt = Debt(user_id=user_id, credit_limit=10000, amount_used=random.randint(1000, 9000))
debt_session.add(debt)

# History
history_session = Sessions["history_db"]()
start_date = date.today() - timedelta(days=random.randint(1, 10) * 365)
history_session.add(History(user_id=user_id, start_date=start_date))


# Credit Mix
mix_session = Sessions["mix_db"]()
mix = CreditMix(user_id=user_id, types_used=random.randint(1, 4), total_types=4)
mix_session.add(mix)

# Commit all
pay_session.commit()
debt_session.commit()
history_session.commit()
mix_session.commit()

print("Sample data inserted for user_id:", user_id)
