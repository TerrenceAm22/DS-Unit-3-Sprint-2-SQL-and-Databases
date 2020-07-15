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
        CREATE TABLE IF NOT EXISTS passengers (
            id SERIAL PRIMARY KEY,
            survived bool,
            pclass int,
            name varchar,
            sex varchar,
            age int,
            sib_spouse_count int,
            parent_child_count int,
            fare float8
            );
            """
        self.cursor.execute(titanic)
    
    def data(self):
        f = open(r'/Users/terrenceam22/Documents/Build/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv', 'r')
        self.cursor.copy_from(f, 'titanic', sep=',')
        f.close()
        self.connection.commit()
    
    def insert_data(self):
        list_of_tuples = list(df.to_records(index=True))
        insertion_query = "INSERT INTO passengers (id, survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
        execute_values(cursor, insertion_query, list_of_tuples)
        self.connection.commit()
        
if __name__=='__main__':
    database_connection = DatabaseConnection()
    #database_connection.create_table()
    database_connection.data()
    database_connection.insert_data()