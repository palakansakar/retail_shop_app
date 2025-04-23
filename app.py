from flask import Flask, render_template, request, redirect, flash
import sqlite3


# Base class using encapsulation
class Database:
    def __init__(self, db_name):
        self._db_name = db_name  # Encapsulated attributes

    def _connect(self):
        return sqlite3.connect(self._db_name)


# Inheriting from Database
class InquiryHandler(Database):
    def save_inquiry(self, name, email, message):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inquiries (name, email, message) VALUES (?, ?, ?)",
                       (name, email, message))
        conn.commit()
        conn.close()


# Flask App
app = Flask(__name__)
app.secret_key = 'secret'  # Required for flash messages
handler = InquiryHandler('retailshop.db')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_inquiry', methods=['POST'])
def send_inquiry():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    if not name or not email or not message:
        flash("All fields are required!", "error")
    else:
        handler.save_inquiry(name, email, message)
        flash("Your inquiry has been sent!", "success")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)