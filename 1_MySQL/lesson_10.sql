-- Курсовой проект на тему интернет-магазин


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
  -- проставить индексы и внещние ключи
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

-- пока делаем обычную колонку. иначе генерировать данные большой гемор
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



-- SET foreign_key_checks = 1;




-- ОСМЫСЛЕННЫЕ ДАННЫЕ --

INSERT INTO catalogs (parent_id, name) VALUES
  (0, 'Электроника'), (0, 'Бытовая техника'), (0, 'Товары для дома'),
  (0, 'Детские товары'), (0, 'Одежда, обувь'),
  (1, 'Телефоны'), (1, 'Планшеты'), (1, 'Фото-видео'), (1, 'Телевизоры'),
  (2, 'Крупная бытовая техника'), (2, 'Встраиваемая техника'), (2, 'Климатическое оборудование'), (2, 'Техника для кухни'), 
  (3, 'Хозяйственные товары'), (3, 'Сушилки для белья'), (3, 'Мебель'), (3, 'Ковры'), 
  (4, 'Детские игрушки'), (4, 'Детские коляски'), (4, 'Детская обувь'), (4, 'Детская одежда'), 
  (5, 'Мужская одежда'), (5, 'Женская одежда'), (5, 'Обувь'), (5, 'Аксессуары');

INSERT INTO warehouse (name, address) VALUES
  ('Сллад - 1', 'г. Москва, Красная площадь, 1'), ('Сллад - 2', 'г. Воронеж, Лизюкова ул., 1');
 
 
INSERT INTO payment_methods (name, payment_type) VALUES
  ('Наличные', 0), ('Наличные', 1),
  ('Терминал QIWI', 1),
  ('VISA/MasterCard', 0), ('VISA/MasterCard', 1),
  ('Boxberry', 1);

 INSERT INTO delivery_methods (name, delivery_type) VALUES
  ('Самовывоз из Boxberry', 0), ('Отделения почты России', 0),
  ('CDEK до терминала', 0), ('CDEK до дери', 1);

 
 -- Генерация данных http://filldb.info/  --
LOCK TABLES `users_rank` WRITE;
/*!40000 ALTER TABLE `users_rank` DISABLE KEYS */;
INSERT INTO `users_rank` VALUES (1,'Новый пользователь','Soluta aut dignissimos eius sit quidem non. Et minus beatae autem nesciunt esse earum id. Iusto repellendus eum voluptatem.'),(2,'Постоянный клиент','Quidem a et non esse adipisci corrupti repudiandae. Ipsa nisi nam harum consequuntur voluptate velit. Eligendi aut qui sed voluptates labore animi omnis.'),(3,'Давно с нами','Expedita rerum doloribus sit nostrum nisi. Neque repellendus eaque expedita perferendis et. Quam et beatae veniam provident voluptas. Hic distinctio voluptates voluptatem rerum quis est aut.'),(4,'Уважаемый','Quasi nisi natus est. Illum corrupti accusamus autem aut velit blanditiis. Blanditiis animi soluta omnis ea sapiente. Et incidunt magnam expedita at similique non.'),(5,'VIP пользователь','Distinctio odit tempora magnam voluptate quae. Quae atque voluptas eligendi dolores possimus odio.');
/*!40000 ALTER TABLE `users_rank` ENABLE KEYS */;
UNLOCK TABLES; 
 
 
LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,79981465804,'manuel.wilderman@example.com','\0','\0','Alisha','2007-11-01','c11193cb2df75816c409744ea71a4d0492354d92',1,'\0','2009-06-19 10:03:11','1983-08-01 05:17:09'),(2,79216488260,'ykutch@example.com','\0','1','Estella','1970-06-30','d235e77bc4f2e3235c0f8efa229022b575397dc9',2,'\0','1982-07-06 10:55:44','2018-04-12 02:55:49'),(3,79885847033,'jnikolaus@example.net','\0','1','Renee','1984-03-07','8930e1fe9c33d3c936b93d945d2c7adc693f0a3c',3,'\0','1997-08-21 22:13:09','2010-05-01 00:24:01'),(4,79708657659,'scot67@example.net','1','\0','Stephania','1977-10-19','cff625491b2040ff598058dad5eb2af7d2cd9248',4,'\0','1976-02-17 16:40:35','2008-10-04 06:55:26'),(5,79395228501,'ellsworth.thiel@example.net','\0','1','Magnus','2016-08-21','598e34c4d371960ffef38d431a57461bc624e474',5,'\0','1999-11-06 05:27:05','2020-07-27 12:25:07'),(6,79884752875,'yharber@example.net','1','1','Kasey','1989-10-07','efb3e79ccf06d55dca02462df97a86272386b24f',1,'\0','1987-07-26 04:32:50','2004-11-03 02:12:18'),(7,79437236593,'myrtice14@example.org','1','\0','Beulah','1984-05-28','ed8624e5e957caf69e4ced3982e4d2e5b2cf025d',2,'\0','2020-02-12 23:41:12','2016-10-27 20:37:47'),(8,79501939853,'dameon.jacobs@example.com','\0','1','Tanner','2009-10-02','0fdfc8fe7fef104f078a7e6b45d79514c9604f2e',3,'\0','2010-06-06 11:04:25','1994-07-06 19:35:04'),(9,79646951189,'alexander85@example.org','1','1','Dameon','1971-03-16','0f5deab0fca8fe5ef10c23428e2cefb9dbda36e7',4,'\0','1999-02-28 21:40:13','2013-01-09 21:31:45'),(10,79123134091,'klein.josie@example.org','\0','1','Myron','1978-06-09','2c65641d91770f1f55332ce6051e7d3f78c90092',5,'\0','1998-11-19 13:50:18','1998-08-17 01:41:25');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

-- для генерации убить внешний ключ
LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (51,'inventore','Et quia ut dolorem quas. Et voluptatum quisquam quos sint numquam labore aut. Autem inventore doloremque animi ut. Aut culpa qui autem.','Est voluptatum aperiam sit blanditiis eligendi perspiciatis in. Quos velit optio aliquid et a velit.',3338.34,NULL,8,'1970-08-06 18:34:01','2020-04-13 20:22:32'),(52,'non','Sapiente impedit inventore atque optio consequuntur voluptate. Non voluptate sed qui ipsam sunt deserunt. Magni voluptates optio dolores eum a aut. Itaque officia sit quisquam veritatis quis incidunt fuga.','Qui non itaque modi eaque. Repudiandae dolores sed atque error non dolor. Sed minus omnis voluptas et ut et aut.',3488.62,NULL,21,'1994-10-05 17:20:40','2021-04-03 03:30:28'),(53,'molestiae','Aperiam et aut fugit sint temporibus fuga nam vero. Ipsum ipsam molestias amet architecto fugiat facere ut aliquid. Nulla dolorum vel rerum soluta deleniti ipsam et. Doloribus neque ut tempora qui omnis quae et.','Placeat adipisci dolores soluta placeat dolorem dicta. Laboriosam ut suscipit eum odio. Atque officia qui voluptas laboriosam. Et sunt laboriosam facere autem odio qui.',347.81,NULL,24,'1981-07-11 18:37:41','1995-08-01 09:46:54'),(54,'sunt','Et qui autem quos enim. Non alias nobis soluta accusantium. Consectetur rem sit aut quisquam.','Vel et et vitae aut et. Est autem quia temporibus. Voluptatem consequatur consequatur et quas id.',7716.00,NULL,16,'1992-03-28 16:37:12','2002-12-23 12:45:38'),(55,'sint','Iure aut modi laudantium architecto neque. Saepe illum ducimus repellat enim reiciendis. Est non ut id soluta temporibus id. Cum est quo ab aut rerum et.','Velit sed reprehenderit vitae adipisci. Est aut sed enim harum. A omnis iure in omnis dignissimos.',2343.79,NULL,17,'2009-01-26 14:22:22','2001-04-01 20:01:46'),(56,'voluptatem','Aspernatur maiores laboriosam qui eos quia illo omnis. Ad aut nulla ratione. Ex facilis qui non alias doloremque dicta sunt quasi. Corporis repellat molestiae et ea totam qui minima.','Consequatur debitis ut nihil aliquid aliquid numquam. Voluptatem fuga possimus officiis distinctio. Delectus voluptatem ipsa pariatur quaerat ducimus.',5988.00,NULL,20,'1972-06-12 15:33:03','1990-11-23 19:25:04'),(57,'minima','Officiis ut ab omnis fuga hic voluptatem. Sed molestiae reiciendis in nihil quo accusantium quo aspernatur. Laudantium quam ad voluptate maiores sunt sit. Sit nobis quidem suscipit dolore similique eos quis ab.','Ratione aspernatur rem reiciendis magni doloremque molestiae. Voluptas reprehenderit blanditiis reprehenderit laudantium voluptatem nobis dolorum. Ut vel tempore et eum est quas qui. Omnis laborum sit accusantium vitae.',6338.03,NULL,12,'1975-02-23 12:27:26','1993-08-23 04:24:35'),(58,'alias','Dolores non qui ut inventore. Sed sunt non possimus deserunt doloremque quos quia distinctio. Commodi cum et qui rem deleniti autem nostrum. Accusamus ipsam possimus iusto nisi et laborum. Maiores et doloremque eius vel quo.','Esse qui ullam inventore eius illo. Rerum similique facere esse et. Ea in error saepe et et ut non. Exercitationem dolorem qui ducimus.',5516.22,NULL,23,'1991-03-04 11:01:49','1989-03-17 18:32:19'),(59,'dolor','Eos quidem dolorum sint architecto nobis et animi. Qui voluptatem excepturi quae non voluptatem. Qui enim eveniet neque alias qui. Quia facilis sapiente laborum.','Rerum dolores nisi suscipit eos nisi culpa. Repellendus nulla et dolorem asperiores. Nesciunt vero doloribus est repellat magnam.',1818.68,NULL,19,'2011-09-02 19:56:38','1982-07-16 14:32:36'),(60,'aut','Qui quibusdam ratione aut natus nemo. Ratione ducimus fugiat corporis at consequatur. Doloremque omnis aut maxime. Eaque aspernatur consequatur enim occaecati. Laboriosam harum harum voluptate quia at.','Et quasi suscipit esse quis inventore. Vitae eveniet et veniam reprehenderit accusamus aut odio voluptatem.',768.27,NULL,16,'1996-07-04 04:40:42','1976-07-06 05:48:39'),(61,'quas','Provident voluptas optio modi debitis hic nobis. Eveniet dolorum dolores quam porro. Suscipit a quidem aut rerum ut repellat dolor soluta. Minus natus doloribus deserunt eum et rerum perspiciatis.','Vel aliquid sit autem in veritatis tempore. Vero expedita sit id eum in veritatis fugiat. Id sit voluptate hic mollitia error vel. Quibusdam aut aut deserunt itaque error ipsa consectetur.',6180.27,NULL,13,'1989-06-30 04:09:57','1990-06-14 18:38:42'),(62,'et','Voluptatem nesciunt quod doloremque veritatis ad voluptate perspiciatis. Aliquam excepturi non laborum voluptatem impedit facilis. Perspiciatis qui nobis fugit possimus sequi. Rerum beatae reprehenderit asperiores distinctio culpa sit.','Eos autem doloribus quos vitae enim sint et. Porro rerum consequatur veritatis qui eos doloribus sapiente. Ducimus officiis suscipit quis consectetur ut. Explicabo odit beatae asperiores ut.',1895.23,NULL,12,'2000-02-03 14:42:00','2011-01-17 09:38:34'),(63,'deserunt','Omnis sequi odio eius nihil ea et ab cupiditate. Cupiditate et delectus molestiae nobis unde. Inventore sint iure nam deleniti.','Enim consequatur officiis eius repudiandae. Est est tenetur praesentium quis quis in. Occaecati aliquid aut quae. Dolores sunt qui soluta voluptatem corporis sunt deleniti.',1545.05,NULL,13,'2013-01-31 05:02:39','1993-11-17 02:31:18'),(64,'ullam','Cupiditate itaque nemo impedit autem ipsam. Eius nobis error voluptatem similique esse illum consequatur ea. Voluptatem hic dolores sint possimus.','Omnis sunt quis dolorem molestias vitae. Aut non laborum laborum rerum nesciunt. Similique temporibus rerum debitis beatae dolores non sequi.',916.35,NULL,12,'1982-01-27 21:37:05','1995-08-31 07:32:18'),(65,'ullam','Doloribus eveniet illo eligendi aperiam. Odio et sit quos recusandae aperiam. Fugit incidunt sunt dolorem repellendus.','Quis magnam et fugit sed omnis natus rerum. Omnis laboriosam fugiat saepe repellat consequuntur voluptatem magnam. Rem soluta repellat magni cum minus deleniti.',3041.29,NULL,9,'2004-05-26 01:27:08','2003-10-12 11:21:24'),(66,'sunt','Ex molestiae nihil cumque placeat nihil voluptas. Porro ratione incidunt nihil quod. Vero et dolorem impedit similique voluptates ad. Qui voluptas odio soluta provident.','Quisquam minima nostrum rerum totam. Aliquam dolorum doloribus temporibus consequatur explicabo voluptatem non nemo. Dolore qui ut et est itaque reprehenderit repellat. Aliquam totam dolorem nesciunt ut. Fugit officiis non officia aut.',5873.94,NULL,24,'2001-01-05 00:25:03','1974-11-15 22:39:45'),(67,'cupiditate','Saepe placeat mollitia earum consequatur. Sed et alias eligendi ea eum commodi esse. Cupiditate et maiores quae quos quo necessitatibus aut accusantium. Dolor qui minus qui sapiente. Nostrum quas voluptas earum ut qui sapiente tenetur.','Ut adipisci cumque soluta quo corrupti odio tenetur. Placeat soluta necessitatibus quia ut nihil vitae ex.',2219.30,NULL,7,'1980-03-10 09:26:41','2014-05-05 15:06:31'),(68,'sunt','Corporis occaecati fugiat cumque dolores ipsum. Ea in qui harum perferendis aut eligendi. Perferendis blanditiis qui repudiandae minima minima reiciendis. Reprehenderit omnis sunt odit est et molestiae aut.','Sit ab aut aut iusto accusamus nesciunt. Rerum voluptatem qui ipsam temporibus et a qui. Dicta officiis rerum sunt qui voluptatem.',4833.92,NULL,11,'2003-02-02 15:07:32','2018-04-29 20:36:31'),(69,'velit','Inventore iste sequi veritatis ut deleniti. Quaerat blanditiis ullam omnis voluptatem. Rerum molestiae ut et distinctio. Sapiente et ipsa doloribus perspiciatis at.','Qui porro qui eos nihil. Voluptatem qui asperiores perspiciatis qui qui quia eaque. Maiores et repudiandae est velit laudantium quae. Harum facilis quasi consequatur enim eos aspernatur blanditiis.',1212.89,NULL,15,'1998-07-13 10:11:24','2000-06-04 09:34:12'),(70,'sed','Laudantium placeat consectetur sit non ullam. Architecto magni sunt id sed occaecati. Molestias qui illo consequatur odit iste doloribus.','Fugiat quisquam aut et veritatis eum qui explicabo veniam. Omnis rerum nesciunt exercitationem. Expedita est optio vel velit. Aut enim vero molestiae ullam consequuntur cupiditate quia.',7006.80,NULL,20,'1982-07-31 03:58:42','1985-09-08 10:09:41'),(71,'quia','Sit quam in aut. Voluptates et non voluptatem nihil fuga. Reiciendis commodi et libero doloribus qui aliquam. Incidunt esse ut iure aperiam eum dolore.','Quod quidem porro omnis eum eos quisquam corporis. Cum distinctio quae repellat repellat deleniti. Qui corrupti vel rem natus dolores et non. Aut quam qui minus.',6821.26,NULL,18,'1973-06-09 10:30:32','2015-08-16 06:08:21'),(73,'dolor','Expedita earum qui fugiat. Eos autem vero temporibus laboriosam quo dolore.','Rerum voluptas eaque voluptas ipsum nesciunt. Perspiciatis soluta et sint provident qui enim itaque. Dolor quam saepe corrupti praesentium sed. Rerum amet saepe officia esse delectus.',7686.14,NULL,18,'1994-03-16 18:21:10','2020-03-20 14:44:31'),(74,'facilis','Accusantium minus blanditiis itaque earum similique. Beatae quia porro dignissimos possimus nam officia deleniti et.','Est sed nihil placeat ad. Quibusdam aut laborum dolor neque aut. Similique tenetur ratione nam temporibus est aut suscipit. Omnis velit sunt iusto quia.',3384.81,NULL,15,'1980-12-29 05:03:24','2003-10-07 12:10:57'),(75,'at','Est voluptatem et iure molestiae. Quos vero aut placeat. Optio atque aut molestiae sunt velit numquam perferendis.','Tempore eveniet dolorum voluptas velit explicabo reiciendis. Et qui voluptatibus ratione recusandae. Repudiandae et illo explicabo non ea modi.',5470.37,NULL,9,'1989-04-20 10:28:30','2004-12-17 12:58:53'),(76,'et','Saepe nemo natus esse libero aliquam quaerat. Explicabo ab aut suscipit ducimus ut voluptas.','Sunt et tempora omnis odio. Dolores quasi aut aut porro. Sapiente nemo voluptates omnis ea.',9735.54,NULL,25,'2015-04-20 11:11:28','2006-10-08 03:52:12'),(77,'quos','Vitae et illum rerum reiciendis perspiciatis. Ut enim rem velit non expedita enim. Vero nobis quasi sed quis.','Labore neque eligendi nobis libero. Maiores non dolore eligendi amet autem velit.',798.79,NULL,10,'1982-07-28 22:35:46','2009-04-29 00:29:18'),(78,'veritatis','Aut vel vitae omnis. Placeat mollitia voluptatum cum quos. Qui explicabo rem perspiciatis tenetur.','Eius consequatur nostrum hic accusantium pariatur. Necessitatibus voluptates consequatur aspernatur ad sunt voluptas. Dolor eaque qui recusandae. Rerum dolores officiis voluptas placeat facere et veritatis. Est autem cumque eum molestiae eius ut voluptates.',980.45,NULL,21,'1984-03-27 01:38:09','1997-09-16 17:34:42'),(79,'non','Voluptas qui ut quaerat sequi sed voluptatum. Quae qui nesciunt itaque nulla et minima animi sit. Corrupti quia voluptas molestias voluptas. Quia quo aut unde non aut eius repellendus.','Sequi eos adipisci laudantium ut sed id provident iure. Fuga est illo quaerat quis ut consequuntur magnam.',7477.69,NULL,10,'1982-08-13 10:55:36','1985-03-10 20:41:25'),(80,'cupiditate','Libero ut consequatur illum rerum repudiandae placeat non dignissimos. Itaque voluptatum ullam nostrum quidem est. Et porro a vero expedita facilis.','Molestias eum deserunt sint eos et aut dolorem. In vel laborum eligendi praesentium nisi doloribus atque. Quam ullam reiciendis ipsum illo eum eius. Est blanditiis officia aut occaecati enim et pariatur doloribus. Quaerat sed ut illum corrupti itaque id.',4096.80,NULL,23,'1970-01-06 15:18:51','1984-05-21 02:25:08'),(81,'est','Fuga optio rerum est et. Rerum dolor vel eum est dolor repellendus. Delectus corrupti aut quia saepe. Cupiditate rem aperiam numquam unde et repellendus consequatur.','Architecto at aut rerum atque velit voluptatem. Iure amet error quia ea corporis laboriosam sit. Repudiandae repudiandae facere quo eveniet assumenda sint. Enim modi doloribus quos et voluptatem.',4632.45,NULL,13,'1989-09-01 11:19:36','1983-02-09 05:05:11'),(82,'nobis','Consequatur explicabo sunt officia doloremque asperiores dignissimos. Quaerat ullam odio ratione doloribus est iusto dolorem voluptate. Commodi et harum est sed officia. Ut et aut et sit sed nihil.','Voluptas qui sunt illum voluptatem vitae quaerat. Voluptatem temporibus sit neque quod. Illo aut est voluptatem ex harum nemo autem quia.',7717.68,NULL,19,'2021-02-16 15:28:51','1995-02-04 11:26:23'),(83,'enim','Cum architecto ratione accusantium ut. Quia dolore commodi ut velit excepturi enim. Fugiat est voluptatem rerum est magnam.','Ea architecto aut eos harum aperiam. Praesentium qui sint accusamus aliquam eligendi officia.',7878.42,NULL,20,'1977-04-13 09:58:51','1998-11-09 18:15:59'),(84,'molestias','Excepturi rem sit voluptate fugiat pariatur qui. Minus eum temporibus autem magnam. Iusto suscipit quod quisquam sed ea. Molestias similique magni ipsam eveniet quia.','Cupiditate eos non culpa aspernatur est quae assumenda. Eos unde sunt doloribus consectetur consequatur excepturi accusantium.',9051.85,NULL,8,'1986-12-13 04:17:20','1997-04-16 17:23:34'),(85,'ducimus','Reprehenderit exercitationem quidem sunt dolorem. Recusandae earum sint nemo eveniet. Molestiae ex atque quibusdam aut debitis nam. Molestiae atque a sit ut quaerat odit magni. Aperiam eos laboriosam aspernatur magnam commodi ipsam corrupti aspernatur.','Laborum rem ipsum nesciunt sed. Porro consequatur consequatur nihil quidem.',4294.77,NULL,20,'1995-03-07 08:36:49','2003-09-19 14:06:47'),(86,'veniam','Quo et labore esse repellendus explicabo tenetur cumque ad. Magni et tenetur ad quia corporis. Sunt cupiditate consequuntur ex non. Et ut ea eveniet ea eveniet.','Est porro dolor nobis sequi. Reiciendis quasi inventore hic dignissimos similique nobis cupiditate. Cumque eveniet quo sit eaque qui deserunt nihil. In amet magni aut rerum deserunt.',2134.34,NULL,18,'2004-01-27 03:30:38','1982-07-06 16:00:43'),(87,'dolores','Impedit odio et mollitia et necessitatibus distinctio. Id odit aspernatur vel architecto magnam commodi.','Sed pariatur officia qui harum facilis aut ut autem. Sint odio natus aut quod atque sint. Consequatur ipsam modi ipsam qui nam.',4059.00,NULL,18,'2021-09-13 13:24:35','1976-07-20 04:02:16'),(88,'id','Modi iure ullam dolor perspiciatis. Nobis odit facere aperiam eius cupiditate delectus labore. Iure velit voluptatem qui quos. Omnis modi perspiciatis voluptas inventore aperiam velit earum. Enim asperiores quidem dignissimos nam aut illo necessitatibus.','Recusandae vel inventore excepturi. Ut consequatur sed vitae minima maiores veniam.',9127.26,NULL,13,'1999-11-23 14:16:18','1992-11-17 05:06:29'),(89,'eum','Saepe commodi at voluptas voluptatibus. Ex aspernatur vero quod corrupti ut.','Omnis veniam rem voluptatem ipsam. Et quaerat et non eveniet eum reprehenderit voluptas. Quia eum facilis debitis fugiat assumenda et.',1284.80,NULL,13,'2013-09-30 14:02:37','1995-12-27 08:52:14'),(90,'nam','Et quia iusto nam recusandae et. Nostrum repellendus expedita assumenda aut quisquam. Molestiae eligendi consectetur reiciendis itaque. Eos perspiciatis accusamus vel debitis optio. Et ut aliquid sint distinctio.','Debitis dolor impedit ut voluptatem corrupti suscipit doloribus expedita. Ut quasi reiciendis quis quod laborum totam. Sequi temporibus harum ex adipisci. Iure qui maxime et laboriosam quam alias.',8453.97,NULL,19,'1986-03-10 04:38:43','1992-09-12 08:23:38'),(91,'rem','Enim provident id ut beatae recusandae. Dolores recusandae ad et fugiat facilis. Voluptas itaque dolores consequuntur ipsam dolores ad commodi. Nulla praesentium quaerat laboriosam quia.','Quia sed molestias id laborum fugiat libero. Ut expedita ipsum doloribus non molestiae est autem. Numquam alias labore velit est.',4312.20,NULL,25,'1978-06-26 17:57:20','1995-01-11 20:09:31'),(92,'similique','Aliquid consequuntur illo quia laboriosam animi non itaque. Doloremque esse non enim similique optio aut. Quasi vero ea blanditiis aspernatur dolores nesciunt cum. Molestias reiciendis cum saepe quam quia voluptate sequi.','Voluptas libero eos molestiae voluptatem maiores architecto. Atque assumenda accusantium reiciendis maxime rerum corrupti voluptatem. Molestiae distinctio qui id alias placeat et. Accusamus esse dolores saepe velit. Consequatur quos voluptas sunt earum aperiam assumenda distinctio.',5106.64,NULL,8,'2015-07-27 21:21:19','2000-01-29 17:08:29'),(93,'sed','Tempore placeat voluptatem doloribus totam illum officia eaque. Velit suscipit dolor aut ea rerum sapiente reprehenderit. Quo provident dolores illo fugit eaque aliquid dolores.','Totam aut voluptas impedit sit qui modi. Placeat doloribus libero corporis sed incidunt vel. Aut illo eum ut aut quos.',3693.27,NULL,16,'1975-11-22 05:33:48','1999-05-07 22:50:37'),(94,'repellat','Eos earum ullam a iste. Cumque vero voluptates quibusdam totam. Repudiandae eaque voluptatem labore culpa. Ea rem architecto unde commodi omnis tempora.','Repudiandae cum qui itaque at modi non est. Et vel amet provident quam provident quisquam. Vel cupiditate ipsum quia fuga placeat porro vel.',8316.53,NULL,11,'1981-09-03 05:53:50','1977-02-24 21:53:24'),(95,'omnis','Voluptate aut sed consequuntur. Fugiat harum occaecati rerum odit sed. Sed temporibus assumenda provident nisi quo doloremque et. Dolores voluptatem non itaque non delectus nihil vel.','Quo quas in aut quidem fuga modi. Dicta modi saepe cum fugiat mollitia voluptas et.',3631.89,NULL,18,'2017-07-20 11:10:04','1978-10-16 19:00:34'),(97,'ad','Alias blanditiis expedita doloribus sunt magni et at. Omnis dolorem non sint corporis consequatur. Quos error in et ad quam.','Provident non minus aut quos nisi. Architecto modi dolores libero molestiae. Alias ipsam maxime aut odio quia. Totam atque voluptatum ut eum.',6335.64,NULL,21,'1996-11-03 11:16:18','2014-02-10 08:30:27'),(98,'aut','Mollitia ipsam et sit consequatur illo et. Ratione itaque aperiam dolorem. Expedita ex numquam et odio. Aut reprehenderit voluptatem aut.','Et consequatur itaque fuga qui dolore est laboriosam inventore. Qui maxime ut vitae voluptatem. Provident autem eos et quae molestiae assumenda temporibus.',7770.02,NULL,21,'2001-11-28 07:10:42','2009-12-26 03:04:17'),(99,'et','Porro voluptas quia nemo ipsam id enim. Quos delectus minus voluptatem rerum optio non et. Commodi dignissimos et sed odio corrupti quos itaque.','Quas illum nesciunt quibusdam nihil qui. Esse itaque debitis quidem eum quo velit. Totam qui in eum inventore quo nam temporibus dolores. Cupiditate nulla odio delectus fuga quo est libero.',3905.33,NULL,22,'1996-07-13 08:31:28','2002-06-22 21:25:13'),(100,'architecto','Incidunt iure eveniet mollitia. Assumenda error laborum nisi aut dignissimos sint. Eaque voluptas laborum id.','Nemo deleniti ullam sit repellendus eos vero et. Aliquid ut in et fuga sit quis dolore. Consectetur commodi omnis unde aut eum sint. Natus eligendi illo suscipit voluptatum in laboriosam quia placeat.',5616.40,NULL,14,'1997-10-26 15:02:19','2007-07-12 02:37:09');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `warehouse_goods` WRITE;
/*!40000 ALTER TABLE `warehouse_goods` DISABLE KEYS */;
INSERT INTO `warehouse_goods` VALUES (1,1,55,7,'2002-12-05 14:07:47','2000-12-26 16:03:09'),(2,1,77,7,'2001-03-25 10:25:28','2005-09-19 20:37:04'),(3,2,69,4,'1979-04-08 09:17:17','1995-04-23 04:45:03'),(4,1,57,2,'2007-10-18 04:34:41','1979-02-21 11:38:39'),(5,2,56,9,'1988-06-09 08:11:50','1979-02-18 09:23:36'),(6,1,55,5,'1991-04-21 03:55:51','2011-01-13 14:12:10'),(7,1,87,5,'1987-04-23 13:13:37','1978-05-29 11:54:53'),(8,1,80,4,'2018-11-22 09:19:05','2000-02-10 17:21:30'),(9,1,88,8,'2011-04-09 14:15:48','2001-08-29 12:19:55'),(10,1,98,2,'1980-04-20 19:57:16','1991-05-24 02:24:23'),(11,1,98,9,'2009-10-30 09:47:44','1988-11-26 16:16:29'),(12,1,75,7,'2015-03-20 14:53:22','2011-07-14 13:37:44'),(13,2,69,9,'2017-05-06 21:02:15','1984-02-02 06:20:13'),(14,2,82,10,'2009-07-06 14:04:49','2007-09-12 13:36:46'),(15,2,62,4,'1979-05-03 05:33:02','2002-03-10 06:40:26'),(16,2,54,3,'1979-05-02 11:48:36','1975-01-08 16:05:43'),(17,1,91,10,'1993-05-12 07:14:36','2016-02-01 00:42:43'),(18,2,88,9,'2002-05-24 10:40:03','2012-08-08 23:49:14'),(19,2,79,5,'1997-06-04 17:14:05','1992-11-14 00:25:14'),(20,2,76,4,'1974-09-28 16:31:43','2012-06-28 15:17:36'),(21,1,84,5,'1985-05-01 02:13:58','1992-04-23 11:34:40'),(22,1,85,2,'1974-08-26 10:55:03','2020-04-18 04:43:49'),(23,2,57,10,'2012-05-28 21:05:54','2014-01-23 13:26:34'),(24,2,76,5,'1990-11-09 10:21:40','1991-04-05 19:24:31'),(25,1,59,7,'1988-07-13 12:31:34','2011-04-25 16:43:29'),(26,1,85,9,'2020-09-23 13:22:07','1980-03-15 20:22:05'),(27,1,90,7,'2021-04-25 22:44:22','1979-11-06 18:24:16'),(28,2,61,3,'1998-10-02 20:57:30','2020-03-04 04:43:47'),(29,1,98,2,'1979-03-04 08:07:38','1970-03-22 13:41:54'),(30,2,71,7,'1980-07-13 07:22:58','1996-07-03 17:28:08'),(31,2,92,4,'1972-08-27 13:55:20','2018-05-07 13:29:28'),(32,1,81,7,'2014-05-10 04:09:17','2006-09-02 12:55:17'),(33,1,57,6,'1976-10-24 16:24:41','2018-01-20 05:08:16'),(34,1,88,8,'2009-02-26 09:26:12','1983-09-20 11:04:25'),(35,2,88,3,'2002-03-15 13:44:04','1979-02-01 19:25:10'),(36,1,58,10,'1987-06-10 20:05:37','1998-03-03 19:54:32'),(37,2,87,8,'2012-05-14 06:18:26','1970-05-12 07:52:37'),(38,1,67,7,'2008-01-26 18:46:36','1988-05-18 00:54:40'),(39,2,73,7,'1971-01-06 22:47:56','2004-01-28 21:39:26'),(40,2,86,2,'1993-08-04 07:51:34','1995-09-08 23:11:56'),(41,2,61,6,'2017-04-20 14:37:24','1974-09-30 18:56:29'),(42,2,97,8,'2001-02-10 05:38:22','1984-09-08 16:06:42'),(43,2,81,5,'2016-09-08 13:40:15','1976-05-13 09:22:07'),(44,1,71,7,'1997-06-27 04:36:23','1984-09-07 21:49:42'),(45,2,76,5,'1988-01-02 01:57:54','1990-08-29 15:21:24'),(46,2,71,5,'1974-05-26 21:59:47','1982-10-11 01:33:33'),(47,1,59,5,'2020-11-25 23:56:09','2021-04-21 06:06:22'),(48,1,58,10,'1978-10-02 19:26:02','2017-11-21 01:01:23'),(49,1,56,3,'2011-02-21 04:31:29','1986-01-17 04:16:31'),(50,2,93,3,'1996-11-27 17:04:45','1991-12-06 16:18:09');
/*!40000 ALTER TABLE `warehouse_goods` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `discounts` WRITE;
INSERT INTO myshop.discounts (user_id,user_rank_id,good_id,catalog_id,discount,started_at,finished_at,day_of_week,created_at,updated_at) VALUES
	 (NULL,NULL,NULL,NULL,0.36,'1982-08-18 03:20:16','2005-03-11 12:01:37',NULL,'1974-12-02 04:19:28','2021-09-18 13:05:16'),
	 (1,NULL,75,8,0.74,'1972-10-28 07:02:57','1974-06-07 02:00:29',NULL,'1973-12-29 22:29:40','2021-09-18 13:05:42'),
	 (9,NULL,NULL,NULL,0.14,'1986-01-20 05:59:31','1976-08-03 18:34:30',NULL,'1985-08-28 18:00:59','2006-01-07 02:08:03'),
	 (8,NULL,NULL,NULL,0.57,'2018-12-12 08:37:24','2019-10-13 06:25:55',NULL,'1986-06-22 16:35:01','1991-09-18 23:34:00'),
	 (NULL,NULL,60,5,0.65,'1974-05-14 11:10:22','2008-01-19 07:08:45',NULL,'1998-09-20 06:11:33','1980-02-08 08:35:55'),
	 (9,1,NULL,8,0.85,'2016-11-01 06:41:40','2015-02-25 13:15:32',NULL,'1997-01-18 03:51:26','1977-08-17 14:32:13'),
	 (5,NULL,NULL,1,0.5,'2004-08-30 10:23:57','1993-12-21 23:01:46',NULL,'1970-04-20 02:36:02','1990-04-21 15:21:59'),
	 (NULL,NULL,NULL,NULL,0.16,'2004-08-10 11:08:56','2005-06-09 09:44:11',NULL,'1974-01-16 14:08:47','1993-03-27 15:25:07'),
	 (NULL,NULL,NULL,2,0.11,'1998-10-30 05:43:13','2000-09-17 09:31:41',NULL,'1971-04-26 18:59:21','1981-10-04 14:55:26'),
	 (NULL,5,67,NULL,0.11,'1982-02-24 09:42:44','2004-06-03 19:35:23',NULL,'1985-01-04 11:15:56','1976-10-17 15:40:27');

UNLOCK TABLES;


LOCK TABLES `orders` WRITE;
INSERT INTO myshop.orders (user_id,status,is_paid,payment_id,delivery_id,created_at,updated_at,paid_at,delivery_at,finish_at) VALUES
	 (6,1,NULL,3,3,'1985-03-17 13:49:52','2021-09-18 13:23:19','2016-08-01 14:52:23',NULL,NULL),
	 (2,2,NULL,6,1,'2019-04-05 21:04:38','2021-09-18 13:23:19','1994-12-13 12:27:11','2011-12-24 01:06:57',NULL),
	 (7,2,NULL,4,4,'1971-12-28 00:58:09','2021-09-18 13:23:19',NULL,NULL,NULL),
	 (8,2,NULL,6,4,'2016-03-07 02:05:41','2021-09-18 13:23:19',NULL,'2016-05-13 18:29:11','2014-06-13 12:22:14'),
	 (6,0,NULL,1,4,'2002-11-14 13:24:54','2021-09-18 13:23:19',NULL,NULL,NULL),
	 (4,1,NULL,6,1,'1972-02-14 13:48:59','2021-09-18 13:23:19','2010-09-02 16:21:20','1978-01-28 02:04:40',NULL),
	 (8,0,NULL,6,2,'2005-02-27 23:01:57','1971-06-10 00:47:29',NULL,'1992-04-09 16:12:58','1976-04-27 05:54:43'),
	 (1,1,NULL,3,1,'2015-08-04 14:49:32','2021-09-18 13:23:19','2010-02-13 12:00:37',NULL,'1991-08-13 15:09:59'),
	 (9,1,NULL,2,3,'1975-03-23 18:28:03','2021-09-18 13:23:19',NULL,NULL,'2005-11-18 04:17:34'),
	 (4,0,NULL,1,3,'2007-09-17 07:37:09','2021-09-18 13:23:19',NULL,'2020-02-04 12:35:40','1984-09-26 06:23:46');
UNLOCK TABLES;


LOCK TABLES `orders_goods` WRITE;
/*!40000 ALTER TABLE `orders_goods` DISABLE KEYS */;
INSERT INTO `orders_goods` VALUES (1,1,76,92.42,2,184.84,'1985-11-15 17:22:26','1988-08-06 07:18:37'),(2,2,59,66.77,8,534.16,'1990-04-16 21:43:12','1987-05-30 08:58:08'),(3,3,70,74.00,1,74.00,'2008-09-22 19:13:31','1996-08-18 17:31:57'),(4,4,59,19.50,7,136.50,'1977-03-09 07:11:54','2010-03-09 07:50:44'),(5,5,80,42.42,10,424.20,'1987-08-25 21:24:48','2003-02-03 20:25:37'),(6,6,82,68.71,7,480.97,'1994-12-12 22:29:55','2004-09-16 12:44:00'),(7,7,66,37.90,6,227.40,'1970-05-12 13:21:31','1988-07-13 23:39:27'),(8,8,54,50.04,3,150.12,'1996-10-03 05:06:00','1994-03-29 01:13:50'),(9,9,83,12.00,9,108.00,'1981-03-02 14:36:28','1976-01-24 21:22:33'),(10,10,69,32.74,9,294.66,'2017-11-28 19:23:39','1994-10-03 10:28:13');
/*!40000 ALTER TABLE `orders_goods` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
-- SET foreign_key_checks = 0;
INSERT INTO `reviews` VALUES (1,10,10,82,'Aut quae sit porro illum repellendus. Occaecati consequatur excepturi doloribus voluptates qui et dolorum quis. Et dolorem et alias. Omnis aperiam aut sed maxime.',9),(2,4,7,89,'Et deleniti et ut eligendi. Sapiente laudantium sapiente est voluptatum. Exercitationem quas et alias cupiditate beatae voluptatem sit ut. Incidunt cum amet blanditiis blanditiis.',9),(3,7,1,67,'Porro tempore libero eius qui dolorum. Fugit aliquid minima ratione doloribus perspiciatis magnam.',9),(4,9,7,NULL,'Aliquid maiores aperiam corrupti rem at dignissimos dolor iusto. Dolor quia maxime aut ea ut sit. Consectetur earum quidem voluptates.',9),(5,9,6,NULL,'Facilis ex et laborum maxime. Rerum vel dicta cum.',10),(6,1,7,96,'Qui voluptatem tenetur illum ducimus excepturi est. Voluptas at voluptas quia possimus ut adipisci voluptatem soluta. Vitae atque natus qui aliquam.',2),(7,7,7,65,'Amet error fugiat autem voluptas voluptas voluptas. Enim voluptatem repellendus eum quidem ut labore minima nam. Molestiae quia ut in.',2),(8,5,3,69,'Necessitatibus quasi consequatur odit eius odio qui qui. Quam ad omnis eos odio. Et placeat qui in in odio architecto similique non.',10),(9,3,10,88,'Perferendis consectetur praesentium vel ab veniam rerum hic. Consectetur vel optio voluptatem. Vel architecto molestiae velit ut magni. Aut commodi modi sit ratione.',2),(10,6,3,NULL,'Ut laborum quia non soluta dolore molestias non. Commodi et harum quisquam velit excepturi. Minus esse labore enim fugiat non eaque. Rem qui hic nesciunt illo qui porro ratione.',7);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `delivery` WRITE;
/*!40000 ALTER TABLE `delivery` DISABLE KEYS */;
INSERT INTO `delivery` VALUES (1,7,3,'573 Morissette Manors Apt. 971\nLake Theodore, VT 78075','125313',0),(2,5,2,'51867 Reichel Bridge Suite 321\nBeerborough, ND 65088','114045',1),(3,4,4,'682 Emmet Heights\nCecilton, NC 87191-2283','195395',1),(4,5,2,'146 Herzog Branch Apt. 107\nCleoraview, WI 84869-3680','324147',0),(5,5,1,'8057 Genesis Pass\nShanymouth, WI 16667-2794','427092',1),(6,4,1,'40042 Hauck Springs\nJohnland, SC 03455','256412',1),(7,6,1,'52824 Mante Island Suite 841\nLake Clinton, ND 03011','409321',0),(8,5,4,'978 Effertz Hills\nErickaside, DE 33283-5204','421218',1),(9,10,3,'7184 Aniyah Springs Suite 519\nEast Alveraberg, NV 95184','261969',1),(10,10,2,'22957 Corkery Bridge Apt. 045\nBaileyfurt, NH 10306-8682','333064',1);
/*!40000 ALTER TABLE `delivery` ENABLE KEYS */;
UNLOCK TABLES;
 