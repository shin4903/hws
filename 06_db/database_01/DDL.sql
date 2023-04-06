CREATE TABLE contacts (
name TEXT NOT NULL,
age INTEGER NOT NULL,
email TEXT NOT NULL UNIQUE
);

ALTER TABLE contacts RENAME TO new_contacts;

ALTER TABLE new_contacts RENAME TO contacts;
ALTER TABLE contacts ADD COLUMN test TEXT NULL;
ALTER TABLE contacts DROP COLUMN test;



