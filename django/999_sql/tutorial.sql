-- DDL

CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
);

DROP TABLE classmates;


CREATE TABLE classmates (
  name TEXT,
  age INTEGER,
  address TEXT
);

CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);


-- DML (CRUD)
-- CREATE

INSERT INTO classmates (name, age)
VALUES ('홍길동', 23);

INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '대전');

INSERT INTO classmates
VALUES ('홍길동', 23, '대전');

INSERT INTO classmates 
VALUES('홍길동',30,'서울'),('김철수',23,'대전'),('박나래',23,'광주'),('이요셉',33,'구미');

insert into classmates
values(address='seoul', age=20, name='홍길동');

insert into classmates (address, age, name)
values('seoul', 20, '홍길동');

INSERT INTO classmates VALUES('홍길동', 20, 'seoul');
-- SELECT