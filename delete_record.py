import sqlite3
# conn = sqlite3.connect(':memory:')
# connect to a database
conn = sqlite3.connect('customer.db')
#create a cursor
c = conn.cursor()

#delete record
c.execute("DELETE from customers WHERE rowid = 1")
conn.commit()

# Query the database
# c.execute("SELECT * FROM customers where last_name = 'Indavudha'")
c.execute("SELECT rowid, * FROM customers")


# no rows id command
# c.execute("SELECT * FROM customers")

# c.fetchone()
# c.fetchmany(3)
# print(c.fetchall())
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