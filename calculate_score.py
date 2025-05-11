from datetime import date
from engines import Sessions
from models.payments_db import Payment
from models.debt_db import Debt
from models.history_db import History
from models.mix_db import CreditMix

def calculate_credit_score(user_id):
    # Sessions
    payments = Sessions["payments_db"]().query(Payment).filter_by(user_id=user_id).all()
    on_time = sum(p.on_time for p in payments)
    total = len(payments)
    payment_score = (on_time / total) * 100 if total else 0

    debt = Sessions["debt_db"]().query(Debt).filter_by(user_id=user_id).first()
    debt_score = ((1 - (debt.amount_used / debt.credit_limit)) * 100) if debt else 0

    history = Sessions["history_db"]().query(History).filter_by(user_id=user_id).first()
    age = (date.today() - history.start_date).days / 365 if history else 0
    history_score = (age / 10) * 100

    mix = Sessions["mix_db"]().query(CreditMix).filter_by(user_id=user_id).first()
    mix_score = (mix.types_used / mix.total_types) * 100 if mix else 0

    final_score = (
        0.35 * payment_score +
        0.30 * debt_score +
        0.15 * history_score +
        0.20 * mix_score
    )

    scaled = 300 + (final_score / 100) * (850 - 300)

    return round(scaled, 2), {
        "payment_score": round(payment_score, 2),
        "debt_score": round(debt_score, 2),
        "history_score": round(history_score, 2),
        "mix_score": round(mix_score, 2)
    }
