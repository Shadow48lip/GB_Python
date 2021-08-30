1. Установите СУБД MySQL. Создайте в домашней директории файл .my.cnf, задав в нем логин и пароль, который указывался при установке.

Сервер уже установлен в Докер контейнере. Баз там предполагается несколько, потому не делаю "автологин" этот на практике. 
Но понимаю как это сделать в случае необходимости.

Создаем в домашней директории cd ~ файл my.cnf и там описываем настройки клиента mysql и mysqldump при необходимости.
Там описываем настройки в серкциях [mysql] или сразу [client]
nano ~/.my.cnf
[client]
host=localhost
user=root
password=PASSWORD

chmod 400 ~/.my.cnf


2. Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name.

CREATE DATABASE `example`;
USE `example`
CREATE TABLE `users` (id SERIAL, name VARCHAR(50));

/*
mysql> show tables;
+-------------------+
| Tables_in_example |
+-------------------+
| users             |
+-------------------+
1 row in set (0,01 sec)

mysql> show columns from users;
+-------+-----------------+------+-----+---------+----------------+
| Field | Type            | Null | Key | Default | Extra          |
+-------+-----------------+------+-----+---------+----------------+
| id    | bigint unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(50)     | YES  |     | NULL    |                |
+-------+-----------------+------+-----+---------+----------------+
2 rows in set (0,00 sec)
*/

3. Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample.

Делаем dump в файл 
mysqldump --protocol=tcp  -P 33010 -u root -p example > example_db.dump

создаем базу в клиенте
CREATE DATABASE `sample`;

разворачиваем
mysql --protocol=tcp  -P 33010 -u root -p sample < example_db.dump 

/*
mysql> use sample
Database changed
mysql> show tables;
+------------------+
| Tables_in_sample |
+------------------+
| users            |
+------------------+
1 row in set (0,00 sec)
*/

4. (по желанию) Ознакомьтесь более подробно с документацией утилиты mysqldump. Создайте дамп единственной таблицы help_keyword базы данных mysql. Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.

так как там есть адишники по порядку
mysqldump --protocol=tcp  -P 33010 -u root -p  mysql help_keyword --where="help_keyword_id < 100" > dump.sql




