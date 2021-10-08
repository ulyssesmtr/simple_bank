from flask_mysqldb import MySQL


def setup(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'ulysses123'
    app.config['MYSQL_DB'] = 'bank_accounts'
    mysql = MySQL(app)
    return mysql


def select_accounts(mysql):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * from account_list")
    if result > 0:
        account_list = cur.fetchall()
        cur.close()
        return account_list
    else:
        return []


def search_last_number(mysql):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * from account_list")
    if result > 0:
        account_list = cur.fetchall()
        last_number = account_list[-1][0]
        last_number += 1
        cur.close()
        return last_number
    else:
        cur.close()
        return 5000


def insert_account(mysql, account_number, account_balance):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO account_list (number, balance) VALUES(%s, %s)", [int(account_number), int(account_balance)])
    mysql.connection.commit()
    cur.close()


def update_balance_db(mysql, new_balance, account_number):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE account_list SET balance = (%s) WHERE number = (%s)", [new_balance, account_number])
    mysql.connection.commit()
    cur.close()


def delete_account_db(mysql, account_number):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM account_list WHERE number=%s", [account_number])
    mysql.connection.commit()
    cur.close()