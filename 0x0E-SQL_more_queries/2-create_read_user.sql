-- This script creates the database hbtn_0d_2 and the user user_0d_2.
-- The user user_0d_2 will have only SELECT privilege on the database hbtn_0d_2.
-- The password for user_0d_2 should be set to user_0d_2_pwd.
-- If the database hbtn_0d_2 already exists, this script will not fail.
-- If the user user_0d_2 already exists, this script will not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
