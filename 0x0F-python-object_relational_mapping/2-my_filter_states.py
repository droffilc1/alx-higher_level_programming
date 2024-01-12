#!/usr/bin/python3
"""
    2-my_filter_states
"""
from sys import argv
import MySQLdb


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
    cur.execute("SELECT * FROM states WHERE name='{}' \
                ORDER BY id ASC".format(argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
