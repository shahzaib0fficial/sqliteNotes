import sqlite3

#connecting with database

conn = sqlite3.connect('database.db')

#create a cursor

cursor = conn.cursor()

#SELECT data from Table

cursor.execute("SELECT * FROM studentTable")
data = cursor.fetchall()

print(data)

#Commit command

conn.commit()

#close connection

conn.close()