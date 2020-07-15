import pymongo
from pymongo import MongoClient
import sqlite3
client = pymongo.MongoClient("mongodb+srv://TerrenceM23:Paradox1998!@cluster0.2cfdw.mongodb.net/<test>?retryWrites=true&w=majority")
db = client.test
rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)
#db.test.insert_one({'rpg_character': rpg_character})
rpg_doc = {
    'sql_key': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
}
#db.test.insert_one(rpg_doc)
#db.test.find_one(rpg_doc)

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
get_characters = 'SELECT * FROM charactercreator_character;'
get_characters = sl_curs.execute(get_characters).fetchall()
print(get_characters)

get_characters = ({'get_characters': get_characters})

db.test.insert_one(get_characters)
