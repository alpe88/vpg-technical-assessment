import psycopg2
from psycopg2 import sql
import json
import os
import sys

# Check if the script is provided with a database name argument
if len(sys.argv) != 2:
    print("Usage: python script requires database name")
    sys.exit(1)

# Get the database name from the command-line argument
db_name = sys.argv[1]


try:
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to config.json in the same directory as the script
    config_path = os.path.join(script_dir, 'config.json')

    # Read database configuration from config.json
    with open(config_path, 'r') as config_file:
        db_config = json.load(config_file)

    # Connect to PostgreSQL
    conn = psycopg2.connect(**db_config)
    conn.autocommit = True
    cursor = conn.cursor()

    sql = (f"CREATE DATABASE {db_name}")
    cursor.execute(sql)

    print(f"Database '{db_name}' created successfully.")

except psycopg2.Error as e:
    print("Error creating the database:", e)

finally:
    if 'conn' in locals():
        cursor.close()
        conn.close()
