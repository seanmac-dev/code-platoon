DROP TABLE IF EXISTS students;
CREATE TABLE students(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    birth_year INT,
    birth_month VARCHAR(3),
    birthday INT,
    grade INT,
    address_id INT
);

INSERT INTO students(first_name, last_name, birth_year, birth_month, birthday, grade, address_id) VALUES
('Tianna', 'Lowe', 1976, 'JUL', 02, 93, 1),
('Elda', 'Sipes', 1983, 'JAN', 03, 74, 2),
('Jed', 'Kunde', 1902, 'APR', 21, 68, 3),
('Leopold', 'Towne', 1960, 'DEC', 30, 84, 4),
('Andre', 'Rohan', 2001, 'NOV', 12, 99, 5);

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses(
    id serial PRIMARY KEY,
    line_1 VARCHAR,
    city VARCHAR,
    states VARCHAR,
    zipcode INT
);

INSERT INTO addresses(line_1, city, states, zipcode) VALUES
('6232 Guiseppe Courts', 'Jamartown', 'Maryland', 49028),
('704 Cecil Mountain', 'West Jon', 'South Dakota', 91578),
('41613 Huel Ranch', 'Loycefort', 'Florida', 12109),
('1397 Braden Shoals', 'New Karine', 'New York', 13913);
SELECT * FROM addresses;
-- SELECT * FROM students;

-- SELECT MAX(grade) from students;
-- SELECT first_name, last_name, grade from students WHERE grade=(SELECT MAX(grade) from students);

-- SELECT first_name, last_name, grade from students WHERE grade=(SELECT MIN(grade) from students);

-- SELECT SUM(grade) from students;
-- SELECT AVG(grade) from students;

-- SELECT * FROM students WHERE first_name = 'Leopold';
-- SELECT * FROM students WHERE grade > 70;

-- SELECT * FROM students WHERE first_name LIKE 'T%' AND grade > 50;

-- SELECT * FROM students WHERE grade > 69 ORDER BY first_name ASC;

-- SELECT * FROM students INNER JOIN addresses ON students.address_id = addresses.id;

-- SELECT students.id, students.first_name, students.last_name, students.birth_year, students.address_id, addresses.line_1, addresses.city, addresses.states, addresses.zipcode FROM students LEFT JOIN addresses ON students.address_id = addresses.id;
-- Everyone gets an A!
UPDATE addresses SET states='Alaska' WHERE id = 2;
SELECT * FROM addresses;