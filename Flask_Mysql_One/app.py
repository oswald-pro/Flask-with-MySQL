from flask import Flask, render_template
import pymysql

app = Flask(__name__)


class Database:
    def __init__(self):
        host = '194.5.156.94'
        user = 'u725134598_OmitAdm'
        password = 'Chantal9933**'
        db = 'u725134598_OMITDB'
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def user_table(self):
        self.cur.execute("SELECT id, EmployeeID, FirstName, LastName, Gender, Email, Role, Password FROM Users")
        result = self.cur.fetchall()
        return result


@app.route('/')
def index():
    def db_query():
        db = Database()
        my_users = db.user_table()
        return my_users

    res = db_query()
    return render_template('users.html', result=res)


if __name__ == '__main__':
    app.run()



