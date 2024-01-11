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
NEW_DB = os.getenv("NEW_DB")

def main():
    """
        Entry point
    """
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=NEW_DB)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC LIMIT 15")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()
