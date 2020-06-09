import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT (charactercreator_character_inventory.item_id) FROM charactercreator_character_inventory GROUP BY charactercreator_character_inventory.character_id LIMIT 20;'
curs.execute(query)
total4 = curs.execute(query).fetchall()
print("TOTAL4", total4)