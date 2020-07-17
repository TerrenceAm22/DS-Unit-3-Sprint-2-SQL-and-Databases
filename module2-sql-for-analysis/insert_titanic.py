import psycopg2
from psycopg2.extras import execute_values
import os
import csv
import pandas 
from pandas import read_csv
from dotenv import load_dotenv
import sqlite3
sl_conn = sqlite3.connect('titanic.db')
sl_curs = sl_conn.cursor()
load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("Cannot Connect to database")
    
    def table_creation(self):
        create_table = """
        DROP TABLE IF EXISTS passengers;
        CREATE TABLE  passengers(
        id SERIAL PRIMARY KEY,
        survived int,
        pclass integer,
        name varchar(250),
        gender varchar(30),
        age float,
        sib_spouse_count int,
        parent_child_spouse int,
        fare float)
        """
        self.cursor.execute(create_table)
    def insert_data(self):
        get_passengers = 'SELECT Survived, Pclass, Name, Sex, Age, SibSp, Parch, Fare FROM passengers;'
        peoples = sl_curs.execute(get_passengers).fetchall()
        for people in peoples:
            insert_people = """
            INSERT INTO passengers
            (Survived, Pclass, Name, gender, Age, sib_spouse_count, parent_child_spouse, Fare)
            VALUES(%s, %s, %s, %s, %s, %s, %s,%s) """
            print(people[1:]) 
            self.cursor.execute(insert_people, people)
            self.connection.commit()
    def survivors(self):
        self.cursor.execute('SELECT COUNT(survived) FROM passengers WHERE survived = 0;')
        print(self.cursor.fetchall())
        self.connection.commit()
    
    def average_age(self):
        self.cursor.execute('SELECT AVG(age) FROM passengers;')
        print(self.cursor.fetchall())
        self.connection.commit()
    
    def average_fare(self):
        self.cursor.execute('SELECT AVG(fare) FROM passengers WHERE survived = 1;')
        print(self.cursor.fetchall())
        self.connection.commit()
    def average_parch(self):
        pass




        
    
if __name__=='__main__':
    database_connection = DatabaseConnection()
    #database_connection.table_creation()
    #database_connection.insert_data()
    #print(database_connection.survivors())
    #print(database_connection.average_age())
    print(database_connection.average_fare())
