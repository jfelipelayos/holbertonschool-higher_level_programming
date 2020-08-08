#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database"""
import MySQLdb
import sys

if __name__ == '__main__':

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host, user, password, database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states "
                   "WHERE name LIKE BINARY '{}' "
                   "ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
