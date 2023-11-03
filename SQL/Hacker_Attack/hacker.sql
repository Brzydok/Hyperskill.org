-- write your queries here
CREATE TABLE "person"(
  "person_id" VARCHAR(9) PRIMARY KEY,
  "full_name" TEXT,
  "address" TEXT,
  "building_number" TEXT,
  "phone_number" TEXT
);

.mode csv
.import --skip 1 person.csv person
.mode column

CREATE TABLE "teacher"(
"person_id" VARCHAR(9) PRIMARY KEY,
"class_code" TEXT
);

.mode csv
.import --skip 1 teacher.csv teacher
.mode column

CREATE TABLE "student"(
"person_id" VARCHAR(9) PRIMARY KEY,
"grade_code" TEXT
);

INSERT INTO student(person_id)
SELECT person.person_id FROM person
LEFT JOIN teacher ON teacher.person_id = person.person_id
WHERE teacher.person_id IS NULL;

CREATE TABLE "score1"(
"person_id" VARCHAR(9),
"score" INTEGER
);

CREATE TABLE "score2"(
"person_id" VARCHAR(9),
"score" INTEGER
);

CREATE TABLE "score3"(
"person_id" VARCHAR(9),
"score" INTEGER
);

.mode csv
.import --skip 1 score1.csv score1
.import --skip 1 score2.csv score2
.import --skip 1 score3.csv score3
.mode column

CREATE TABLE "score"(
"person_id" VARCHAR(9),
"score" INTEGER
);

INSERT INTO score("person_id", "score")
SELECT "person_id", "score" 
FROM score1
UNION ALL
SELECT "person_id", "score" 
FROM score2
UNION ALL
SELECT "person_id", "score" 
FROM score3;

DROP TABLE score1;
DROP TABLE score2;
DROP TABLE score3;

UPDATE student
    SET grade_code = 'GD-09'
    WHERE 
        person_id NOT IN (SELECT person_id FROM score);

UPDATE student
    SET grade_code = 'GD-10'
    WHERE
        person_id IN 
            (SELECT person_id FROM score GROUP BY person_id HAVING COUNT(score) = 1);

UPDATE student
    SET grade_code = 'GD-11'
    WHERE
        person_id IN 
            (SELECT person_id FROM score GROUP BY person_id HAVING COUNT(score) = 2);

UPDATE student
    SET grade_code = 'GD-12'
    WHERE 
        person_id IN 
            (SELECT person_id FROM score GROUP BY person_id HAVING COUNT(score) = 3);

SELECT person_id, ROUND(AVG(score), 2) as "avg_score" 
FROM 
    score
WHERE 
    person_id IN (SELECT person_id FROM student WHERE grade_code = "GD-12")
GROUP BY
    person_id
ORDER BY 
    avg_score DESC;
