#!/usr/bin/python3
"""
    2-my_filter_states
"""
from sys import argv
import MySQLdb

search_value = argv[4]


def main():
    """
        Entry point
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s \
                ORDER BY id ASC", (search_value,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
