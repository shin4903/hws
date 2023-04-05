-- 테이블 만들기
CREATE TABLE contacts (
name TEXT NOT NULL,
age INTEHER NOT NULL,
email TEXT NOT NULL UNIQUE
);


-- 테이블 이름 변경
ALTER TABLE contacts RENAME TO new_contacts;

-- 테이블 컬럼 이름 변경
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

-- 테이블에 컬럼 추가 (NULL까지만 하면 값이 없기때문에 오류가 나서 DEFAULT로 값 추가)
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';

-- 테이블 컬럼 삭제 (버전 이슈 때문에 터미널 창에서 sqlite켜서 직접 SQL 입력)
ALTER TABLE new_contacts DROP COLUMN address;

-- 테이블 삭제
DROP TABLE new_contacts;
