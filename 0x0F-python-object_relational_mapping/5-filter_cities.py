#!/usr/bin/python3
"""All cities by state"""
import MySQLdb
import sys

if __name__ == '__main__':

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host, user, password, database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities, states \
                   WHERE cities.state_id =states.id and states.name=%s\
                   ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cursor.fetchall()

    cities = []
    for row in rows:
        cities.append(row[0])

    print(", ".join(cities))
    cursor.close()
    db.close()
