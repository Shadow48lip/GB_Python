/*
ОПИСАНИЕ

База данных инетрнет-магазина.

Далее прилагаю краткое описание функционала, хотя DDL команды вроде бы снабдил комментариями.

  БД позволяет создавать многоуровневые каталоги товаров с шаблоном спецификаций для дальнейшей передачи этого
шаблона в товар, который прикрепят к каталогу.
  Скидки могут действовать на пользователя, на группу пользователей (ранг), товар или группу каталога. 
  Все с учетом периода действия либо дня недели.Товары снабжаются коротким и длинными описаниями и наследуют 
спецификации от каталога.
  Предусмотрены складские таблицы. Список складов, где отражается адрес склада и рабочий статус. Дабы не продавать
товары с этого склада если он закрыт. Таблица складских остатков где учтены товар, в каком количестве и где находится.
  При заказе товара работает основная таблица orders, которая связана внешними ключами (один ко многим) с вспомогательными
таблицами состава заказа orders_goods, способов оплаты payment_methods, способов доставки delivery и delivery_methods.
  Одна из основных таблиц, на которую многие ссылаются это users. Поскольку логином для авторизации может выступать 
как e-mail, так и и номер телефона, то снабжаем таблицу трекером, который не даст добавить пользователя двумя 
этими пустыми полями.
  Для пользователей так же существует таблица уровней крутости - ранги. В зависимости от частоты заказов можем
ему их повышать, а в дальнейшем для одного из рангов делать распродажи.
  Ну и наконец пользователь может писать отзывы и ставить оценки как заказам, так и товарам. Тут надо следить,
чтоб отзыв можно было оставлять только о тех товарах, которые им покупались.
*/

-- DDL

DROP DATABASE IF EXISTS myshop;
CREATE DATABASE myshop;

USE myshop;

SET foreign_key_checks = 0;

DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
  id SERIAL PRIMARY KEY,
  parent_id BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'id родителя, если верхний уровень то 0',
  name VARCHAR(100) NOT NULL COMMENT 'Название раздела',
  specifications JSON COMMENT 'Базовые характеристики для товаров этого раздела',
  INDEX parent_idx (parent_id)
) COMMENT = 'Разделы интернет-магазина';



DROP TABLE IF EXISTS goods;
CREATE TABLE goods (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL COMMENT 'Название',
  description_short VARCHAR(300) COMMENT 'Краткое описание',
  description_full TEXT COMMENT 'Полное описание с html тегами',
  price DECIMAL (11,2) NOT NULL DEFAULT 0 COMMENT 'Цена',
  specifications JSON COMMENT 'Характеристики для товаров этого раздела. Наследуется из группы.',
  catalog_id BIGINT UNSIGNED,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX catalog_id_idx (catalog_id),
  INDEX name_idx (name),
  UNIQUE catalog_name_uniq (catalog_id, name) COMMENT 'Точно не должно быть в одном каталоге двух одинаковых товаров',
  CONSTRAINT `catalog_id_fk` FOREIGN KEY (`catalog_id`) REFERENCES `catalogs` (`id`)
) COMMENT = 'Товарные позиции';


DROP TABLE IF EXISTS warehouse;
CREATE TABLE warehouse (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL COMMENT 'Название',
  address VARCHAR(100) NOT NULL COMMENT 'Адрес скалада',
  is_working BINARY(1) DEFAULT 1 COMMENT 'Работает ли склад. 1 - работает, 0 - нет',
  INDEX working_flag (is_working)
) COMMENT = 'Складские помещения';


DROP TABLE IF EXISTS warehouse_goods;
CREATE TABLE warehouse_goods (
  id SERIAL PRIMARY KEY,
  warehouse_id BIGINT UNSIGNED NOT NULL,
  good_id BIGINT UNSIGNED NOT NULL,
  value INT UNSIGNED COMMENT 'Количество',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX good_idx (good_id), 
  INDEX warehouse_idx (warehouse_id),
  CONSTRAINT `warehouse_id_fk` FOREIGN KEY (`warehouse_id`) REFERENCES `warehouse` (`id`),
  CONSTRAINT `goods_id_fk` FOREIGN KEY (`good_id`) REFERENCES `goods` (`id`)
 ) COMMENT = 'Остаток товара на складе';


DROP TABLE IF EXISTS discounts;
CREATE TABLE discounts (
  id SERIAL PRIMARY KEY,
  user_id BIGINT UNSIGNED DEFAULT NULL COMMENT 'Если скидка относится к пользователю',
  user_rank_id BIGINT UNSIGNED DEFAULT NULL COMMENT 'Если скидка относится ко всем пользователям с рангом таким-то',
  good_id BIGINT UNSIGNED DEFAULT NULL COMMENT 'Если скидка относится к товару',
  catalog_id BIGINT UNSIGNED DEFAULT NULL COMMENT 'Если скидка относится к каталогу',
  discount FLOAT(4,2) COMMENT 'Величина скидки от 0.0 до 1.0',
  started_at DATETIME DEFAULT NULL,
  finished_at DATETIME DEFAULT NULL,
  day_of_week VARCHAR(13) DEFAULT NULL COMMENT 'Дни недели работы скидки через запрятую',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX user_idx (user_id),
  INDEX user_rank_idx (user_rank_id),
  INDEX good_idx (good_id),
  CONSTRAINT `discount_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `discount_rank_id_fk` FOREIGN KEY (`user_rank_id`) REFERENCES `users_rank` (`id`),
  CONSTRAINT `discount_goods_id_fk` FOREIGN KEY (`good_id`) REFERENCES `goods` (`id`),
  CONSTRAINT `discount_catalog_id_fk` FOREIGN KEY (`catalog_id`) REFERENCES `catalogs` (`id`)
) COMMENT = 'Скидки';


DROP TABLE IF EXISTS users_rank;
CREATE TABLE users_rank (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL COMMENT 'Название',
  description VARCHAR(300) COMMENT 'Описание'
) COMMENT = 'Ранги пользователей';

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  phone BIGINT UNSIGNED UNIQUE DEFAULT NULL,
  email VARCHAR(120) UNIQUE DEFAULT NULL,
  is_confirmed_phone BINARY(1) DEFAULT 0 COMMENT 'Подтвержден ли телефон',
  is_confirmed_email BINARY(1) DEFAULT 0 COMMENT 'Подтвержден ли e-mail',
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  password_hash VARCHAR(100),
  user_rank_id BIGINT UNSIGNED DEFAULT NULL,
  is_active BINARY(1) DEFAULT 1 COMMENT 'Пользователь может быть отключен, например за подбор пароля',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX phone_pwd_idx (phone, password_hash) COMMENT 'для авторизации',
  INDEX email_pwd_idx (email, password_hash),
  CONSTRAINT `rank_id_fk` FOREIGN KEY (`user_rank_id`) REFERENCES `users_rank` (`id`)
) COMMENT = 'Покупатели';

-- триггер на телефон и e-mail, обязательно что-нибудь - это логин
DELIMITER //
DROP TRIGGER IF EXISTS not_empty_phone_or_email//
CREATE TRIGGER not_empty_phone_or_email BEFORE INSERT ON users
FOR EACH ROW
BEGIN
	IF (NEW.phone IS NULL AND NEW.email IS NULL) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Недопустима ситуация когда оба поля NULL';
	END IF;
END//
DELIMITER ;






DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id BIGINT UNSIGNED,
  status TINYINT(1) UNSIGNED DEFAULT 0 COMMENT '0-корзина на сайте, 1-корзина сформирована, 2-доставляется, 10-выполнен',
  is_paid BINARY(1) DEFAULT 0 COMMENT 'Заказ оплачен',
  payment_id BIGINT UNSIGNED DEFAULT NULL COMMENT 'Способ оплаты',
  delivery_id BIGINT UNSIGNED DEFAULT NULL COMMENT 'Способ доставки',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  paid_at DATETIME DEFAULT NULL,
  delivery_at DATETIME DEFAULT NULL,
  finish_at DATETIME DEFAULT NULL,
  INDEX user_idx (user_id),
  CONSTRAINT `orders_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `orders_payment_id_fk` FOREIGN KEY (`payment_id`) REFERENCES `payment_methods` (`id`),
  CONSTRAINT `orders_delivery_id_fk` FOREIGN KEY (`delivery_id`) REFERENCES `delivery_methods` (`id`)
) COMMENT = 'Заказы';



DROP TABLE IF EXISTS orders_goods;
CREATE TABLE orders_goods (
  id SERIAL PRIMARY KEY,
  order_id BIGINT UNSIGNED,
  good_id BIGINT UNSIGNED,
  price DECIMAL (11,2) NOT NULL DEFAULT 0 COMMENT 'Цена позиции с учетом скидок',
  quantity INT UNSIGNED NOT NULL DEFAULT 1 COMMENT 'Количество заказанных товарных позиций',
  total DECIMAL (11,2) AS (price * quantity) STORED COMMENT 'Сумма по позиции',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX orders_goods_order_idx (order_id),
  CONSTRAINT `orders_goods_order_id_fk` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `orders_goods_good_id_fk` FOREIGN KEY (`good_id`) REFERENCES `goods` (`id`)
) COMMENT = 'Состав заказа';

-- после восстановления дампа можно убрать, иначе пакетная вставка не пройдет
ALTER TABLE orders_goods MODIFY COLUMN total decimal(11,2) DEFAULT 0.00 NOT NULL COMMENT 'Сумма по позиции';



DROP TABLE IF EXISTS payment_methods;
CREATE TABLE payment_methods (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL COMMENT 'Название',
  payment_type TINYINT UNSIGNED DEFAULT 0 COMMENT '0-онлайн оплата, 1-оплата при получении'
) COMMENT = 'Способы оплаты'; 



DROP TABLE IF EXISTS delivery_methods;
CREATE TABLE delivery_methods (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL COMMENT 'Название',
  delivery_type TINYINT UNSIGNED DEFAULT 0 COMMENT '0-до терминала, 1-до двери'
  
) COMMENT = 'Способы доставки'; 


DROP TABLE IF EXISTS delivery;
CREATE TABLE delivery (
  id SERIAL PRIMARY KEY,
  order_id BIGINT UNSIGNED,
  delivery_met_id BIGINT UNSIGNED DEFAULT NULL COMMENT 'Способ доставки',
  address VARCHAR(255) NOT NULL COMMENT 'Адрес доставки или пункта выдачи',
  track VARCHAR(50) NOT NULL COMMENT 'Трэк внешней системы доставки',
  status TINYINT(1) UNSIGNED DEFAULT 0,
  INDEX delivery_order_id_idx (order_id),
  CONSTRAINT `delivery_order_id_fk` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `delivery_method_id_fk` FOREIGN KEY (`delivery_met_id`) REFERENCES `delivery_methods` (`id`)
  
) COMMENT = 'Детали и статус конкретной доставки'; 


DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  user_id BIGINT UNSIGNED NOT NULL,
  order_id BIGINT UNSIGNED DEFAULT NULL,
  good_id BIGINT UNSIGNED DEFAULT NULL COMMENT 'Если присутвует то отзыв о товаре',
  description TEXT NOT NULL COMMENT 'Текст отзыва',
  score TINYINT UNSIGNED DEFAULT 0 COMMENT 'Оценка пользователя',
  INDEX reviews_order_id_idx (order_id),
  INDEX reviews_good_id_idx (good_id),
  INDEX reviews_user_idx (user_id),
  CONSTRAINT `reviews_order_id_fk` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `reviews_good_id_fk` FOREIGN KEY (`good_id`) REFERENCES `goods` (`id`),
  CONSTRAINT `reviews_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
  
) COMMENT = 'Отзывы о заказе или товаре'; 



SET foreign_key_checks = 1;


