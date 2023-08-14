-- Create a new db hbtn_0d_2 with table states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,

	PRIMARY KEY(id)
);