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

    # Define table creation SQLs
    sqls = {
        "stop": """
        CREATE TABLE IF NOT EXISTS Stops (
            stop_id INTEGER PRIMARY KEY,
            x REAL NOT NULL,
            y REAL NOT NULL,
            stop_name TEXT NOT NULL
        )
        """,
        "path": """
        CREATE TABLE IF NOT EXISTS Paths (
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
        (1, 0.0, 0.2, "Stop 1"),
        (2, 0.1, 0.2, "Stop 2"),
        (3, 0.1, 0.3, "Stop 3"),
        (4, 0.2, 0.3, "Stop 4"),
        (5, 0.2, 0.1, "Stop 5"),
        (6, 0.2, 0.0, "Stop 6"),
        (7, 0.3, 0.0, "Stop 7"),
        (8, 0.3, 0.1, "Stop 8"),
        (9, 0.3, 0.4, "Stop 9"),
        (10, 0.0, 0.4, "Stop 10"),
        (11, 0.0, 0.5, "Stop 11"),
        (12, 0.4, 0.5, "Stop 12"),
        (13, 0.4, 0.4, "Stop 13"),
        (14, 0.5, 0.4, "Stop 14"),
        (15, 0.5, 0.3, "Stop 15"),
        (16, 0.4, 0.3, "Stop 16"),
        (17, 0.4, 0.1, "Stop 17"),
        (18, 0.1, 0.0, "Stop 18"),
        (19, 0.1, 0.1, "Stop 19"),
        (20, 0.0, 0.0, "Stop 20")
    ]

    path_data = [
        (1, 2, 0.1, 0.0),
        (2, 3, 0.0, 0.1),
        (3, 4, 0.1, 0.0),
        (4, 5, 0.0, -0.2),
        (5, 6, 0.0, -0.1),
        (6, 7, 0.1, 0.0),
        (7, 8, 0.0, 0.1),
        (8, 9, 0.0, 0.3),
        (9, 10, -0.3, 0.0),
        (10, 11, 0.0, 0.1),
        (11, 12, 0.4, 0.0),
        (12, 13, 0.0, -0.1),
        (13, 14, 0.1, 0,0),
        (14, 15, 0,0, -0.1),
        (15, 16, -0.1, 0,0),
        (16, 17, 0,0, -0.1),
        (17, 18, -0.3, 0.0),
        (18, 19, 0.0, -0.1),
        (19, 20, -0.1, 0.0),
        (20, 1, 0.0, 0.2)
    ]

    road_conditions_data = [
        (1, "CLEAR", ""),
        (2, "CLEAR", ""),
        (3, "CLEAR", ""),
        (4, "CLEAR", ""),
        (5, "CLEAR", ""),
        (6, "CLEAR", ""),
        (7, "CLEAR", ""),
        (8, "CLEAR", ""),
        (9, "CLEAR", ""),
        (10, "CLEAR", ""),
        (11, "CLEAR", ""),
        (12, "CLEAR", ""),
        (13, "CLEAR", ""),
        (14, "CLEAR", ""),
        (15, "CLEAR", ""),
        (16, "CLEAR", ""),
        (17, "CLEAR", ""),
        (18, "CLEAR", ""),
        (19, "CLEAR", ""),
        (20, "CLEAR", "")
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
        (1, 2, "Route A", "09:00", "09:30", "Monday"),
        (2, 3, "Route B", "09:00", "09:30", "Tuesday")
    ]

    routedetails_data = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (7, 8),
        (8, 9),
        (9, 10),
        (10, 11),
        (11, 12),
        (12, 13),
        (13, 14),
        (14, 15),
        (15, 16),
        (16, 17),
        (17, 18),
        (18, 19),
        (19, 20),
        (20, 1)
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
