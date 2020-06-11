import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT (*) FROM charactercreator_character;'
curs.execute(query)
total = curs.execute(query).fetchall()
print("TOTAL", total)