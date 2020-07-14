import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT * FROM charactercreator_character LIMIT 20;'
curs.execute(query)
total5 = curs.execute(query).fetchall()
print("TOTAL5", total5)