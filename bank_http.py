from flask import Flask, request, render_template
import bank
from flask_mysqldb import MySQL
from db import select_accounts, setup

app = Flask(__name__)
bank1 = bank.Bank()

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'ulysses123'
# app.config['MYSQL_DB'] = 'bank_accounts'
# mysql = MySQL(app)

mysql = setup(app)


def update_balance(new_balance, account_number):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE account_list SET balance = (%s) WHERE number = (%s)", [new_balance, account_number])
    mysql.connection.commit()
    cur.close()


@app.route("/")
def home():
    # cur = mysql.connection.cursor()
    # result = cur.execute("SELECT * from account_list")
    # if result > 0:
    #     account_list = cur.fetchall()
    account_list = select_accounts(mysql)
    for account in account_list:
        acc = bank1.create_account(account[0])  # Create the account using the number on the db
        acc.deposit(account[1])  # Update the account balance with the value present on the db
    # cur.close()
    return render_template('front_page.html')


@app.route("/account", methods=['POST'])
def create_account():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * from account_list")
    if result > 0:
        account_list = cur.fetchall()
        last_number = account_list[-1][0]
        last_number += 1
    else:
        last_number = 5000

    account = bank1.create_account(last_number)
    account_number = account.number
    account_balance = account.balance
    cur.execute("INSERT INTO account_list (number, balance) VALUES(%s, %s)", [int(account_number), int(account_balance)])
    mysql.connection.commit()
    cur.close()
    return f'The acccount number: {account.number} with a balance of {account.balance} was created'


@app.route("/account/balance", methods=['POST'])
def show_balance():
    account_number = request.form['account_number']
    account_balance = bank1.show_balance(int(account_number))
    return f'The account {account_number} has a balance of {account_balance}'
    # return bank1.show_balance(int(account_number))


@app.route("/search/show_balance", methods=['POST'])
def search_show_balance():

    return render_template('search_show_balance.html')


@app.route("/account/deposit", methods=['POST'])
def deposit():
    account_number = int(request.form['account_number'])
    value = int(request.form['value'])
    new_balance = bank1.make_deposit(account_number, value)
    update_balance(new_balance, account_number)

    return f'The value of {value} was deposited to the account {account_number}'


@app.route("/search/deposit", methods=['POST'])
def search_deposit():

    return render_template('search_deposit.html')


@app.route("/account/withdraw", methods=['POST'])
def withdraw():
    account_number = int(request.form['account_number'])
    value = int(request.form['value'])
    new_balance = bank1.make_withdraw(account_number, value)
    update_balance(new_balance, account_number)

    return f'The value of {value} was withdrawn from the account number {account_number}'


@app.route("/search/withdraw", methods=['POST'])
def search_withdraw():
    return render_template('search_withdraw.html')


@app.route("/account/transfer", methods=['POST'])
def transfer():
    account_number1 = int(request.form['account_number1'])
    account_number2 = int(request.form['account_number2'])
    value = int(request.form['value'])
    new_balance1, new_balance2 = bank1.transfer(account_number1, account_number2, value)
    update_balance(new_balance1, account_number1)
    update_balance(new_balance2, account_number2)
    return f'The value of {value} was transfered from the account {account_number1} to the account {account_number2}'


@app.route("/search/transfer", methods=['POST'])
def search_transfer():

    return render_template('search_transfer.html')


@app.route("/search/delete", methods=['POST'])
def search_delete():

    return render_template('search_delete.html')


@app.route("/account/delete", methods=['POST'])
def delete_account():
    account_number = int(request.form['account_number'])
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM account_list WHERE number=%s", [account_number])
    mysql.connection.commit()
    cur.close()
    bank1.delete_account(account_number)
    return f'The account {account_number} was deleted'


@app.route("/all_accounts", methods=['POST'])
def show_all_accounts():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from account_list")
    result = cur.fetchall()
    cur.close()
    return render_template('accounts.html', result=result)






