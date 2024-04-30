import psycopg2

conn = psycopg2.connect(
    host="localhost", 
    dbname='postgres', 
    user='postgres', 
    password='1234', 
    port=5432)

cur = conn.cursor()

# Creating a table in the database

cur.execute("""CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
            );
            """
            )

# Inserting data into a table

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
            
            (1, 'John', 26, 'm'),
            (2, 'Sarah', 26, 'f'),
            (3, 'Linda', 26, 'f'),
            (4, 'Bren', 26, 'm'),
            (5, 'Michael', 26, 'm'),
            (6, 'Veronica', 26, 'f'),
            (7, 'Paul', 26, 'm'),
            (8, 'Timothy', 26, 'm');
            """)

# Adding column to table
cur.execute(""" ALTER TABLE person
            ADD emp_id INT;

""")

# Insert values into new column
cur.execute(""" INSERT INTO person (emp_id)
                VALUES (500,
                        501, 
                        502,
                        503,
                        504,
                        505,
                        506,
                        507);
""")

# Create additional table
cur.execute("""CREATE TABLE IF NOT EXISTS employee (
            emp_id INT PRIMARY KEY,
            job_title VARCHAR(255)
            );
            """)
# Fill second table with data
cur.execute("""INSERT INTO employee (emp_id, job_title) VALUES

               (500, 'Accountant'),
               (501, 'Financial Analyst'),
               (502, 'Junior Software Engineer'),
               (503, 'Technician'),
               (504, 'Data Analyst'),
               (505, 'Data Scientist'),
               (506, 'Data Engineer'),
               (507, 'Lead Data Analyst');
            """)
# Join tables
cur.execute(""" SELECT *
            FROM person
            INNER JOIN employee
            ON person.emp_id = employee.emp_id;
""")
# filter tables with query
cur.execute("""

""")


conn.commit()

cur.close()

conn.close()