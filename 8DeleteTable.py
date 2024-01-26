import sqlite3

#connecting with database

conn = sqlite3.connect('database.db')

#create a cursor

cursor = conn.cursor()

#Delete whole Table

cursor.execute("DROP TABLE studentTable")

#An Error occurs because this table is no more exists

cursor.execute("SELECT * FROM studentTable")

#Commit command

conn.commit()

#close connection

conn.close()