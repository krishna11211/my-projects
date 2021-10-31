import sqlite3
from typing import Text

conn = sqlite3.connect('demo.db') # Connect to Database in Python(Permanent)
# conn = sqlite3.connect(':memory:') # Connect tbase in Python(Temporary)

"""Create a Database Table"""
c = conn.cursor() # Create cursor(for adding data using cursor)

# Create a table
# c.execute("""CREATE TABLE demo (
#         first_name DATATYPE,
#         last_name DATATYOE
#     )""")

"""SQLite Datatypes"""
# Null
# Integer
# Real
# Text
# Blob - for photos, vidoes, audio & other files

"""Insert one record into the table"""
# c.execute("INSERT INTO demo VALUES ('joh', 'aditya')")
# print("Command executed Successfully...")

"""Insert many records into the table"""
# many_customer = [('Aditya', 'kumar', 'singh'), ('khushi', 'kumari', 'singh')]
# c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customer)
# print("Command executed Successfully...") # Error

"""Fetching date from .db file"""
# c.execute("SELECT * FROM demo")
# print(c.fetchmany(2))
# c.fetchmany(3)
# items = c.fetchall()
# for item in items:
#     print(item[0], " ", item[1])

# Primary Key Id

"""Format results"""
# c.execute("SELECT rowid, * FROM demo")
# items = c.fetchall()
# for item in items:
#     print(f"{item[0]} {item[1]} {item[2]}")

"""Where claus"""
# c.execute("SELECT * FROM demo WHERE last_name='adia'")
# c.execute("SELECT * FROM demo WHERE last_name LIKE 'adi%'")
# items = c.fetchall()
# for item in items:
#     print(item)

"""Update Records"""
# c.execute("""UPDATE demo SET first_name ='Bob'
#             WHERE last_name = 'aditya'

#     """)

"""Delete Record"""
# c.execute("DELETE from demo WHERE rowid=1")

"""Order Result by"""
# c.execute("SELECT rowid, * FROM demo ORDER BY rowid")
c.execute("SELECT rowid, * FROM demo ORDER BY rowid DESC")




# Commit our command
conn.commit()

# Update Records(You have to commit after the update/delete so that's it)
c.execute("SELECT * FROM demo")
items = c.fetchall()
for item in items:
    print(item)

# close our connection
conn.close()
