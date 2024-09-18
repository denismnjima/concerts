import psycopg2
from psycopg2 import sql

def database_connect():
    try:
        conn = psycopg2.connect(
            dbname="concert",
            user="postgres",
            password="pass",
            host="localhost",  
            port="5432"      
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    