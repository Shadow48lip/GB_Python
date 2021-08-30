DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
	`id` SERIAL PRIMARY KEY,
	`user_id` BIGINT UNSIGNED DEFAULT NULL,
	`annotation` varchar(255) NOT NULL COMMENT 'Аннотация',
    `body` TEXT,
    `created_at` DATETIME DEFAULT NOW(),
    `num_views` INT DEFAULT '0',
    
	INDEX user_id(user_id),
    FOREIGN KEY (user_id) REFERENCES users(id)

);


DROP TABLE IF EXISTS `posts_comments`;
CREATE TABLE `posts_comments` (
	`id` SERIAL PRIMARY KEY,
	`user_id` BIGINT UNSIGNED DEFAULT NULL,
	`post_id` BIGINT UNSIGNED DEFAULT NULL,
	`body` varchar(255) COMMENT 'Короткий коментарий',
    `created_at` DATETIME DEFAULT NOW(),

   	INDEX post_id(post_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES posts(id)

);


DROP TABLE IF EXISTS `users_ban`;
CREATE TABLE `users_ban` (
	`id` SERIAL PRIMARY KEY,
	`user_id` BIGINT UNSIGNED DEFAULT NULL,
	`reason` varchar(255) COMMENT 'Причина накащания',
	`type` ENUM('login', 'posts', 'messages', 'media') COMMENT 'Что запрещаем делать',
    `created_at` DATETIME DEFAULT NOW(),
    `duration__up_to` DATETIME DEFAULT NULL COMMENT 'Когда бан закончится',

    INDEX user_id_duration(user_id, duration__up_to) COMMENT 'Для быстрой проверки действия Бана',
    FOREIGN KEY (user_id) REFERENCES users(id)

) COMMENT 'Наказания пользователя';