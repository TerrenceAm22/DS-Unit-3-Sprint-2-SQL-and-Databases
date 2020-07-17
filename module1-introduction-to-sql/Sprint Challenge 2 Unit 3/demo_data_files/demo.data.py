import sqlite3

import sqlite3
conn = sqlite3.connect('demo_data.sqlite')



def table_creation():
    create_table = """ CREATE TABLE test_demo (
        S text,
        X int,
        Y int)
        """ 
    curs = conn
    table = curs.execute(create_table).fetchall()
    curs.commit()
    print(table) 

def insert_data():
    data_entry = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]
    curs = conn
    curs.executemany("INSERT INTO test_demo VALUES(?, ?, ?)", data_entry)
    curs.commit()

def count_rows():
    ### Question 1 Count Rows in table
    query = 'SELECT COUNT(*) FROM test_demo;'
    curs = conn
    query1 = curs.execute(query).fetchall()
    curs.commit()
    print("NUMBER OF ROWS", query1)

def distinct_values():
    ### Function to return distinct values of column Y
    query2 = 'SELECT DISTINCT Y FROM test_demo;'
    curs = conn
    query2 = curs.execute(query2).fetchall()
    curs.commit()
    print("DISTINCT VALUES OF COLUMN Y", query2)

def conditonal_query():
    """ Function to return count of rows
    where column X and column Y are atleast 5
    """
    query3 = 'SELECT COUNT(*) FROM test_demo WHERE test_demo.x <= 5 AND test_demo.y >= 5;'
    curs = conn
    query3 = curs.execute(query3).fetchall()
    curs.commit()
    print("Conditional WHERE Query", query3)

    
    
    
    
#table_creation()
#insert_data()
#count_rows()
#distinct_values()
conditonal_query()





