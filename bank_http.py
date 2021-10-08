from flask import Flask, request, render_template
import bank
import db

app = Flask(__name__)
bank1 = bank.Bank()
mysql = db.setup(app)


def load_base():
    account_list = db.select_accounts(mysql)
    for account in account_list:
        acc = bank1.create_account(account[0])  # Create the account using the number on the db
        acc.deposit(account[1])  # Update the account balance with the value present on the db


@app.route("/")
def home():
    load_base()
    return render_template('front_page.html')


@app.route("/account", methods=['POST'])
def create_account():
    last_number = db.search_last_number(mysql)
    account = bank1.create_account(last_number)
    db.insert_account(mysql, account.number, account.balance)

    return f'The accccount number: {account.number} with a balance of {account.balance} was created'


@app.route("/account/balance", methods=['POST'])
def show_balance():
    try:
        account_number = request.form['account_number']
        account_balance = bank1.show_balance(int(account_number))
        return f'The account {account_number} has a balance of {account_balance}'
    except ValueError:
        return f'Invalid account'


@app.route("/search/show_balance", methods=['POST'])
def search_show_balance():

    return render_template('search_show_balance.html')


@app.route("/account/deposit", methods=['POST'])
def deposit():
    try:
        account_number = int(request.form['account_number'])
        value = int(request.form['value'])
        new_balance = bank1.make_deposit(account_number, value)
        db.update_balance_db(mysql, new_balance, account_number)

        return f'The value of {value} was deposited to the account {account_number}'
    except ValueError:
        return 'Invalid account number or value'


@app.route("/search/deposit", methods=['POST'])
def search_deposit():

    return render_template('search_deposit.html')


@app.route("/account/withdraw", methods=['POST'])
def withdraw():
    try:
        account_number = int(request.form['account_number'])
        value = int(request.form['value'])
        new_balance = bank1.make_withdraw(account_number, value)
        db.update_balance_db(new_balance, account_number)

        return f'The value of {value} was withdrawn from the account number {account_number}'
    except ValueError:
        return 'Invalid account number or value'


@app.route("/search/withdraw", methods=['POST'])
def search_withdraw():
    return render_template('search_withdraw.html')


@app.route("/account/transfer", methods=['POST'])
def transfer():
    try:
        account_number1 = int(request.form['account_number1'])
        account_number2 = int(request.form['account_number2'])
        value = int(request.form['value'])
        new_balance1, new_balance2 = bank1.transfer(account_number1, account_number2, value)
        db.update_balance_db(new_balance1, account_number1)
        db.update_balance_db(new_balance2, account_number2)
        return f'The value of {value} was transfered from the account {account_number1} to the account {account_number2}'
    except ValueError:
        return 'Invalid account number or value'


@app.route("/search/transfer", methods=['POST'])
def search_transfer():

    return render_template('search_transfer.html')


@app.route("/search/delete", methods=['POST'])
def search_delete():

    return render_template('search_delete.html')


@app.route("/account/delete", methods=['POST'])
def delete_account():
    try:
        account_number = int(request.form['account_number'])
        db.delete_account_db(mysql, account_number)
        bank1.delete_account(account_number)
        return f'The account {account_number} was deleted'
    except ValueError:
        return 'Invalid account number'


@app.route("/all_accounts", methods=['POST'])
def show_all_accounts():
    result = db.select_accounts(mysql)
    return render_template('accounts.html', result=result)






