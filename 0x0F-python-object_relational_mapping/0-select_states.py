#!/usr/bin/python3
"""
    0-select_states
"""
from sys import argv
import MySQLdb


def main():
    """
    Entry point
    """
    # Connect to a MySQL database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
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
