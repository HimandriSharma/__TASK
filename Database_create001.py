import sqlite3

conn = sqlite3.connect('base002.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE name002(here TEXT)')
print ("Table created successfully");
conn.close()