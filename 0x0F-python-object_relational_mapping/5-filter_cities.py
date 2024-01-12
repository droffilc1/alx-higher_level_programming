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
    cur.execute("SELECT * FROM cities\
                INNER JOIN states\
                ON cities.states_id = states.id\
                ORDER BY cities.id")

    print(", ".join([city[2]
                     for city in cur.fetchall()
                     if city[4] == argv[4]])
          )

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
