import psycopg2
from psycopg2.extras import execute_values
import os
import csv
import pandas 
from pandas import read_csv

DB_NAME = 'ggrrjklv'
DB_USER = 'ggrrjklv'
DB_PASSWORD = 'cTA7aHWgPxf4kzOOBeKS5dhRUSW4sk5i'
DB_HOST = 'ruby.db.elephantsql.com'


### Connecting to ELephantSQL
class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("Cannot Connect to database")
    
    def table_creation(self):
        table_creation_query = """
        DROP TABLE passengers;
        CREATE TABLE IF NOT EXISTS passengers (
            id SERIAL PRIMARY KEY,
            survived integer,
            pclass integer,
            name varchar NOT NULL,
            gender varchar NOT NULL,
            age float,
            sib_spouse_count integer,
            parent_child_count integer,
            fare float);
            """
        self.cursor.execute(table_creation_query)
        
        
    
    def create_table(self):
        titanic = """ 
        CREATE TYPE sex AS ENUM ('male', 'female');
        CREATE TABLE titanic (
            Survived INTEGER NOT NULL,
            Pclass INTEGER NOT NULL,
            Name TEXT NOT NULL,
            Sex sex,
            Age NUMERIC NOT NULL,
            Siblings_Spouses Aboard INTEGER NOT NULL,
            Parents/Children Aboard INTEGER NOT NULL,
            Fare NUMERIC NOT NULL);
            """
        self.connection.commit()

    def data(self):
        f = open('/Users/terrenceam22/Documents/Build/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv', 'w')
        self.cursor.copy_to(f, 'passengers', sep=',')
        f.close()
        f = open('/Users/terrenceam22/Documents/Build/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv', 'r')
        self.cursor.copy_from(f, 'titanic', sep=',')
        self.connection.commit()
        
    def insert_data(self):
        with open(r'titanic.csv', 'r') as f:
            self.cursor.copy_from(f, 'titanic', sep=',')
            f.close()
            self.connection.commit()
        
        
if __name__=='__main__':
    database_connection = DatabaseConnection()
    #database_connection.create_table()
    #database_connection.data()
    database_connection.insert_data()