import pandas
from pandas import read_csv, DataFrame
import sqlite3
import os
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
conn = sqlite3.connect('buddy.db')

df = pandas.read_csv("buddymove_holidayiq.csv")
df.to_sql('users', con=conn)
engine.execute("SELECT * FROM users").fetchall()
