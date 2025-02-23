-- creates the database hbnb_dev_db in MySQL server
-- create user hbnb_dev with pwd hbnb_dev_pwd
-- grant hbnb_dev select on performance_schema
-- grant all privileges on hbnb_dev_db
-- only if database doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
