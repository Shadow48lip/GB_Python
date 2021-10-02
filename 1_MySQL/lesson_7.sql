-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
SELECT id, name FROM users WHERE id IN (
	SELECT DISTINCT user_id FROM orders
);

-- Выведите список товаров products и разделов catalogs, который соответствует товару.
SELECT p.name AS prod_name, c.name AS cat_name FROM products p JOIN catalogs c ON p.catalog_id = c.id ;

-- (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
-- Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов 
-- flights с русскими названиями городов.

-- Создал простенькие таблицы для теста.
CREATE TABLE test1.flights (
	id serial auto_increment NOT NULL,
	`from` varchar(100) NULL,
	`to` varchar(100) NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci
COMMENT='7 видеоурок mysql';

CREATE TABLE test1.cities (
	label varchar(100) NULL,
	name varchar(100) NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;

-- Вот такой давольно тяжелый запрос получился при миллионе записей.

SELECT id, 
	(SELECT name FROM cities WHERE label=`flights`.`from`) AS `from`,
	(SELECT name FROM cities WHERE label=`flights`.`to`) AS `to`
FROM flights;

-- best variant
SELECT 
	f.id,
	cities_from.name AS `from`,
	cities_to.name AS `to`
FROM flights f
LEFT JOIN cities AS cities_from ON f.from = cities_from.label
LEFT JOIN cities AS cities_to ON f.to = cities_to.label