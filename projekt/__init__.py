from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database_name'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)
from projekt import views
