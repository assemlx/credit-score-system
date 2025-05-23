from flask import Flask, render_template, request
import mysql.connector
from calculate_score import calculate_credit_score
from config import DB_CONFIG

app = Flask(__name__)

def get_user(user_id):
    conn = mysql.connector.connect(database='user_db', **DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    user_info = None

    if request.method == "POST":
        user_id_input = request.form.get("user_id")

        if not user_id_input or not user_id_input.isdigit():
            error = "Please enter a valid numeric user ID."
        else:
            user_id = int(user_id_input)
            user = get_user(user_id)

            if not user:
                error = f"No user found with ID {user_id}."
            else:
                try:
                    score, details = calculate_credit_score(user_id)

                    if all(v == 0 for v in details.values()):
                        error = f"User {user['name']} exists, but there isn't enough data to calculate their credit score."
                    else:
                        result = {"score": score, "details": details}
                        user_info = {
                            "id": user["id"],
                            "name": user["name"],
                            "email": user["email"]
                        }

                except Exception as e:
                    error = f"An error occurred: {str(e)}"

    return render_template("index.html", result=result, user_info=user_info, error=error)

if __name__ == "__main__":
    app.run(debug=True)

