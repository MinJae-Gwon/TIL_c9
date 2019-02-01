CREATE TABLE movies (
    '영화코드' INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' TEXT,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);
-- import boxoffice csv
.mode csv
.import boxoffice.csv movies
.headers on
.mode column

SELECT * FROM movies;

--2.
INSERT INTO movies("영화코드", "영화이름", "관람등급", "감독", "개봉 연도", "누적관객수", "상영시간", "제작국가", "장르")                         
VALUES(20182530, "극한직업", "15세이상관람가", "이병헌","20190123", 313846, 111, "한국", "코미디");

DELETE FROM movies WHERE 영화코드=20040521;

--3.
SELECT * FROM movies WHERE 영화코드=20185124;

UPDATE movies SET 감독='없음' WHERE 영화코드=20185124 AND 감독="";


