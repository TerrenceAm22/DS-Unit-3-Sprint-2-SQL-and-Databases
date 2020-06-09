import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT * FROM charactercreator_character, armory_weapon;'
curs.execute(query)
total6 = curs.execute(query).fetchall()
print("TOTAL6", total6)