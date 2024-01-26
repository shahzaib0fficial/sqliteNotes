import sqlite3

#connecting with database

conn = sqlite3.connect('database.db')

#create a cursor

cursor = conn.cursor()

#Limiting of Selection

cursor.execute("SELECT * FROM studentTable LIMIT 1")
data = cursor.fetchall()

print(data)

#Commit command

conn.commit()

#close connection

conn.close()