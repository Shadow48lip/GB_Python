-- Пусть в таблице users поля created_at и updated_at оказались незаполненными. 
-- Заполните их текущими датой и временем.
UPDATE users SET created_at=NOW(), updated_at=NOW();



-- Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы
--  типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 8:10". 
--  Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.

-- ломаем
ALTER TABLE	users CHANGE updated_at updated_at VARCHAR(50);
ALTER TABLE	users CHANGE created_at created_at VARCHAR(50);
-- Пишем не верные строковые значения
UPDATE users SET created_at='20.10.2017 8:10', updated_at='20.10.2017 9:30';

-- исправляем данные
UPDATE users SET 
created_at = STR_TO_DATE (created_at, '%d.%m.%Y %H:%i'),
updated_at = STR_TO_DATE (updated_at, '%d.%m.%Y %H:%i');

-- выставляем правильное поле
ALTER TABLE	users CHANGE updated_at updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
ALTER TABLE	users CHANGE created_at created_at DATETIME DEFAULT CURRENT_TIMESTAMP;



-- В таблице складских запасов storehouses_products в поле value могут встречаться самые 
-- разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы. Необходимо
-- отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения 
-- value. Однако, нулевые запасы должны выводиться в конце, после всех записей.

SELECT *
FROM `storehouses_products`
ORDER BY `value` = 0, `value` ASC;

-- или так
SELECT *
FROM `storehouses_products`
ORDER BY IF( `value` = 0, 1, 0 ), `value` ASC;


