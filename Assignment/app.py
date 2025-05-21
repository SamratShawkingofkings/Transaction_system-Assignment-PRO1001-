from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    with sqlite3.connect("transactions.db") as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                description TEXT NOT NULL,
                credit REAL DEFAULT 0,
                debit REAL DEFAULT 0,
                balance REAL
            )
        ''')

def calculate_running_balance():
    with sqlite3.connect("transactions.db") as conn:
        cursor = conn.execute("SELECT * FROM transactions ORDER BY date ASC, id ASC")
        rows = cursor.fetchall()
        balance = 0
        for row in rows:
            id, date, desc, credit, debit, _ = row
            balance += credit - debit
            conn.execute("UPDATE transactions SET balance = ? WHERE id = ?", (balance, id))
        conn.commit()

@app.route('/')
def index():
    calculate_running_balance()
    with sqlite3.connect("transactions.db") as conn:
        transactions = conn.execute("SELECT * FROM transactions ORDER BY date DESC, id DESC").fetchall()
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        t_type = request.form['type']
        amount = float(request.form['amount'])
        desc = request.form['description']
        date = datetime.today().strftime('%m/%d/%Y')

        credit = amount if t_type == 'Credit' else 0
        debit = amount if t_type == 'Debit' else 0

        with sqlite3.connect("transactions.db") as conn:
            conn.execute("INSERT INTO transactions (date, description, credit, debit, balance) VALUES (?, ?, ?, ?, 0)",
                         (date, desc, credit, debit))
            conn.commit()

        return redirect('/')
    return render_template('add_transaction.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
