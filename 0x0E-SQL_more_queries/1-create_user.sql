-- creates a MySQL server user user_0d_1.
-- server should have all privileges on your MySQL server
-- The user_0d_1 password is set by user_0d_1_pwd
-- If the user user_0d_1 already exists, script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
