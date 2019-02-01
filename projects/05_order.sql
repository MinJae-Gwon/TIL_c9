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

--2.1.
INSERT INTO movies("영화코드", "영화이름", "관람등급", "감독", "개봉 연도", "누적관객수", "상영시간", "제작국가", "장르")                         
VALUES(20182530, "극한직업", "15세이상관람가", "이병헌","20190123", 313846, 111, "한국", "코미디");

--2.2
DELETE FROM movies WHERE 영화코드=20040521;

--2.3.
SELECT * FROM movies WHERE 영화코드=20185124;

UPDATE movies SET 감독='없음' WHERE 영화코드=20185124 AND 감독="";


--3.1
SELECT 영화이름 FROM movies WHERE 상영시간>=150
--3.2
SELECT 영화이름, 영화코드 FROM movies WHERE 장르="애니메이션"
--3.3
SELECT 영화이름 FROM movies WHERE 제작국가="덴마크" AND 장르="애니메이션";
--3.4
SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수>1000000 AND 관람등급="청소년관람불가";
--3.5
SELECT * FROM movies WHERE 20000101<=개봉연도 AND 개봉연도<=20091231;
--3.6
SELECT DISTINCT 장르 FROM movies; 

--4.1
SELECT SUM(누적관객수) FROM movies;
--4.2
SELECT 영화이름, MAX(누적관객수) FROM  movies;
--4.3
SELECT 장르, MIN(상영시간) FROM movies;
--4.4
SELECT AVG(누적관객수) FROM movies WHERE 제작국가="한국";
--4.5
SELECT COUNT(영화이름) FROM movies WHERE 관람등급="청소년관람불가";
--4.6
SELECT COUNT(영화이름) FROM movies WHERE 상영시간>=100 AND 장르="애니메이션";

--5.1
SELECT * FROM movies ORDER BY 누적관객수 DESC LIMIT 5;
--5.2
SELECT * FROM movies WHERE 장르="애니메이션" ORDER BY 제작국가 ASC , 누적관객수 DESC LIMIT 10;
--5.3
SELECT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10;