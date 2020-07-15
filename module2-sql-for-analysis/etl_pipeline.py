import psycopg2
import csv


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
    
    def create_table(self):
        titanic = """
                    CREATE TABLE titanic(
                    id SERIAL PRIMARY KEY,
                    name varchar(40) NOT NULL);
                    """
        self.cursor.execute(titanic)
    
    def data(self):
        f = open(r'/Users/terrenceam22/Documents/Build/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv', 'r')
        self.cursor.copy_from(f, 'titanic', sep=',')
        f.close()
        self.connection.commit()
        
        


if __name__=='__main__':
    database_connection = DatabaseConnection()
    #database_connection.create_table()
    database_connection.data()