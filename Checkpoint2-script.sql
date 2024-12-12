.headers on
CREATE TABLE driver(
	d_driverid		decimal(9,0) not null,
	d_busid			decimal(9,0) not null,
	d_subbusid		decimal(9,0) not null,
	d_drivername	char(100) not null,
	d_experience	char(100) not null,
	d_status		char(100) not null
);

CREATE TABLE bus(
	b_busid			decimal(9,0) not null,
	b_condition		char(100) not null,
	b_gas			decimal(9,0) not null
);

CREATE TABLE stop(
	s_stopid		decimal(9,0) not null,
	s_locationx		decimal(9,0) not null,
	s_locationy		decimal(9,0) not null,
	s_stopname		char(100) not null
);

CREATE TABLE route(
	r_routeid		decimal(9,0) not null,
	r_busid			decimal(9,0) not null,
	r_routename		char(100) not null,
	r_starttime		char(100) not null,
	r_endtime		char(100) not null,
	r_routeday		char(100) not null
);

CREATE TABLE routedetails(
	rd_routeid		decimal(9,0) not null,
	rd_stopid		decimal(9,0) not null,
	rd_stopno		decimal(9,0) not null
);

CREATE TABLE path_(
	p_pathid		decimal(9,0) not null,
	p_startid		decimal(9,0) not null,
	p_endid			decimal(9,0) not null,
	p_pathlength	decimal(9,0) not null,
	p_gasusage		decimal(9,0) not null
);

CREATE TABLE roadconditions(
	rc_pathid		decimal(9,0) not null,
	rc_clearance	char(100) not null,
	rc_comments		char(300) not null
);

INSERT INTO driver (d_driverid, d_busid, d_subbusid, d_drivername, d_experience, d_status)
	SELECT 1,
	1,
	2,
	"DRIVER#001",
	"NEW",
	"ABLE";

INSERT INTO driver (d_driverid, d_busid, d_subbusid, d_drivername, d_experience, d_status)
	SELECT 2,
	2,
	1,
	"DRIVER#002",
	"VETERAN",
	"ABLE";

INSERT INTO bus (b_busid, b_condition, b_gas)
	SELECT 1,
	"FUNCTIONAL",
	60;

INSERT INTO bus (b_busid, b_condition, b_gas)
	SELECT 2,
	"FUNCTIONAL",
	45;

INSERT INTO stop (s_stopid, s_locationx, s_locationy, s_stopname)
	SELECT 1,
	0,
	0,
	"STOP#001";

INSERT INTO stop (s_stopid, s_locationx, s_locationy, s_stopname)
	SELECT 2,
	0.25,
	0.25,
	"STOP#002";

INSERT INTO stop (s_stopid, s_locationx, s_locationy, s_stopname)
	SELECT 3,
	0.75,
	0.25,
	"STOP#003";

INSERT INTO stop (s_stopid, s_locationx, s_locationy, s_stopname)
	SELECT 4,
	0.75,
	0.1,
	"STOP#004";

INSERT INTO stop (s_stopid, s_locationx, s_locationy, s_stopname)
	SELECT 5,
	0.25,
	0.1,
	"STOP#005";

INSERT INTO stop (s_stopid, s_locationx, s_locationy, s_stopname)
	SELECT 6,
	0.25,
	0,
	"STOP#005";

INSERT INTO route (r_routeid, r_busid, r_routename, r_starttime, r_endtime, r_routeday)
	SELECT 1,
	1,
	"ROUTE#001",
	"9:00",
	"9:30",
	"MONDAY";

INSERT INTO routedetails (rd_routeid, rd_stopid, rd_stopno)
	SELECT 1,
	1,
	1;

INSERT INTO routedetails (rd_routeid, rd_stopid, rd_stopno)
	SELECT 1,
	2,
	2;

INSERT INTO routedetails (rd_routeid, rd_stopid, rd_stopno)
	SELECT 1,
	3,
	3;

INSERT INTO routedetails (rd_routeid, rd_stopid, rd_stopno)
	SELECT 1,
	4,
	4;

INSERT INTO routedetails (rd_routeid, rd_stopid, rd_stopno)
	SELECT 1,
	5,
	5;

INSERT INTO routedetails (rd_routeid, rd_stopid, rd_stopno)
	SELECT 1,
	6,
	6;

INSERT INTO routedetails (rd_routeid, rd_stopid, rd_stopno)
	SELECT 1,
	1,
	7;

INSERT INTO path_ (p_pathid, p_startid, p_endid, p_pathlength, p_gasusage)
	SELECT 1,
	1,
	2,
	0.3546,
	0.047;

INSERT INTO path_ (p_pathid, p_startid, p_endid, p_pathlength, p_gasusage)
	SELECT 2,
	2,
	3,
	0.5,
	0.067;

INSERT INTO path_ (p_pathid, p_startid, p_endid, p_pathlength, p_gasusage)
	SELECT 3,
	3,
	4,
	0.15,
	0.02;

INSERT INTO path_ (p_pathid, p_startid, p_endid, p_pathlength, p_gasusage)
	SELECT 4,
	4,
	5,
	0.5,
	0.067;

INSERT INTO path_ (p_pathid, p_startid, p_endid, p_pathlength, p_gasusage)
	SELECT 5,
	5,
	6,
	0.1,
	0.013;

INSERT INTO path_ (p_pathid, p_startid, p_endid, p_pathlength, p_gasusage)
	SELECT 6,
	6,
	1,
	0.25,
	0.033;

INSERT INTO path_ (p_pathid, p_startid, p_endid, p_pathlength, p_gasusage)
	SELECT 7,
	2,
	5,
	0.15,
	0.02;

INSERT INTO roadconditions(rc_pathid, rc_clearance, rc_comments)
	SELECT 1,
	"CLEAR",
	"";

INSERT INTO roadconditions(rc_pathid, rc_clearance, rc_comments)
	SELECT 2,
	"CLEAR",
	"";

INSERT INTO roadconditions(rc_pathid, rc_clearance, rc_comments)
	SELECT 3,
	"CLEAR",
	"";

INSERT INTO roadconditions(rc_pathid, rc_clearance, rc_comments)
	SELECT 4,
	"BLOCKED",
	"Road under maintenance";

INSERT INTO roadconditions(rc_pathid, rc_clearance, rc_comments)
	SELECT 5,
	"CLEAR",
	"";

INSERT INTO roadconditions(rc_pathid, rc_clearance, rc_comments)
	SELECT 6,
	"CLEAR",
	"";

INSERT INTO roadconditions(rc_pathid, rc_clearance, rc_comments)
	SELECT 7,
	"CLEAR",
	"";

SELECT *
FROM driver;

UPDATE driver
SET d_experience = "RETIRED",
	d_status = "RETIRED"
WHERE d_driverid = 2;

SELECT *
FROM driver;

SELECT *
FROM roadconditions;

UPDATE roadconditions
SET rc_clearance = "CLEAR",
	rc_comments = "Maintenance complete"
WHERE rc_pathid = 4;

SELECT *
FROM roadconditions;

DELETE FROM roadconditions
WHERE rc_pathid = 7;

SELECT *
FROM roadconditions;

SELECT *
FROM bus;

UPDATE bus
SET b_gas = b_gas - 0.26728
WHERE b_busid = 1;

SELECT *
FROM bus;

UPDATE roadconditions(
SET p_pathlength = '1', p_gasusage = '2'
WHERE rc_pathid = '2'
;)

UPDATE driver(
SET d_driverid = b_busid
WHERE d_drivername = '1'
;)

DROP TABLE IF EXISTS driver;
DROP TABLE IF EXISTS bus;
DROP TABLE IF EXISTS stop;
DROP TABLE IF EXISTS route;
DROP TABLE IF EXISTS routedetails;
DROP TABLE IF EXISTS path_;
DROP TABLE IF EXISTS roadconditions;