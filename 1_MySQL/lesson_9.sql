-- Практическое задание по теме “Транзакции, переменные, представления”
-- В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
-- Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.

-- У меня нет БД sample, если не возражаете, буду использовать БД test1. 

START TRANSACTION;
INSERT INTO test1.users SELECT * FROM shop.users WHERE id = 1;
DELETE FROM shop.users WHERE id = 1;
COMMIT;


-- Создайте представление, которое выводит название name товарной позиции из таблицы products и 
-- соответствующее название каталога name из таблицы catalogs.

CREATE OR REPLACE VIEW mini_catalog AS
SELECT  c.name AS `catalog`, p.name AS `product` 
FROM  products p 
JOIN catalogs c ON p.catalog_id = c.id;


SELECT * FROM mini_catalog;


-- по желанию) Пусть имеется таблица с календарным полем created_at. В ней размещены разряженые календарные 
-- записи за август 2018 года '2018-08-01', '2016-08-04', '2018-08-16' и 2018-08-17. Составьте запрос, который 
-- выводит полный список дат за август, выставляя в соседнем поле значение 1, если дата присутствует в 
-- исходном таблице и 0, если она отсутствует.

DROP TABLE IF EXISTS test1.dates1;
CREATE TEMPORARY TABLE test1.dates1 (
	id SERIAL,
	created_at DATE
);

INSERT INTO dates1 (created_at) VALUES ('2018-08-01'), ('2018-08-04'), ('2018-08-08'),('2018-08-10');

SELECT * FROM dates1;

DROP TABLE IF EXISTS test1.dates2;
CREATE TEMPORARY TABLE test1.dates2 (
	`date` DATE
);

INSERT INTO dates2 VALUES ('2018-08-01'), ('2018-08-02'), ('2018-08-03'),('2018-08-04'),('2018-08-05'),('2018-08-06')
,('2018-08-07'),('2018-08-08'),('2018-08-09'), ('2018-08-10'), ('2018-08-11'), ('2018-08-12'), ('2018-08-13')
, ('2018-08-14'), ('2018-08-15'), ('2018-08-16'), ('2018-08-17'), ('2018-08-18'), ('2018-08-19'), ('2018-08-20')
, ('2018-08-21'), ('2018-08-22'), ('2018-08-23'), ('2018-08-24'), ('2018-08-25'), ('2018-08-26'), ('2018-08-27')
, ('2018-08-28'), ('2018-08-29'), ('2018-08-30'), ('2018-08-31');

SELECT * FROM dates2;

SELECT d2.*, IF(d1.created_at IS NULL, 0, 1) AS `col`
FROM dates2 AS d2
LEFT JOIN dates1 AS d1 ON d1.created_at = d2.`date`; 


-- Практическое задание по теме “Хранимые процедуры и функции, триггеры"
-- Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего 
-- времени суток. С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция 
-- должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".

-- NOT DETERMINISTIC - чтобы серевер не кешировал ответы
DELIMITER //

DROP FUNCTION IF EXISTS hello//
CREATE FUNCTION hello()
RETURNS TINYTEXT NOT DETERMINISTIC
BEGIN
	DECLARE curr_hour INT;
	DECLARE message TINYTEXT DEFAULT '';

	SET curr_hour = HOUR(NOW());

	IF (curr_hour < 6) THEN
		SET message = 'Доброй ночи';
    ELSEIF (curr_hour < 12) THEN
        SET message = 'Доброе утро';
    ELSEIF (curr_hour < 18) THEN
        SET message = 'Добрый день';
    ELSE
        SET message = 'Добрый вечер';
	END IF;

	RETURN message;
END//

DELIMITER ;

SELECT hello();




-- В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
-- Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное 
-- значение NULL неприемлема. Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля 
-- были заполнены. При попытке присвоить полям NULL-значение необходимо отменить операцию.

-- Такой же триггер можно создать и на UPDATE
DELIMITER //
DROP TRIGGER IF EXISTS not_empty_name_or_descr//
CREATE TRIGGER not_empty_name_or_descr BEFORE INSERT ON products
FOR EACH ROW
BEGIN
	IF (NEW.name IS NULL AND NEW.description IS NULL) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Недопустима ситуация когда оба поля NULL';
	END IF;


END//

DELIMITER ;


-- (по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. Числами Фибоначчи 
-- называется последовательность в которой число равно сумме двух предыдущих чисел. Вызов функции FIBONACCI(10)
--  должен возвращать число 55.

DELIMITER //
DROP FUNCTION IF EXISTS fibonacci//
CREATE FUNCTION fibonacci (dig INT)
RETURNS NUMERIC(38) DETERMINISTIC
BEGIN
	DECLARE one, two NUMERIC(38);
	DECLARE counter INT;
	
	SET two = 1;

	IF dig > 2 THEN
		SET counter = 3;
		SET one = 1;
	
		WHILE dig >= counter DO
			SET two = one + two;
			SET one = two - one;
			SET counter = counter + 1;
		
		END WHILE;
	
	END IF;
	


	RETURN two;
END//

DELIMITER ;


SELECT fibonacci(18);


