import sqlite3


def check_tab_exist(cur: sqlite3.Cursor, table: str):
    """Check if a table exists in the database."""
    sql = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'"
    cur.execute(sql)
    rows = cur.fetchall()
    return len(rows) != 0


def create_table(cur: sqlite3.Cursor, table: str, table_attr: str):
    """Drop and recreate a table with the given schema."""
    cur.execute(f"DROP TABLE IF EXISTS {table}")
    cur.execute(table_attr)


def insert_data(cur, table: str, data):
    """Insert data into the table."""
    for row in data:
        placeholders = ', '.join(['?'] * len(row))
        sql = f"INSERT INTO {table} VALUES({placeholders})"
        cur.execute(sql, row)


def create_tab(conn: sqlite3.Connection):
    """Create tables and populate them with initial data."""
    cur = conn.cursor()

    # Define tables
    sqls = {
        "stop": """
        CREATE TABLE IF NOT EXISTS stop (
            stop_id INTEGER PRIMARY KEY,
            x REAL NOT NULL,
            y REAL NOT NULL,
            stop_name TEXT NOT NULL
        )
        """,
        "paths": """
        CREATE TABLE IF NOT EXISTS path (
            path_id INTEGER PRIMARY KEY,
            start_stop INTEGER NOT NULL,
            end_stop INTEGER NOT NULL,
            distance REAL NOT NULL,
            gas_usage REAL NOT NULL,
            FOREIGN KEY (start_stop) REFERENCES Stops(stop_id),
            FOREIGN KEY (end_stop) REFERENCES Stops(stop_id)
        )
        """,
        "roadconditions": """
        CREATE TABLE IF NOT EXISTS RoadConditions (
            path_id INTEGER PRIMARY KEY,
            clearance TEXT NOT NULL,
            comments TEXT,
            FOREIGN KEY (path_id) REFERENCES Paths(path_id)
        )
        """,
        "driver": """
        CREATE TABLE IF NOT EXISTS Driver (
            d_driverid INTEGER PRIMARY KEY,
            d_busid INTEGER NOT NULL,
            d_subbusid INTEGER NOT NULL,
            d_drivername TEXT NOT NULL,
            d_experience TEXT NOT NULL,
            d_status TEXT NOT NULL
        )
        """,
        "bus": """
        CREATE TABLE IF NOT EXISTS Bus (
            b_busid INTEGER PRIMARY KEY,
            b_condition TEXT NOT NULL,
            b_gas REAL NOT NULL
        )
        """,
        "route": """
        CREATE TABLE IF NOT EXISTS Route (
            r_routeid INTEGER PRIMARY KEY,
            r_busid INTEGER NOT NULL,
            r_routename TEXT NOT NULL,
            r_starttime TEXT NOT NULL,
            r_endtime TEXT NOT NULL,
            r_routeday TEXT NOT NULL
        )
        """,
        "routedetails": """
        CREATE TABLE IF NOT EXISTS RouteDetails (
            rd_routeid INTEGER NOT NULL,
            rd_stopid INTEGER NOT NULL,
            rd_stopno INTEGER NOT NULL,
            PRIMARY KEY (rd_routeid, rd_stopid),
            FOREIGN KEY (rd_routeid) REFERENCES Route(r_routeid),
            FOREIGN KEY (rd_stopid) REFERENCES Stops(stop_id)
        )
        """
    }

    # Define initial data
    stop_data = [
        (1, 0.0, 0.0, "Stop 1"),
        (2, 0.25, 0.25, "Stop 2"),
        (3, 0.75, 0.25, "Stop 3"),
        (4, 0.75, 0.1, "Stop 4"),
        (5, 0.25, 0.1, "Stop 5"),
        (6, 0.25, 0.0, "Stop 6")
    ]

    path_data = [
        (1, 1, 2, 0.3546, 0.047),
        (2, 2, 3, 0.5, 0.067),
        (3, 3, 4, 0.15, 0.02),
        (4, 4, 5, 0.5, 0.067),
        (5, 5, 6, 0.1, 0.013),
        (6, 6, 1, 0.25, 0.033),
        (7, 2, 5, 0.15, 0.02)
    ]

    road_conditions_data = [
        (1, "CLEAR", ""),
        (2, "CLEAR", ""),
        (3, "CLEAR", ""),
        (4, "CLEAR", "Maintenance complete"),
        (5, "CLEAR", ""),
        (6, "CLEAR", ""),
        (7, "CLEAR", "")
    ]

    driver_data = [
        (1, 1, 1, "DRIVER#001", "EXPERIENCED", "ACTIVE"),
        (2, 1, 2, "DRIVER#002", "NOVICE", "ACTIVE")
    ]

    bus_data = [
        (1, "FUNCTIONAL", 50),
        (2, "MAINTENANCE", 30)
    ]

    route_data = [
        (1, 1, "Route A", "08:00", "10:00", "Monday"),
        (2, 2, "Route B", "11:00", "13:00", "Tuesday")
    ]

    routedetails_data = [
        (1, 1, 1),
        (1, 2, 2),
        (1, 3, 3),
        (2, 4, 1),
        (2, 5, 2),
        (2, 6, 3)
    ]

    # Create and populate tables
    for table, schema in sqls.items():
        if not check_tab_exist(cur, table):
            create_table(cur, table, schema)
            if table == "stops":
                insert_data(cur, table, stop_data)
            elif table == "paths":
                insert_data(cur, table, path_data)
            elif table == "roadconditions":
                insert_data(cur, table, road_conditions_data)
            elif table == "driver":
                insert_data(cur, table, driver_data)
            elif table == "bus":
                insert_data(cur, table, bus_data)
            elif table == "route":
                insert_data(cur, table, route_data)
            elif table == "routedetails":
                insert_data(cur, table, routedetails_data)

    conn.commit()


def main():
    conn = sqlite3.connect("Checkpoint2-dbase.sqlite3")
    create_tab(conn)
    conn.close()


if __name__ == "__main__":
    main()
