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

# Inserting person data into a table

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

# Adding column to table for employee id
cur.execute(""" ALTER TABLE person
            ADD emp_id INT;

""")

# Inserting employee id values into new column
cur.execute(""" UPDATE person
                SET emp_id = CASE 
                                WHEN id = 1 THEN 500
                                WHEN id = 2 THEN 501
                                WHEN id = 3 THEN 502
                                WHEN id = 4 THEN 503
                                WHEN id = 5 THEN 504
                                WHEN id = 6 THEN 505
                                WHEN id = 7 THEN 506
                                WHEN id = 8 THEN 507
                                ELSE NULL
                            END;
""")

# Creating additional table to contain employee data
cur.execute("""CREATE TABLE IF NOT EXISTS employee (
            emp_id INT PRIMARY KEY,
            job_title VARCHAR(255)
            );
            """)

# Updating second table with data
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

# Joining tables on employee id
cur.execute(""" SELECT *
            FROM person
            INNER JOIN employee
            ON person.emp_id = employee.emp_id;
""")

# filter tables with query
# finding all employees that work in the data field
query = cur.execute(""" SELECT person.name
            FROM person
            INNER JOIN employee
            ON person.emp_id = employee.emp_id
            WHERE employee.job_title IN ('Data Analyst', 'Data Scientist' ,'Data Engineer', 'Lead Data Analyst');
""")

conn.commit()

cur.close()

conn.close()