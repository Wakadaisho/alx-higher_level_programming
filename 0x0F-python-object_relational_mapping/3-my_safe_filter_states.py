#!/usr/bin/python3

"""
Module 3-my_safe_filter_states.py
List all the states whose name matches a given argument
from the database hbtn_0e_0_usa
Checks for safe input (in execute)
"""

import MySQLdb
from sys import argv


def run_db_query(query, args=None):
    """Run a db query and return the cursor results

    Args:
        query (str): sql query to run
        args (tuple): possible arguments to query

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
            cur.execute(query, args)
            query_rows = cur.fetchall()
    return query_rows


if __name__ == "__main__":
    results = run_db_query("""
                            SELECT *
                            FROM states
                            WHERE name = %s
                            ORDER BY id ASC
                           """,
                           (argv[4],))
    for row in results:
        print(row)
