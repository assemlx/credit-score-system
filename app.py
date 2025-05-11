from flask import Flask, render_template, request
from engines import Sessions
from calculate_score import calculate_credit_score
from models.user_db import User

app = Flask(__name__)

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

            # Check if user exists
            user_session = Sessions["user_db"]()
            user = user_session.query(User).filter_by(id=user_id).first()

            if not user:
                error = f"No user found with ID {user_id}."
            else:
                try:
                    score, details = calculate_credit_score(user_id)

                    # Check if all score components are zero (meaning insufficient data)
                    if all(v == 0 for v in details.values()):
                        error = f"User {user.name} exists, but there isn't enough data to calculate their credit score."
                    else:
                        result = {"score": score, "details": details}
                        user_info = {
                            "id": user.id,
                            "name": user.name,
                            "email": user.email
                        }

                except Exception as e:
                    error = f"An error occurred: {str(e)}"

    return render_template("index.html", result=result, user_info=user_info, error=error)

if __name__ == "__main__":
    app.run(debug=True)
