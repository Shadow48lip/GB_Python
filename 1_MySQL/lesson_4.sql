-- # Сервисы для генерации данных
-- # http://filldb.info/
-- # http://www.generatedata.com/
-- # https://sourceforge.net/p/benerator/wiki/Home/
-- # http://www.dominicgiles.com/datagenerator.html
-- #


--  i. Заполнить все таблицы БД vk данными (по 10-20 записей в каждой таблице)

-- Сгенерировал через filldb.info. Тет наверное не стоит прикладывать портянку дампа на несколько экранов.
-- Пример
LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Wilfred','Ledner','zschneider@example.org','3930d0fbab468826a35efe7e06f5073b7b2937d6',79746377673),(2,'Merl','Kerluke','piper.bailey@example.net','1ad1a02d51efe3a533b6398b3a470298098d4b5c',79808814777),(3,'Jackie','Haley','cody88@example.org','0d67b52e7a42a0ee40209a9960490208b3f91162',79091118864),(4,'Maximillian','Stanton','grant.arlo@example.org','18099ddb8d0ec1e48d1b540aff79541de060a843',79534983184),(5,'Leilani','Crist','russ08@example.com','a0052c4526778d63c448ccc03c480d0947f9fd35',79034933905),(6,'Irwin','Kub','iweissnat@example.net','bab89f61736bd65f4fe7defdb078f0ebf3dca768',79544916737),(7,'Vergie','Brakus','douglas.vada@example.net','8bd56eaa1c87f84941b32ed850fac8c498f61436',79753220564),(8,'Leila','Upton','betty20@example.net','80daa6b9757d1ee581b535ba60fedff18586e243',79540460818),(9,'Lia','Hessel','amelia.lesch@example.com','f77a3dfb04688d3013afb1c4faf819fcf7b84e84',79636820184),(10,'Louisa','King','bruen.antonietta@example.com','b43bf6dcd3e0f5ba9f1222b8f205fe6da9b712c4',79839660213);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;


-- ii. Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке
SELECT DISTINCT `firstname` FROM users ORDER BY  `firstname` ASC;


-- iii. Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false). Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)
ALTER TABLE profiles ADD COLUMN is_active ENUM('1','0') DEFAULT '1' NOT NULL;

UPDATE profiles SET is_active='0' WHERE birthday < DATE(NOW() - INTERVAL 18 YEAR);



-- iv. Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)
DELETE FROM messages WHERE created_at > NOW();


-- v. Написать название темы курсового проекта (в комментарии)
-- Пока колеблюсь между тем, что бы сделать что-то более менее оригинальное или более очевидное из примера.

-- Вариант 1 - БД сбора статистики проезда автомобилей по фередаральным трассам.
-- С таблицами вида Трасса (название, протяженность, откуда и куда), Типы авто (легковой. грузовик, автобус),
-- Производитель (название, страна, дата основания), Модель, Автомобиль (номерной знак, модель),
-- Предвижения (когда, в какую сторону ехал автомобиль).
-- А далее можно уже позапрашивать инетересную статистику - какие авто и когда чаще ездять и по каким направлениям.
-- Самы популярные  и так далее.

-- Вариант 2 - Кинопоиск. Фильмы, жанры, режиссеры и актеры, рецензии, баллы, коментарии зрителей и критиков. Ну там
-- моожно бысто насобирать.

-- Как-то так в общем.