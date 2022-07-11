--1.
CREATE TABLE employee(
	id INTEGER,
	name VARCHAR(50),
	birthday DATE,
	email VARCHAR(100)
);

--3.
UPDATE employee
SET name='Bedirhan',
    email='bedirhancebi@gmail.com'
WHERE id=1;

UPDATE employee
SET name='Ali'
WHERE name='Etti';  
 
UPDATE employee
SET birthday='2012-09-22'
WHERE name='Brody';

UPDATE employee
SET birthday='2012-09-22',
	name='Martin',
	email='qwerty@yahoo.com'
WHERE name='Rosy';

UPDATE employee
SET 
	name='Martin Eden'
WHERE name='Gage';

--4.
DELETE FROM employee
WHERE birthday='1973-09-26';

DELETE FROM employee
WHERE id>45;

DELETE FROM employee
WHERE email='velmars@blog.com';

DELETE FROM employee
WHERE name='Pauly';

DELETE FROM employee
WHERE id=17;


