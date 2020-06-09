import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT AVG (charactercreator_character.character_id) FROM  charactercreator_character;'
curs.execute(query)
total8 = curs.execute(query).fetchall()
print("TOTAL8", total8)

