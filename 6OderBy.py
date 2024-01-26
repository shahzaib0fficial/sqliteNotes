import sqlite3

#connecting with database

conn = sqlite3.connect('database.db')

#create a cursor

cursor = conn.cursor()

#Selecting BY ODER

cursor.execute("Select * FROM studentTable ORDER BY Name DESC") #By Default it's accending
data = cursor.fetchall()
print(data)


#Commit command

conn.commit()

#close connection

conn.close()