import psycopg2
from psycopg2 import Error

try:
    
    # connct to database
    connection = psycopg2.connect(
        user="admin", password="root", host="127.0.0.1", port="5432", database="mydb"
    )
    cursor = connection.cursor()
    delete = """ DROP TABLE utilisateur;"""
    
    # creation d la table utilisateur
    create_table_query = """CREATE TABLE utilisateur
          (id SERIAL PRIMARY KEY     NOT NULL,
          nom           VARCHAR(255)    NOT NULL,
          prenom         VARCHAR(255))
          ; """
    
    # execution de laa commmande sql
    cursor.execute(create_table_query)
    
    #cursor.execute(delete)
    connection.commit()
    print("Table created successfully in PostgreSQL ")


except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)
finally:
    
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
