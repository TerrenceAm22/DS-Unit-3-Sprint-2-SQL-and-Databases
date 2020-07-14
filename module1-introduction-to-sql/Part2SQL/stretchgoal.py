import sqlite3

conn = sqlite3.connect('buddy.db')
query = '''SELECT AVG(Nature+Shopping+Theatre+Religious+Picnic+Sports)
AS Average FROM users;
'''
curs = conn
curs.execute(query)
totalavg = curs.execute(query).fetchall()
print("TOTAL AVG", totalavg)