-- Запросы, процедуры, вьюшки


-- запросим юзеров с заказами
SELECT u.id, u.phone, u.email, o.id AS order_id
FROM users u 
JOIN orders o ON u.id = o.user_id;

-- представление по этому же запросу
CREATE OR REPLACE VIEW user_orders AS
SELECT u.id, u.phone, u.email, o.id AS order_id
FROM users u 
JOIN orders o ON u.id = o.user_id;

-- запрос представление с условием
SELECT * FROM user_orders WHERE phone IS NOT NULL;



-- отзывы о каком товаре
SELECT r.id, g.name, r.score, u.id AS user_id
FROM reviews r 
JOIN goods g ON r.good_id = g.id 
JOIN users u ON r.user_id = u.id

-- представление
CREATE OR REPLACE VIEW user_reviews AS
SELECT r.id, g.name, r.score, u.id AS user_id, CONCAT(SUBSTR(r.description, 1, 50), '...') AS mini_descr
FROM reviews r 
JOIN goods g ON r.good_id = g.id 
JOIN users u ON r.user_id = u.id

-- запрос представление с условием
SELECT user_id, name, mini_descr AS good_name FROM user_reviews;



-- группировки. сколько выбрали какие методы доставки
SELECT COUNT(*), dm.name 
FROM delivery d 
JOIN delivery_methods dm ON d.delivery_met_id = dm.id
GROUP BY d.delivery_met_id;


-- Функция которая возвращает количество заказаов у пользователя
-- Триггер уже создан в DDL командах


DELIMITER //
DROP FUNCTION IF EXISTS orders_by_user//
CREATE FUNCTION orders_by_user (uid BIGINT)
RETURNS INT DETERMINISTIC
BEGIN
	DECLARE orders_count INT;
	SET orders_count = 0;

	SELECT COUNT(*) INTO orders_count FROM orders WHERE user_id = uid;

	RETURN orders_count;
END//

DELIMITER ;

SELECT id, orders_by_user(id) AS orders_count FROM users;