import psycopg2

DB_NAME = 'ggrrjklv'
DB_USER = 'ggrrjklv'
DB_PASSWORD = 'cTA7aHWgPxf4kzOOBeKS5dhRUSW4sk5i'
DB_HOST = 'ruby.db.elephantsql.com'

### Connecting to ELephantSQL
pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", pg_conn)

pg_curs = pg_conn.cursor()
create_table = """ CREATE TABLE titanic (
            id SERIAL PRIMARY KEY,
            name varchar(30) NOT NULL,
            data JSONB);
            """
### Creating and Committing Table to Server
pg_curs.execute(create_table)
pg_conn.commit()


