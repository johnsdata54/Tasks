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

# Insert values into new column

# Query duplicates

# Create additional table

# Fill second table with data

# Join tables

# filter tables with query



conn.commit()

cur.close()

conn.close()