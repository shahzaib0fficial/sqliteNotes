import sqlite3

#connecting with database

conn = sqlite3.connect('database.db')

#create a cursor

cursor = conn.cursor()

#creating a Table

cursor.execute("""CREATE TABLE studentTable(
               Reg INTEGER,
               Name TEXT
    )""")


#Commit command

conn.commit()

#close connection

conn.close()