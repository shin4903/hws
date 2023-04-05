CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
address TEXT NOT NULL,
phoneNumber TEXT NOT NULL,
balance INTEGER NOT NULL
);

-- 실습 1-1. 
-- 이름, 나이, 잔고를 나이가 어린순으로, 나이가 같으면 계좌 잔고가 많은 순으로
-- sqlite에서 .mode column을 통해 컬럼별로 정리하여 데이터 확인 가능.
SELECT first_name, age, balance  FROM users 
ORDER BY age, balance DESC;

-- 실습 1-2.
-- 이름과 나이를 이름의 오름차순, 나이의 내림차순
SELECT first_name, age FROM users 
ORDER BY first_name, age DESC;

-- 실습 1-3-1
-- 이름이 '건우'이고, 지역이 '경기도'인 정보를 이름과 지역만 출력
SELECT first_name, address FROM users
WHERE first_name = '건우' AND address = '경기도';

-- 실습 1-3-2
-- 경기도, 강원도에서 살지 않는 사람 중, 나이가 20살 이상 30살 이하를 나이기준 오름차순
SELECT first_name, address, age FROM users 
WHERE address NOT IN ('경기도', '강원도') AND age BETWEEN 20 AND 30
ORDER BY age;

-- 실습 1-4
-- 전화번호 중간 4자리가 51로 시작하고 지역이 '서울'이 아닌 사람들의 이름, 전화번호, 지역
-- table 생성시 phoneNumber로 컬럼을 생성하였음 
-- 조회시에 phone으로 표기될 수 있도록 AS 설정
-- address 역시 country가 될 수 있도록 AS 설정
-- phone의 경우, wild card %와 _를 사용하여 진행
  -- %의 경우, 해당 자리에 0개 이상의 값이 올 수 있음 (값이 없을 수도 있음)
  -- _의 경우, 해당 자리에 반드시 한개의 값이 와야함
    -- 따라서 `%-51__-%` 형식으로 작성시 `-51` 앞에는 아무값이나 올 수 있고,
    -- `-51__` 부분의 와일드카드 __으로 인해 51 뒤에는 반드시 2글자가 와야함
    -- `-51__-%` 에서 __ 다음의 - 는 일반 문자열이 오고, 그 뒤 %는 뒤에 아무 글자나 올 수 있음을 의미한다.
SELECT first_name, phoneNumber AS phone, address AS country
FROM users
WHERE phone LIKE '%-51__-%'
AND country != '서울';

-- 실습 1-5
-- 나이가 어린순으로 3번쨰 페이지(페이지당 20개, 즉 41번 데이터부터 20개의 데이터) 조회
-- 제대로 41번 부터 60번까지 나오는지 확인하기 위해 rowid와 이름을 출력
-- LIMIT으로 20개의 데이터로 데이터 조회수 제한,
-- OFFSET을 사용하여 앞자리 40개를 제외
SELECT rowid, first_name FROM users
LIMIT 20 OFFSET 40;