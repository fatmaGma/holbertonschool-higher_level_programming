-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa).
-- If the database hbtn_0d_usa already exists, the script should not fail.
-- If the table states already exists, the script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE  IF NOT EXISTS hbtn_0d_usa.states(
	PRIMARY KEY(id),
	id INT NOT NULL AUTO_INCREMENT, 
	name VARCHAR(256) NOT NULL);
