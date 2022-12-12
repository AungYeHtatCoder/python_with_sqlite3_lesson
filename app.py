import database_conn
# add a new record
# database_conn.add_one('John', 'Elder', 'john@gmail.com')
# show all records
# database_conn.show_all()
# delete a record using rowid as string
# database_conn.delete_one('2')
# addd many records
list = [
 ('Wes', 'Brown', 'web@gmail.com'),
 ('Steph', 'Kuewa', 'st@gmail.com'),
 ('Dan', 'Pas', 'pa@gmail.com'),
 ('ashin', 'kumar', 'kumar@gmail.com')
]
# database_conn.add_many(list)
# call the email lookup function
database_conn.email_lookup('pa@gmail.com')