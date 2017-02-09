# flask-mysqldb
Simple Python+Flask application with Flask-MySQLdb database connection.

To run this code, you must have Python 3+ and Flask installed.

Don't forget to edit you database configuration in `__init__.py`.

If you are running this code on server (not localhost), remember to change line `app.run(debug=True)` to `app.run(host="0.0.0.0", post=XXXX, debug=True)` to be able to access it from the browser.


Read more about Flask-MySQL in its documentation: http://flask-mysqldb.readthedocs.io/en/latest/

Read more about creating web app in Flask from my blog (in Polish): http://www.alicja.it/category/flask/

There are two nice ways to connect to database in Flask - via Flask-MySQL and via Flask-MySQLdb. This is code using the second one. You can find example with the first here: https://github.com/alicjamusial/flask-mysql
