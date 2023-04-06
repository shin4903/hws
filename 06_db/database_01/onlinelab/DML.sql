CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
address TEXT NOT NULL,
phoneNumber TEXT NOT NULL,
balance INTEGER NOT NULL
);

INSERT INTO users (
first_name, last_name, age, address, phoneNumber, 
balance)
VALUES (
'구현', '김', 20, '창원', '010-1234-1234', 10);

SELECT * FROM users;

-- 이름, 나이, 재산 만 users 테이블에서 가지고 온다.
SELECT first_name, age, balance FROM users;

-- 정렬 ORDER BY column_name - 기본은 오름차순
SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;

-- 내림차순 DESC
SELECT first_name, age, balance FROM users
ORDER BY age DESC;

SELECT first_name, age, balance FROM users
ORDER BY first_name;

-- 이름이 건우인 사람의 이름과 나이만 표기
SELECT first_name, age FROM users
WHERE first_name = '건우';

-- 이름이 가 - 바 사이에 들어가는 사람 표기
SELECT first_name, age FROM users
WHERE first_name BETWEEN '가' AND '바'
ORDER BY first_name;
