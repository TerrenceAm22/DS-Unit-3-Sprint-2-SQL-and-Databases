import sqlite3
import pandas
from pandas import read_csv
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
conn = sqlite3.connect('titanic.db')
df = pandas.read_csv("titanic.csv", sep=',')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS passengers')
df.to_sql('passengers', con = conn)


def create_table():
    c.execute("""

    CREATE TABLE IF NOT EXISTS passengers(
        id SERIAL PRIMARY KEY,
        survived int,
        pclass integer
        name varchar(30),
        gender varchar(30),
        age float,
        sib_spouse_count int,
        parent_child_spouse int,
        fare float)
        """)
    conn.commit()


