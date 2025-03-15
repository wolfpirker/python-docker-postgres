import os
import psycopg2
import requests
import pandas as pd
from data_processing import process_data
from cli import CLI

# Database connection settings
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'dbname': os.getenv('DB_NAME')
}

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()

def insert_data(conn, data):
    with conn.cursor() as cur:
        for user in data:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING", (user['name'], user['email']))
        conn.commit()

def main():
    # Fetch data from API
    raw_data = fetch_data()
    
    # Process data using Pandas
    processed_data = process_data(raw_data)
    
    # Connect to the database
    conn = psycopg2.connect(**DB_CONFIG)
    
    # Insert processed data into the database
    insert_data(conn, processed_data)
    
    # Initialize and run the CLI
    cli = CLI(conn)
    cli.run()
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
