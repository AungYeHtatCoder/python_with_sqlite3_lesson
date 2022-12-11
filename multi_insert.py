import sqlite3
# conn = sqlite3.connect(':memory:')
# connect to a database
conn = sqlite3.connect('customer.db')
#create a cursor
c = conn.cursor()



# multiple insert data to a table
many_customers = [
                 ('Wes', 'Brown', ' wes@gmail.com'),
                 ('Steph', 'Bru', 'step@gmail.com'),
                 ('Dan', 'Bara', 'pas@gmail.com'),
                 ]
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)
print("Command executed successfully...")

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