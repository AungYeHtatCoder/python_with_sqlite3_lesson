import sqlite3
# conn = sqlite3.connect(':memory:')
# connect to a database
conn = sqlite3.connect('customer.db')
#create a cursor
c = conn.cursor()



# Query the database - and or
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'B%' AND rowid = 2")

# or
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'B%' OR rowid = 2")
items = c.fetchall()
# print(items)
print("ID" + "Name" + "\t" + "LASTNAME" + "\t" + "EMAIL")
print("------------------------------------------------------------")
for item in items:
    print(item)
# print("Command executed successfully...")

# Data types
# NULL -> no value
# integer -> whole number
# real -> floating point number
# text -> string
# blob (for images and other binary data)
conn.commit() # commit our command
# close our connection
conn.close()
# https://www.youtube.com/watch?v=byHcYRpMgI4