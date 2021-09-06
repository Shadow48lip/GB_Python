-- Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех 
-- общался с выбранным пользователем (написал ему сообщений)

SELECT COUNT(*) AS `c`, from_user_id 
FROM messages WHERE to_user_id = 3 GROUP BY from_user_id
ORDER BY c DESC LIMIT 1;


-- Подсчитать общее количество лайков, которые получили пользователи младше 10 лет.
SELECT COUNT(*) FROM likes WHERE user_id IN (
	SELECT user_id FROM profiles
	WHERE TIMESTAMPDIFF(YEAR, birthday , NOW()) < 10
);

-- Определить кто больше поставил лайков (всего): мужчины или женщины.

SELECT 'female' AS gender, COUNT(*) FROM likes WHERE user_id IN (
	SELECT user_id FROM profiles
	WHERE gender = 'f'
)
UNION 
SELECT 'male' AS gender, COUNT(*) FROM likes WHERE user_id IN (
	SELECT user_id FROM profiles
	WHERE gender = 'm'
);