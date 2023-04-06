CREATE TABLE test (
name TEXT NOT NULL,
age iIT CHECK (typeof(age) = 'integer')
);

INSERT INTO test COLUMN (name, age)
VALUES ('test', 4);

INSERT INTO test (name, age)
VALUES ('test', 5);