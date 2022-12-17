from faker import Faker
import sqlite3 as sql
import random

faker = Faker()


local_database = './instance/site.db'

def add_data():  
  try:
    # Connecting to database
    connections = sql.connect(local_database)
    #  Getting cursor
    cur =  connections.cursor() 
    # c.execute(f"Select * from 'profile'")
    # row = c.fetchone()
    # print(row)
    print("Successfully Connected to SQLite")
    for datas in range(10):
        first_names = faker.first_name()
        last_names = faker.last_name()
        ages = random.randint(20,60)
        # print(f"first_name - {first_name} --- last_name - {last_name}  --- age - {age}")
        # Adding data
        sqlite_insert_query = f"""INSERT INTO profile ('first_name','last_name','age') VALUES ('{first_names}','{last_names}','{ages}')
        """
        print(sqlite_insert_query)
        count = cur.execute(sqlite_insert_query)
        connections.commit() 
    cur.close()    
    print("Data Added successfully")
  except sql.Error as error:
    print("Failed to insert data into sqlite table", error)
    
add_data()