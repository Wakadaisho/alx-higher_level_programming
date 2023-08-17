#!/usr/bin/python3

"""
Module 5-filter_cities.py
List all cities in a State
from the database hbtn_0e_0_usa
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
                            SELECT c.name
                            FROM states s
                            JOIN cities c ON s.id = c.state_id
                            WHERE s.name = %s
                            ORDER BY c.id ASC
                           """,
                           (argv[4],))
    print(", ".join([c for (c,) in results]))
