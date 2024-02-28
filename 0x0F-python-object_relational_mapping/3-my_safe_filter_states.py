#!/usr/bin/python3
"""A script that takes in an argument and displays 
    all values in the states table of hbtn_0e_0_usa
     My script has 3 arguments :  mysql username
                                  mysql password
                                  database name
                                 state name searched
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
