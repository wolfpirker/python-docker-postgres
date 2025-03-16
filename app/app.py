import os
import pyodbc
import requests
import pandas as pd
from data_processing import process_data
from cli import CLI

# Database connection settings
DB_CONFIG = {
    'driver': 'ODBC Driver 17 for SQL Server',
    'server': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'Trusted_Connection': 'no',
}

def get_connection():
    connection_string = f"DRIVER={DB_CONFIG['driver']};SERVER={DB_CONFIG['server']},{DB_CONFIG['port']};DATABASE={DB_CONFIG['database']};UID={DB_CONFIG['user']};PWD={DB_CONFIG['password']}"
    return pyodbc.connect(connection_string)

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()

def insert_data(conn, data):
    cursor = conn.cursor()
    for user in data:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user['name'], user['email']))
    conn.commit()

def main():
    # Fetch data from API
    raw_data = fetch_data()
    
    # Process data using Pandas
    processed_data = process_data(raw_data)
    
    # Connect to the database
    conn = get_connection()
    
    # Insert processed data into the database
    insert_data(conn, processed_data)
    
    # Initialize and run the CLI
    cli = CLI(conn)
    cli.run()
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
