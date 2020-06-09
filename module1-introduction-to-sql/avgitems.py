import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
query = 'SELECT AVG (charactercreator_character_inventory.item_id) FROM charactercreator_character_inventory;'
curs = conn
curs.execute(query)
total7 = curs.execute(query).fetchall()
print("TOTAL7", total7)
