import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def check_tab_exist(cur: sqlite3.Cursor, table: str):
    sql = f"""
        SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'
    """
    cur.execute(sql)
    rows = cur.fetchall()
    return len(rows) != 0


def check_tab_update(cur: sqlite3.Cursor, table: str):
    sql = f"SELECT * FROM {table}"

    cur.execute(sql)
    rows = cur.fetchall()

    f = open(f"./data/{table}.db", "r")
    lines = f.readlines()

    return len(rows) == len(lines)


def test_table(cur: sqlite3.Cursor, table: str):
    sql = f"SELECT * FROM {table}"
    cur.execute(sql)
    rows = cur.fetchall()

    # for row in rows:
    #   print(row)


def create_table(cur: sqlite3.Cursor, table: str, table_attr: str):
    sql = f"DROP TABLE IF EXISTS {table}"
    cur.execute(sql)
    cur.execute(table_attr)


def import_data(cur: sqlite3.Cursor, table: str):
    cur.executescript(f"import ./data/{table}.db {table}")


def insert_data(cur, table: str):
    f = open(f"data/{table}.db", "r")
    lines = f.readlines()

    n = len(lines[0].strip().split("|"))
    s = (n * "?,")[:-1]

    for line in lines:
        line = line.strip().split("|")
        sql = f"INSERT INTO {table} VALUES({s})"
        cur.execute(sql, (list(line)))

def create_tab(conn: sqlite3.Connection):
    """
    Create tables in the database and store in file tpch.sqlite
    """
    cur = conn.cursor()
    sqls = {
        "driver": """
        CREATE TABLE IF NOT EXISTS driver (
            d_driverid		INTEGER PRIMARY KEY
	        d_busid			INTEGER,
	        d_subbusid		INTEGER,
	        d_drivername	TEXT,
	        d_experience	TEXT,
	        d_status        TEXT
            )
        """,

        "bus": """
        CREATE TABLE IF NOT EXISTS bus (
            b_busid			INTEGER PRIMARY KEY,
	        b_condition		TEXT,
	        b_gas			DECIMAL
            )
        """,

        "stop": """
        CREATE TABLE IF NOT EXISTS stop (
            s_stopid		INTEGER PRIMARY KEY
	        s_locationx		DECIMAL,
	        s_locationy		DECIMAL,
	        s_stopname		TEXT
            )
        """,

        "route": """
        CREATE TABLE IF NOT EXISTS route (
            r_routeid		INTEGER PRIMARY KEY,
	        r_busid			INTEGER,
	        r_routename		TEXT,
	        r_starttime		TEXT,
	        r_endtime		TEXT,
	        r_routeday		TEXT
            )
        """,

        "routedetails": """
        CREATE TABLE IF NOT EXISTS routedetails (
            rd_routeid		INTEGER PRIMARY KEY,
	        rd_stopid		INTEGER,
	        rd_stopno		DECIMAL
            )
        """,

        "path": """
        CREATE TABLE IF NOT EXISTS path (
            p_pathid		INTEGER PRIMARY KEY,
	        p_startid		INTEGER,
	        p_endid			INTEGER,
	        p_pathlength	DECIMAL,
	        p_gasusage		DECIMAL
            )
        """,

        "roadconditions": """
        CREATE TABLE IF NOT EXISTS roadconditions (
            rc_pathid		INTEGER PRIMARY KEY,
	        rc_clearance	TEXT,
	        rc_comments		TEXT
            )
        """
    }

    for table in sqls:
        if not check_tab_exist(cur, table) or not check_tab_update(cur, table):
            create_table(cur, table, sqls[table])
            # import_data(cur, table)
            insert_data(cur, table)
        test_table(cur, table)

    conn.commit()

def execute_query(sql, values=None, fetchone=False):
    conn = sqlite3.connect("tpch.sqlite")
    cur = conn.cursor()

    if values:
        cur.execute(sql, values)
    else:
        cur.execute(sql)

    if fetchone:
        result = cur.fetchone()
    else:
        result = cur.fetchall()

    conn.commit()
    conn.close()

    return result

def main():
    conn = sqlite3.connect(r"tpch.sqlite")
    create_tab(conn)
    conn.close()

if __name__ == "__main__":
    main()
    app.run(debug=True)
