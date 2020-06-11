import psycopg2
DB_NAME = 'ciczfjoe'
DB_USER = 'ciczfjoe'
DB_PASSWORD = 'OR9vK8l8FhGb0IbUCuJ79M4wpXEUPlBf'
DB_HOST = 'ruby.db.elephantsql.com'

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION",  connection)
                    
### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
print("CURSOR", cursor)
### An example query
cursor.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cursor.fetchall()
print(result)