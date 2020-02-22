from flask import Flask
import sqlite3 as sql


app = Flask(__name__)


@app.route('/')
def one():
    return 'This is home.'

@app.route('/name')
def two():
    with sql.connect("base002.db") as con:
            cur = con.cursor()
            con.execute("INSERT INTO name002 (here) VALUES ('Paul')");
    return '<h1>Added query!<h1>'
   

if __name__=="__main__":
    app.run(debug=True)
