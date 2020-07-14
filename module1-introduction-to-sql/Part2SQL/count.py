import sqlite3

conn = sqlite3.connect('buddy.db')
query = 'SELECT COUNT(Sports) FROM users;'
curs = conn
curs.execute(query)
totalcount = curs.execute(query).fetchall()
print("TOTAL COUNT", totalcount)