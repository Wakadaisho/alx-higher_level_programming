#!/usr/bin/python3

"""
Module 0-select_states.py
List all the states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


def run_db_query(query):
    """Run a db query and return the cursor results

    Args:
        query (str): sql query to run

    Returns:
        list of query results
    """
    query_rows = None
    with MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8") as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            query_rows = cur.fetchall()
    return query_rows


if __name__ == "__main__":
    results = run_db_query("SELECT * FROM states ORDER BY id ASC")
    for row in results:
        print(row)
