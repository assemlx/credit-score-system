from datetime import date
from config import DB_CONFIG
import mysql.connector
from database_setup import connect_to_db



def calculate_credit_score(user_id):
    # Payments
    conn = connect_to_db('payments_db')
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT on_time FROM payment WHERE user_id = %s", (user_id,))
    payments = cursor.fetchall()
    on_time = sum(p['on_time'] for p in payments)
    total = len(payments)
    payment_score = (on_time / total) * 100 if total else 0
    conn.close()

    # Debt
    conn = connect_to_db('debt_db')
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT amount_used, credit_limit FROM debt WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    debt_score = ((1 - row['amount_used'] / row['credit_limit']) * 100) if row else 0
    conn.close()

    # History
    conn = connect_to_db('history_db')
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT start_date FROM history WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    age = ((date.today() - row['start_date']).days / 365) if row else 0
    history_score = (age / 10) * 100
    conn.close()

    # Mix
    conn = connect_to_db('mix_db')
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT types_used, total_types FROM credit_mix WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    mix_score = (row['types_used'] / row['total_types']) * 100 if row else 0
    conn.close()

    # Final score
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

# if __name__ == "__main__":
#     score, breakdown = calculate_credit_score(1)
#     print("Credit Score:", score)
#     print("Breakdown:", breakdown)
