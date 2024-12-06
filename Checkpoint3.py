import sqlite3
from sqlite3 import Error

# Database functions
# Open connection
def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn


# Close connection
def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


# Create tables
def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    cur = _conn.cursor()
    # driver
    cur.execute("""
    CREATE TABLE driver(
	d_driverid		integer not null primary key,
	d_busid			integer not null,
	d_drivername	char(100) not null,
	d_type      	char(100) not null,
	d_subid         integer not null,
	d_subbusid      integer not null,
	d_status		char(100) not null,
	d_hours		    decimal(9,0) not null);
    """)

    # bus
    cur.execute("""
    CREATE TABLE bus(
	b_busid			integer not null primary key,
	b_busname		char(100) not null,
	b_condition		char(100) not null,
	b_gas			decimal(9,0) not null);
    """)

    # stop
    cur.execute("""
    CREATE TABLE stop(
	s_stopid		integer not null primary key,
	s_locationx		decimal(9,0) not null,
	s_locationy		decimal(9,0) not null,
	s_stopname		char(100) not null);
    """)

    # stopdetails
    cur.execute("""
    CREATE TABLE stopdetails(
	sd_routetype	integer not null,
	sd_stopid		integer not null,
	sd_stopno		integer not null);
    """)

    # path_
    cur.execute("""
    CREATE TABLE path_(
	p_pathid		integer not null primary key,
	p_startid		integer not null,
	p_endid			integer not null,
	p_pathlength	decimal(9,0) not null,
	p_gasusage		decimal(9,0) not null);
    """)

    # pathdetails
    cur.execute("""
    CREATE TABLE pathdetails(
    pd_routetype	integer not null,
    pd_pathid		integer not null,
    pd_pathno		integer not null);
    """)

    # route
    cur.execute("""
    CREATE TABLE route(
    r_routeid		integer not null primary key,
    r_busid			integer not null,
    r_routename		char(100) not null,
    r_routetype		integer not null,
    r_starttime		char(100) not null,
    r_endtime		char(100) not null,
    r_day		    char(100) not null);
    """)

    print("++++++++++++++++++++++++++++++++++")


# Drop tables
def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")
    cur = _conn.cursor()
    cur.execute("DROP TABLE IF EXISTS driver;")
    cur.execute("DROP TABLE IF EXISTS bus;")
    cur.execute("DROP TABLE IF EXISTS stop;")
    cur.execute("DROP TABLE IF EXISTS stopdetails;")
    cur.execute("DROP TABLE IF EXISTS path_;")
    cur.execute("DROP TABLE IF EXISTS pathdetails;")
    cur.execute("DROP TABLE IF EXISTS route;")
    print("++++++++++++++++++++++++++++++++++")


# Populate tables
def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
    cur = _conn.cursor()

    # driver
    cur.execute("""
    INSERT INTO driver (d_busid, d_drivername, d_type, d_subid, d_subbusid, d_status, d_hours)
    VALUES
    (1, "DRIVER#01", "PRIMARY", 0, 0, "ABLE", 0.0),
    (2, "DRIVER#02", "PRIMARY", 0, 0, "ABLE", 0.0),
    (3, "DRIVER#03", "PRIMARY", 0, 0, "ABLE", 0.0),
    (4, "DRIVER#04", "PRIMARY", 0, 0, "ABLE", 0.0),
    (5, "DRIVER#05", "PRIMARY", 0, 0, "ABLE", 0.0),
    (6, "DRIVER#06", "PRIMARY", 0, 0, "ABLE", 0.0),
    (7, "DRIVER#07", "PRIMARY", 0, 0, "ABLE", 0.0),
    (8, "DRIVER#08", "PRIMARY", 0, 0, "ABLE", 0.0),
    (9, "DRIVER#09", "PRIMARY", 0, 0, "ABLE", 0.0),
    (10, "DRIVER#10", "SECONDARY", 0, 0, "ABLE", 0.0),
    (11, "DRIVER#11", "SECONDARY", 0, 0, "ABLE", 0.0),
    (12, "DRIVER#12", "SECONDARY", 0, 0, "ABLE", 0.0),
    (13, "DRIVER#13", "SECONDARY", 0, 0, "ABLE", 0.0),
    (14, "DRIVER#14", "SECONDARY", 0, 0, "ABLE", 0.0),
    (15, "DRIVER#15", "SECONDARY", 0, 0, "ABLE", 0.0),
    (16, "DRIVER#16", "SECONDARY", 0, 0, "ABLE", 0.0),
    (17, "DRIVER#17", "SECONDARY", 0, 0, "ABLE", 0.0),
    (18, "DRIVER#18", "SECONDARY", 0, 0, "ABLE", 0.0);
    """)

    # bus
    cur.execute("""
    INSERT INTO bus (b_busname, b_condition, b_gas)
    VALUES
    ("BUS#01", "FUNCTIONAL", 60),
    ("BUS#02", "FUNCTIONAL", 60),
    ("BUS#03", "FUNCTIONAL", 60),
    ("BUS#04", "FUNCTIONAL", 60),
    ("BUS#05", "FUNCTIONAL", 60),
    ("BUS#06", "FUNCTIONAL", 60),
    ("BUS#07", "FUNCTIONAL", 60),
    ("BUS#08", "FUNCTIONAL", 60),
    ("BUS#09", "FUNCTIONAL", 60),
    ("BUS#10", "FUNCTIONAL", 60),
    ("BUS#11", "FUNCTIONAL", 60),
    ("BUS#12", "FUNCTIONAL", 60);
    """)

    # stop
    cur.execute("""
    INSERT INTO stop (s_locationx, s_locationy, s_stopname)
    VALUES
    (0.0, 0.2, "STOP#01"),
    (0.1, 0.2, "STOP#02"),
    (0.2, 0.2, "STOP#03"),
    (0.2, 0.3, "STOP#04"),
    (0.2, 0.1, "STOP#05"),
    (0.2, 0.0, "STOP#06"),
    (0.3, 0.0, "STOP#07"),
    (0.3, 0.1, "STOP#08"),
    (0.3, 0.4, "STOP#09"),
    (0.0, 0.4, "STOP#10"),
    (0.0, 0.5, "STOP#11"),
    (0.4, 0.5, "STOP#12"),
    (0.4, 0.4, "STOP#13"),
    (0.5, 0.4, "STOP#14"),
    (0.5, 0.3, "STOP#15"),
    (0.4, 0.3, "STOP#16"),
    (0.4, 0.1, "STOP#17"),
    (0.1, 0.1, "STOP#18"),
    (0.1, 0.0, "STOP#19"),
    (0.0, 0.0, "STOP#20");
    """)

    # stopdetails
    # Full route
    cur.execute("""
    INSERT INTO stopdetails (sd_routetype, sd_stopid, sd_stopno)
    VALUES
    (1, 1, 0),
    (1, 2, 1),
    (1, 3, 2),
    (1, 4, 5),
    (1, 5, 6),
    (1, 6, 7),
    (1, 7, 8),
    (1, 8, 9),
    (1, 9, 10),
    (1, 10, 11),
    (1, 12, 13),
    (1, 13, 14),
    (1, 14, 15),
    (1, 15, 16),
    (1, 16, 17),
    (1, 17, 18),
    (1, 8, 19),
    (1, 5, 20),
    (1, 18, 21),
    (1, 19, 22),
    (1, 20, 23),
    (1, 1, 24);
    """)

    # Half route A
    cur.execute("""
    INSERT INTO stopdetails (sd_routetype, sd_stopid, sd_stopno)
    VALUES
    (2, 6, 0),
    (2, 7, 1),
    (2, 8, 2),
    (2, 5, 3),
    (2, 18, 4),
    (2, 19, 5),
    (2, 20, 6),
    (2, 1, 7),
    (2, 2, 8),
    (2, 3, 9),
    (2, 4, 10),
    (2, 5, 11),
    (2, 6, 12);
    """)

    # Half route A
    cur.execute("""
    INSERT INTO stopdetails (sd_routetype, sd_stopid, sd_stopno)
    VALUES
    (3, 15, 0),
    (3, 16, 1),
    (3, 17, 2),
    (3, 8, 3),
    (3, 9, 4),
    (3, 10, 5),
    (3, 11, 6),
    (3, 12, 7),
    (3, 13, 8),
    (3, 14, 9),
    (3, 15, 10);
    """)

    # path
    cur.execute("""
    INSERT INTO path_ (p_startid, p_endid, p_pathlength, p_gasusage)
    VALUES
    (1, 2, 0.1, 0.0133),
    (2, 3, 0.1, 0.0133),
    (3, 4, 0.1, 0.0133),
    (4, 5, 0.2, 0.0266),
    (5, 6, 0.1, 0.0133),
    (6, 7, 0.1, 0.0133),
    (7, 8, 0.1, 0.0133),
    (8, 9, 0.3, 0.0400),
    (9, 10, 0.3, 0.0400),
    (10, 11, 0.1, 0.0133),
    (11, 12, 0.4, 0.0533),
    (12, 13, 0.1, 0.0133),
    (13, 14, 0.1, 0.0133),
    (14, 15, 0.1, 0.0133),
    (15, 16, 0.1, 0.0133),
    (16, 17, 0.2, 0.0266),
    (17, 8, 0.1, 0.0133),
    (8, 5, 0.1, 0.0133),
    (5, 18, 0.1, 0.0133),
    (18, 19, 0.1, 0.0133),
    (19, 20, 0.1, 0.0133),
    (20, 1, 0.2, 0.0266);
    """)

    # path
    # Full route
    cur.execute("""
    INSERT INTO pathdetails (pd_routetype, pd_pathid, pd_pathno)
    VALUES
    (1, 1, 1),
    (1, 2, 2),
    (1, 3, 3),
    (1, 4, 4),
    (1, 5, 5),
    (1, 6, 6),
    (1, 7, 7),
    (1, 8, 8),
    (1, 9, 9),
    (1, 10, 10),
    (1, 11, 11),
    (1, 12, 12),
    (1, 13, 13),
    (1, 14, 14),
    (1, 15, 15),
    (1, 16, 16),
    (1, 17, 17),
    (1, 18, 18),
    (1, 19, 19),
    (1, 20, 20),
    (1, 21, 21),
    (1, 22, 22);
    """)

    # Half route A
    cur.execute("""
    INSERT INTO pathdetails (pd_routetype, pd_pathid, pd_pathno)
    VALUES
    (2, 6, 1),
    (2, 7, 2),
    (2, 18, 3),
    (2, 19, 4),
    (2, 20, 5),
    (2, 21, 6),
    (2, 22, 7),
    (2, 1, 8),
    (2, 2, 9),
    (2, 3, 10),
    (2, 4, 11),
    (2, 5, 12);
    """)

    # Half route B
    cur.execute("""
    INSERT INTO pathdetails (pd_routetype, pd_pathid, pd_pathno)
    VALUES
    (3, 15, 1),
    (3, 16, 2),
    (3, 17, 3),
    (3, 8, 4),
    (3, 9, 5),
    (3, 10, 6),
    (3, 11, 7),
    (3, 12, 8),
    (3, 13, 9),
    (3, 14, 10);
    """)

    # route
    # Monday full route 6-8
    cur.execute("""
    INSERT INTO route (r_busid, r_routename, r_routetype, r_starttime, r_endtime, r_day)
    VALUES
    (1, "MONDAY FULL ROUTE#01", 1, "6:00", "6:15", "MONDAY"),
    (1, "MONDAY FULL ROUTE#02", 1, "6:15", "6:30", "MONDAY"),
    (1, "MONDAY FULL ROUTE#03", 1, "6:30", "6:45", "MONDAY"),
    (1, "MONDAY FULL ROUTE#04", 1, "6:45", "7:00", "MONDAY"),
    (1, "MONDAY FULL ROUTE#05", 1, "7:00", "7:15", "MONDAY"),
    (1, "MONDAY FULL ROUTE#06", 1, "7:15", "7:30", "MONDAY"),
    (1, "MONDAY FULL ROUTE#07", 1, "7:30", "7:45", "MONDAY");
    """)

    # Monday full route 8-10
    cur.execute("""
    INSERT INTO route (r_busid, r_routename, r_routetype, r_starttime, r_endtime, r_day)
    VALUES
    (2, "MONDAY FULL ROUTE#08", 1, "8:00", "8:15", "MONDAY"),
    (2, "MONDAY FULL ROUTE#09", 1, "8:15", "8:30", "MONDAY"),
    (2, "MONDAY FULL ROUTE#10", 1, "8:30", "8:45", "MONDAY"),
    (2, "MONDAY FULL ROUTE#11", 1, "8:45", "9:00", "MONDAY"),
    (2, "MONDAY FULL ROUTE#12", 1, "9:00", "9:15", "MONDAY"),
    (2, "MONDAY FULL ROUTE#13", 1, "9:15", "9:30", "MONDAY"),
    (2, "MONDAY FULL ROUTE#14", 1, "9:30", "9:45", "MONDAY");
    """)

    # Monday full route 10-12
    cur.execute("""
    INSERT INTO route (r_busid, r_routename, r_routetype, r_starttime, r_endtime, r_day)
    VALUES
    (3, "MONDAY FULL ROUTE#15", 1, "10:00", "10:15", "MONDAY"),
    (3, "MONDAY FULL ROUTE#16", 1, "10:15", "10:30", "MONDAY"),
    (3, "MONDAY FULL ROUTE#17", 1, "10:30", "10:45", "MONDAY"),
    (3, "MONDAY FULL ROUTE#18", 1, "10:45", "11:00", "MONDAY"),
    (3, "MONDAY FULL ROUTE#19", 1, "11:00", "11:15", "MONDAY"),
    (3, "MONDAY FULL ROUTE#20", 1, "11:15", "11:30", "MONDAY"),
    (3, "MONDAY FULL ROUTE#21", 1, "11:30", "11:45", "MONDAY");
    """)

    # Monday full route 12-14
    cur.execute("""
    INSERT INTO route (r_busid, r_routename, r_routetype, r_starttime, r_endtime, r_day)
    VALUES
    (4, "MONDAY FULL ROUTE#22", 1, "12:00", "12:15", "MONDAY"),
    (4, "MONDAY FULL ROUTE#23", 1, "12:15", "12:30", "MONDAY"),
    (4, "MONDAY FULL ROUTE#24", 1, "12:30", "12:45", "MONDAY"),
    (4, "MONDAY FULL ROUTE#25", 1, "12:45", "13:00", "MONDAY"),
    (4, "MONDAY FULL ROUTE#26", 1, "13:00", "13:15", "MONDAY"),
    (4, "MONDAY FULL ROUTE#27", 1, "13:15", "13:30", "MONDAY"),
    (4, "MONDAY FULL ROUTE#28", 1, "13:30", "13:45", "MONDAY");
    """)

    # Monday full route 14-16
    cur.execute("""
    INSERT INTO route (r_busid, r_routename, r_routetype, r_starttime, r_endtime, r_day)
    VALUES
    (5, "MONDAY FULL ROUTE#29", 1, "14:00", "14:15", "MONDAY"),
    (5, "MONDAY FULL ROUTE#30", 1, "14:15", "14:30", "MONDAY"),
    (5, "MONDAY FULL ROUTE#31", 1, "14:30", "14:45", "MONDAY"),
    (5, "MONDAY FULL ROUTE#32", 1, "14:45", "15:00", "MONDAY"),
    (5, "MONDAY FULL ROUTE#33", 1, "15:00", "15:15", "MONDAY"),
    (5, "MONDAY FULL ROUTE#34", 1, "15:15", "15:30", "MONDAY"),
    (5, "MONDAY FULL ROUTE#35", 1, "15:30", "15:45", "MONDAY");
    """)

    # Monday full route 16-18
    cur.execute("""
    INSERT INTO route (r_busid, r_routename, r_routetype, r_starttime, r_endtime, r_day)
    VALUES
    (6, "MONDAY FULL ROUTE#36", 1, "16:00", "16:15", "MONDAY"),
    (6, "MONDAY FULL ROUTE#37", 1, "16:15", "16:30", "MONDAY"),
    (6, "MONDAY FULL ROUTE#38", 1, "16:30", "16:45", "MONDAY"),
    (6, "MONDAY FULL ROUTE#39", 1, "16:45", "17:00", "MONDAY"),
    (6, "MONDAY FULL ROUTE#40", 1, "17:00", "17:15", "MONDAY"),
    (6, "MONDAY FULL ROUTE#41", 1, "17:15", "17:30", "MONDAY"),
    (6, "MONDAY FULL ROUTE#42", 1, "17:30", "17:45", "MONDAY");
    """)

    # Monday full route 18-20
    cur.execute("""
    INSERT INTO route (r_busid, r_routename, r_routetype, r_starttime, r_endtime, r_day)
    VALUES
    (7, "MONDAY FULL ROUTE#43", 1, "18:00", "18:15", "MONDAY"),
    (7, "MONDAY FULL ROUTE#44", 1, "18:15", "18:30", "MONDAY"),
    (7, "MONDAY FULL ROUTE#45", 1, "18:30", "18:45", "MONDAY"),
    (7, "MONDAY FULL ROUTE#46", 1, "18:45", "19:00", "MONDAY"),
    (7, "MONDAY FULL ROUTE#47", 1, "19:00", "19:15", "MONDAY"),
    (7, "MONDAY FULL ROUTE#48", 1, "19:15", "19:30", "MONDAY"),
    (7, "MONDAY FULL ROUTE#49", 1, "19:30", "19:45", "MONDAY");
    """)

    # Monday full route 20-22
    cur.execute("""
    INSERT INTO route (r_busid, r_routename, r_routetype, r_starttime, r_endtime, r_day)
    VALUES
    (8, "MONDAY FULL ROUTE#50", 1, "20:00", "20:15", "MONDAY"),
    (8, "MONDAY FULL ROUTE#51", 1, "20:15", "20:30", "MONDAY"),
    (8, "MONDAY FULL ROUTE#52", 1, "20:30", "20:45", "MONDAY"),
    (8, "MONDAY FULL ROUTE#53", 1, "20:45", "21:00", "MONDAY"),
    (8, "MONDAY FULL ROUTE#54", 1, "21:00", "21:15", "MONDAY"),
    (8, "MONDAY FULL ROUTE#55", 1, "21:15", "21:30", "MONDAY"),
    (8, "MONDAY FULL ROUTE#56", 1, "21:30", "21:45", "MONDAY");
    """)

    # Monday full route 22-24
    cur.execute("""
    INSERT INTO route (r_busid, r_routename, r_routetype, r_starttime, r_endtime, r_day)
    VALUES
    (9, "MONDAY FULL ROUTE#57", 1, "22:00", "22:15", "MONDAY"),
    (9, "MONDAY FULL ROUTE#58", 1, "22:15", "22:30", "MONDAY"),
    (9, "MONDAY FULL ROUTE#59", 1, "22:30", "22:45", "MONDAY"),
    (9, "MONDAY FULL ROUTE#60", 1, "22:45", "23:00", "MONDAY"),
    (9, "MONDAY FULL ROUTE#61", 1, "23:00", "23:15", "MONDAY"),
    (9, "MONDAY FULL ROUTE#62", 1, "23:15", "23:30", "MONDAY"),
    (9, "MONDAY FULL ROUTE#63", 1, "23:30", "23:45", "MONDAY");
    """)

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    try:
        sql = _conn.execute("""
        SELECT r_starttime, r_endtime
        FROM route
        
        WHERE r_routetype = 1
        """)
        table = sql.fetchall()

        print(table)
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"Checkpoint3-dbase.sqlite3"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateTable(conn)

        Q1(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()