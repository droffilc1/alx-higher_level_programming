#!/usr/bin/python3
"""
    1-filter_states
"""
import os
import MySQLdb
from dotenv import load_dotenv

load_dotenv()

MY_HOST = os.getenv("MY_HOST")
MY_USER = os.getenv("MY_USER")
MY_PASS = os.getenv("MY_PASS")
MY_DB = os.getenv("MY_DB")

def main():
    """
        Entry point
    """
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC LIMIT 2")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()
