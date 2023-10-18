-- This script creates a table first_table in current db
-- and it does not fail if table exists
CREATE TABLE IF NOT EXISTS first_table (id INT,
name VARCHAR(256));
