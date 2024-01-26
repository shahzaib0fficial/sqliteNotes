import sqlite3

#connecting with database

conn = sqlite3.connect('database.db')

#create a cursor

cursor = conn.cursor()

#INSERT data in table

cursor.execute("INSERT INTO studentTable VALUES ('01','Shahzaib')")

#Commit command

conn.commit()

#close connection

conn.close()