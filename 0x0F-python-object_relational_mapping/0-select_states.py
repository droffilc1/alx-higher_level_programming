#!/usr/bin/python3
"""
    0-select_states
"""
import os
import MySQLdb
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

MY_HOST = os.getenv("MY_HOST")
MY_USER = os.getenv("MY_USER")
MY_PASS = os.getenv("MY_PASS")
MY_DB = os.getenv("MY_DB")

def main():
    """
    Entry point
    """
    # Connect to a MySQL database
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC LIMIT 5")

    # Fetch all rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursir and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
