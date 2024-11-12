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
	s_routeid		decimal(9,0) not null,
	s_stopname		char(100) not null,
	s_stopnumber	decimal(9,0) not null
);

CREATE TABLE route(
	r_routeid		decimal(9,0) not null,
	r_busid			decimal(9,0) not null,
	r_routename		char(100) not null,
	r_starttime		char(100) not null,
	r_endtime		char(100) not null,
	r_routeday		char(100) not null
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
	rc_clearange	char(100) not null,
	rc_comments		char(100) not null
);

INSERT INTO driver (d_driverid, d_busid, d_subbusid, d_drivername, d_experience, d_status)
	SELECT 1,
	1,
	2
	"DRIVER#001"
	"NEW"
	"ABLE";

INSERT INTO bus (b_busid, b_condition, b_gas)
	SELECT 1,
	"FUNCTIONAL",
	60;

INSERT INTO bus (b_busid, b_condition, b_gas)
	SELECT 2,
	"FUNCTIONAL",
	60;

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
DROP TABLE IF EXISTS path_;
DROP TABLE IF EXISTS roadconditions;