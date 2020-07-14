import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT (*) FROM armory_item;'
curs.execute(query)
total3 = curs.execute(query).fetchall()
print("TOTAL3", total3)