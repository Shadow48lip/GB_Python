-- Задачи необходимо решить с использованием объединения таблиц

-- Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех 
-- общался с выбранным пользователем (написал ему сообщений).

SELECT COUNT(*) AS `count`, CONCAT(u.firstname,' ', u.lastname) AS `sender`
FROM messages AS m
JOIN users AS u ON u.id = m.from_user_id
WHERE to_user_id = 3 
GROUP BY from_user_id
ORDER BY `count` DESC LIMIT 1;


-- Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..

SELECT COUNT(*) AS `count`
FROM likes AS l
JOIN profiles AS p ON l.user_id = p.user_id
WHERE TIMESTAMPDIFF(YEAR, birthday , NOW()) < 10;

-- Определить кто больше поставил лайков (всего): мужчины или женщины.

SELECT IF(gender='m', 'Male', 'Female') AS gender, COUNT(*) 
FROM likes AS l
JOIN profiles AS p ON l.user_id = p.user_id
GROUP BY p.gender;