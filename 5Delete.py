import sqlite3

#connecting with database

conn = sqlite3.connect('database.db')

#create a cursor

cursor = conn.cursor()

#Deleting in Records

cursor.execute("DELETE FROM studentTable WHERE Name = 'Shahzaib' AND rowid = 3")

#Commit command

conn.commit()

#close connection

conn.close()