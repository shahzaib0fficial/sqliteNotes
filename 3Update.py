import sqlite3

#connecting with database

conn = sqlite3.connect('database.db')

#create a cursor

cursor = conn.cursor()

#UPDATE data in table

cursor.execute("UPDATE studentTable SET Name = 'AbdulAleem' where rowid = 1")

#Commit command

conn.commit()

#close connection

conn.close()