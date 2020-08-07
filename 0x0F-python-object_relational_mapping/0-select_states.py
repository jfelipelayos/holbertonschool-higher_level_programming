#!/usr/bin/python3
"""lists all states from the database"""
import MySQLdb
import sys

if __name__ == '__main__':

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host, user, password, database)
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
