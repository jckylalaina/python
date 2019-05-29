# # -*- coding:utf-8 -*-


import psycopg2
from psycopg2 import Error
try:
  #connct to database
    connection = psycopg2.connect(user = "admin",
                                  password = "root",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "mydb")
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE mobile
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         REAL); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")
    a = '''select * from mobile'''
    cursor.execute(a)





except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")