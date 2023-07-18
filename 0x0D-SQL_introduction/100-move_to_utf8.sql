-- Convert hbtn_0c_0, hbtn_0c_0.first_table, hbtn_0c_0.first_table.name
-- to UTF-8  (utf8mb4, collate utf8mb4_unicode_ci) 

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
