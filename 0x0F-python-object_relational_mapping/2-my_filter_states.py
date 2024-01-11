#!/usr/bin/python3
"""
    2-my_filter_states
"""
import os
import sys
import MySQLdb
from dotenv import load_dotenv

load_dotenv()

MY_HOST = os.getenv("MY_HOST")
MY_USER = os.getenv("MY_USER")
MY_PASS = os.getenv("MY_PASS")
MY_DB = os.getenv("MY_DB")

search_value = sys.argv[4]

def main():
    """
        Entry point
    """
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC LIMIT 1".format(search_value))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if  __name__ == "__main__":
    main()
