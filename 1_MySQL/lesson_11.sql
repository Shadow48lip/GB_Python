-- Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, catalogs и products 
-- в таблицу logs помещается время и дата создания записи, название таблицы, идентификатор первичного ключа и 
-- содержимое поля name.

USE shop;

DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  `table` VARCHAR(30) NOT NULL COMMENT 'Какую таблицу залогировали',
  `key` BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Идентификатор первичного ключа',
  name VARCHAR(255) NOT NULL COMMENT 'Идентификатор поля name'
) COMMENT = 'Архивная таблица логов' ENGINE=Archive;


DELIMITER //
DROP TRIGGER IF EXISTS log_for_users//
CREATE TRIGGER log_for_users AFTER INSERT ON users
FOR EACH ROW
BEGIN
	INSERT INTO logs VALUES (NOW(), 'users', NEW.id, NEW.name);

END//
DELIMITER ;


INSERT INTO users (name, birthday_at) VALUES ('Дармидон', NOW());



DELIMITER //
DROP TRIGGER IF EXISTS log_for_catalogs//
CREATE TRIGGER log_for_catalogs AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
	INSERT INTO logs VALUES (NOW(), 'catalogs', NEW.id, NEW.name);

END//
DELIMITER ;

INSERT INTO catalogs (name) VALUES ('Мышки');



DELIMITER //
DROP TRIGGER IF EXISTS log_for_products//
CREATE TRIGGER log_for_products AFTER INSERT ON products
FOR EACH ROW
BEGIN
	INSERT INTO logs VALUES (NOW(), 'products', NEW.id, NEW.name);
END//
DELIMITER ;


INSERT INTO products (name, price) VALUES ('Ipad pro 12', 30000);


SELECT * FROM logs;


-- (по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион записей.


DELIMITER //
DROP PROCEDURE IF EXISTS generate_users//
CREATE PROCEDURE generate_users (IN value INT)
BEGIN
	
	DECLARE i INT DEFAULT 0;
	WHILE i < value DO
		INSERT INTO users (name, birthday_at) VALUES (CONCAT('user ', i), NOW());
		SET i=i+1;
	END WHILE;

END//
DELIMITER ;

CALL generate_users(10000000);