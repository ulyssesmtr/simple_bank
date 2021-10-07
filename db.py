from flask_mysqldb import MySQL
from bank_http import app


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
