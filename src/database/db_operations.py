import psycopg2
import os
from configparser import ConfigParser

# Read database configuration from a config file
config = ConfigParser()
config.read('config.ini')  # Place your config file in the same directory as your script

# Get database connection details from the config file
dbname = config.get('database', 'dbname')
user = config.get('database', 'user')
password = config.get('database', 'password')
host = config.get('database', 'host')

# Function to connect to the database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        return conn
    except Exception as e:
        print("Error:", e)
        return None

# Function to perform database operations (example)
def fetch_data():
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM your_table")
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("Error:", e)
        finally:
            conn.close()