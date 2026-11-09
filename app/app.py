from flask import Flask, render_template, request
import os
from db import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/employees")
def employees():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees")
        records = cursor.fetchall()
        cursor.close()
        connection.close()

        return render_template("employees.html", employees=records)

    except Exception as error:
        app.logger.exception("Database connection failed")
        return "Database connection failed", 500

@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form.get("name")
    email = request.form.get("email")

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO employees (name, email) VALUES (%s, %s)",
            (name, email)
        )

        connection.commit()
        cursor.close()
        connection.close()

        return "Employee added successfully. <a href='/employees'>View employees</a>"

    except Exception:
        app.logger.exception("Could not add employee")
        return "Could not add employee", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
