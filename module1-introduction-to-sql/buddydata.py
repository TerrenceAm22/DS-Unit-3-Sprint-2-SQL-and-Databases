import pandas
from pandas import read_csv
import sqlite3

buddy = read_csv('buddymove_holidayiq.csv')
#print(buddy.head())

buddy.to_sql(schema=None)
conn = sqlite3.connect('buddymove_holidayiq.csv')
curs = conn.cursor()
query = 'SELECT * FROM user;'
curs.execute(query)
total10 = curs.execute(query).fetchall()
