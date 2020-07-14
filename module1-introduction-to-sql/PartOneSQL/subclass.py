import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT * FROM charactercreator_mage, charactercreator_necromancer;'
curs.execute(query)
total2 = curs.execute(query).fetchall()
print("TOTAL2", total2)

