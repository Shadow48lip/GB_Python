-- MariaDB dump 10.17  Distrib 10.4.15-MariaDB, for Linux (x86_64)
--
-- Host: mysql.hostinger.ro    Database: u574849695_23
-- ------------------------------------------------------
-- Server version	10.4.15-MariaDB-cll-lve

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `communities`
--

DROP TABLE IF EXISTS `communities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `communities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `admin_user_id` bigint(20) unsigned NOT NULL,
  UNIQUE KEY `id` (`id`),
  KEY `communities_name_idx` (`name`),
  KEY `admin_user_id` (`admin_user_id`),
  CONSTRAINT `communities_ibfk_1` FOREIGN KEY (`admin_user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communities`
--

LOCK TABLES `communities` WRITE;
/*!40000 ALTER TABLE `communities` DISABLE KEYS */;
INSERT INTO `communities` VALUES (1,'quidem',1),(2,'corporis',2),(3,'qui',3),(4,'eligendi',4),(5,'dolorem',5),(6,'sequi',6),(7,'distinctio',7),(8,'enim',8),(9,'quasi',9),(10,'eum',10);
/*!40000 ALTER TABLE `communities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `friend_requests`
--

DROP TABLE IF EXISTS `friend_requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friend_requests` (
  `initiator_user_id` bigint(20) unsigned NOT NULL,
  `target_user_id` bigint(20) unsigned NOT NULL,
  `status` enum('requested','approved','declined','unfriended') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `requested_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`initiator_user_id`,`target_user_id`),
  KEY `target_user_id` (`target_user_id`),
  CONSTRAINT `friend_requests_ibfk_1` FOREIGN KEY (`initiator_user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `friend_requests_ibfk_2` FOREIGN KEY (`target_user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friend_requests`
--

LOCK TABLES `friend_requests` WRITE;
/*!40000 ALTER TABLE `friend_requests` DISABLE KEYS */;
INSERT INTO `friend_requests` VALUES (1,1,'declined','2016-11-22 22:12:39','1982-10-12 11:54:11'),(2,2,'declined','1987-08-16 03:08:57','1982-06-15 16:54:37'),(3,3,'declined','2016-03-06 18:21:59','1992-11-12 20:50:34'),(4,4,'approved','2003-05-26 11:28:56','1972-05-23 12:48:20'),(5,5,'approved','2006-11-24 23:11:21','1982-02-16 10:32:11'),(6,6,'approved','1998-04-20 17:13:36','1979-12-30 23:37:40'),(7,7,'declined','1997-03-23 03:39:01','1971-09-02 14:41:07'),(8,8,'approved','2017-02-25 14:11:01','1986-04-23 21:41:09'),(9,9,'requested','2021-05-01 23:58:32','2012-07-27 08:11:26'),(10,10,'approved','1989-06-05 12:39:28','2020-04-10 18:34:24');
/*!40000 ALTER TABLE `friend_requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `likes` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `media_id` bigint(20) unsigned NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (1,1,1,'2001-12-26 06:54:09'),(2,2,2,'1995-04-03 21:04:21'),(3,3,3,'2015-11-17 01:47:07'),(4,4,4,'1984-08-29 04:28:32'),(5,5,5,'2000-02-14 07:28:12'),(6,6,6,'1979-04-27 06:15:59'),(7,7,7,'2003-12-14 13:42:28'),(8,8,8,'2017-08-18 20:27:17'),(9,9,9,'2001-07-31 19:04:06'),(10,10,10,'1978-09-24 19:48:26'),(11,1,1,'2010-12-06 06:12:46'),(12,2,2,'1984-12-17 20:32:02'),(13,3,3,'1975-09-06 06:02:52'),(14,4,4,'2014-04-27 13:03:25'),(15,5,5,'2009-02-20 06:16:57'),(16,6,6,'1983-01-04 14:11:17'),(17,7,7,'1984-02-21 01:21:50'),(18,8,8,'2001-02-12 03:55:17'),(19,9,9,'1982-08-04 04:45:44'),(20,10,10,'1982-06-27 23:09:31');
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `media`
--

DROP TABLE IF EXISTS `media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `media` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `media_type_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `body` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `filename` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `metadata` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`metadata`)),
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  KEY `media_type_id` (`media_type_id`),
  CONSTRAINT `media_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `media_ibfk_2` FOREIGN KEY (`media_type_id`) REFERENCES `media_types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `media`
--

LOCK TABLES `media` WRITE;
/*!40000 ALTER TABLE `media` DISABLE KEYS */;
INSERT INTO `media` VALUES (1,1,1,'Blanditiis assumenda tenetur hic autem laborum. Enim delectus ea deserunt. Rerum sint eius et veritatis possimus iste. Consequatur rerum quaerat voluptas voluptatum itaque.','aut',727,NULL,'2018-05-17 14:55:13','2005-04-28 22:08:01'),(2,2,2,'Ab nihil sed harum iure repellat iusto doloremque. A excepturi et alias quo ab quas veritatis. Suscipit quis quo quam perferendis officia.','commodi',0,NULL,'1993-02-03 20:04:25','2008-10-12 23:50:27'),(3,3,3,'Consequatur nisi voluptatem reiciendis corporis id vero. Sed repellendus illum vel et. Saepe illo ut voluptas aut aliquid optio.','vel',5367,NULL,'1975-09-18 10:28:33','1991-02-14 02:26:23'),(4,4,4,'Vitae sint voluptates sunt illum neque ut. Voluptatem aut eum illum nisi. Eaque ipsa alias voluptas omnis dolore ad. Commodi tenetur qui quasi consequatur sequi.','porro',0,NULL,'2015-08-15 06:08:36','2014-06-02 22:03:21'),(5,1,5,'Eius aut quis harum rerum aut. Nobis eius magnam quia commodi. Autem adipisci reprehenderit ratione non aut. Dolorem minima velit nam et doloribus fugit ea.','ipsum',4709,NULL,'2012-06-12 21:08:11','2021-08-10 13:05:08'),(6,2,6,'A laudantium suscipit et libero inventore. Qui sit amet quia sed. Ipsum est vel dolore molestias. Quo enim expedita necessitatibus et.','odit',883531,NULL,'1998-06-08 18:57:07','2002-01-04 20:54:20'),(7,3,7,'Quia temporibus qui ducimus ex expedita est. Perspiciatis sit sunt voluptas cumque. Illum voluptas sit voluptates necessitatibus.','recusandae',66,NULL,'1990-11-18 17:26:59','1990-11-29 06:35:57'),(8,4,8,'Aliquid aliquam quae molestiae quis autem voluptas. Qui quo quia quis. Voluptatem id veniam recusandae corporis. Impedit recusandae corporis nisi quasi soluta sit consequatur vitae.','labore',816,NULL,'1971-03-25 07:42:35','1995-12-22 21:12:52'),(9,1,9,'Architecto debitis maxime quae et debitis tempora. Ut rerum aperiam voluptatem numquam magni autem. Perferendis nobis ex modi iste nisi molestias. Pariatur facilis debitis sint molestiae ipsum.','libero',88848,NULL,'2000-11-29 02:51:28','2000-11-13 20:13:25'),(10,2,10,'Iste dolor rerum facere maxime aspernatur dolores numquam eligendi. Doloremque tenetur iure recusandae deserunt veritatis.','atque',9811,NULL,'2008-04-02 01:29:04','1970-03-19 06:07:09');
/*!40000 ALTER TABLE `media` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `media_types`
--

DROP TABLE IF EXISTS `media_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `media_types` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `media_types`
--

LOCK TABLES `media_types` WRITE;
/*!40000 ALTER TABLE `media_types` DISABLE KEYS */;
INSERT INTO `media_types` VALUES (1,'minus','2018-02-03 10:01:01','1992-01-07 22:05:43'),(2,'voluptatem','2006-11-06 22:52:38','1974-06-07 02:27:45'),(3,'consequatur','1982-11-29 13:37:42','1972-11-05 21:46:41'),(4,'doloremque','2004-10-23 04:07:06','2011-07-04 09:11:08');
/*!40000 ALTER TABLE `media_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `from_user_id` bigint(20) unsigned NOT NULL,
  `to_user_id` bigint(20) unsigned NOT NULL,
  `body` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  UNIQUE KEY `id` (`id`),
  KEY `from_user_id` (`from_user_id`),
  KEY `to_user_id` (`to_user_id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`from_user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`to_user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,1,'Quibusdam occaecati nisi vero eos nemo. Ipsa voluptate molestiae voluptatem.','1973-02-08 20:54:20'),(2,2,2,'Quis assumenda vel sapiente nostrum distinctio dolores. Necessitatibus neque et earum sapiente quas eum distinctio ut. Dicta error mollitia nisi ipsa ex non. Facere id libero sunt libero. Aliquid et omnis similique sed quia.','1980-11-17 03:50:46'),(3,3,3,'Dolores laudantium laboriosam neque et. Cupiditate accusamus expedita amet voluptate qui. Consequatur id labore earum molestias et quas. Ipsam corrupti excepturi vero cum qui deleniti asperiores et.','2000-02-11 21:16:59'),(4,4,4,'Ut quis rerum ea sed. Impedit vero ut velit nam. Et labore totam voluptas magnam quaerat. Provident at quis et rem rerum.','2008-11-04 22:47:19'),(5,5,5,'Et sed beatae distinctio. Sequi tempore officiis in laudantium qui est qui. Sed soluta velit aperiam sed culpa est esse ratione.','1980-01-20 01:09:42'),(6,6,6,'Et velit et incidunt veritatis tempora laboriosam ex iure. Quibusdam sed exercitationem nobis. Reiciendis voluptatem quia sunt ad beatae.','1995-10-04 23:38:15'),(7,7,7,'Expedita quia ipsam maxime sed cum quas reprehenderit mollitia. Rem et asperiores quia in qui. Fuga et accusantium nisi cum ad dolore.','1989-11-08 00:45:09'),(8,8,8,'Error tempora placeat magni vel at. Quaerat nam impedit error tenetur fugiat aut. A dicta ut occaecati tenetur alias.','1974-03-07 13:16:37'),(9,9,9,'Occaecati est sit incidunt eaque eos sunt aut. Sed reprehenderit impedit aut fuga animi eum. Sapiente quia eos vel porro quia consequatur explicabo velit. Et aut dolorem tenetur excepturi.','1992-08-07 15:48:27'),(10,10,10,'Quis autem non quisquam minima a consectetur in. Ea tempora minus temporibus unde harum est. Aliquam optio repellendus eum id quisquam iste quasi.','2009-11-06 15:05:38'),(11,1,1,'Placeat sit totam laboriosam commodi. Ipsa voluptas ea labore. Voluptas impedit quae aperiam et provident.','1972-02-25 16:59:25'),(12,2,2,'Quibusdam commodi blanditiis vel eius aliquid tempora voluptatem. Ad commodi molestiae quisquam est magnam. Et sed et quo. Soluta voluptates in itaque similique eius eum.','1992-04-03 09:10:12'),(13,3,3,'Natus impedit dolorum voluptatum ad et. Voluptas aut magni sed et voluptatem at laudantium. Omnis tempore non nulla distinctio expedita. Excepturi blanditiis quae explicabo harum nihil. Architecto sunt sint ipsam et maiores officia eaque.','1992-08-09 19:35:44'),(14,4,4,'Et ab accusantium id sunt doloribus ad. Culpa doloribus eum quasi. Sint aut sint voluptatum nemo dolor.','2009-02-15 02:38:28'),(15,5,5,'Sequi numquam sint sequi autem velit non. Sit et minus est nihil explicabo nam odit aut. Nam omnis voluptatem qui tempore. Excepturi corporis eos et maxime esse laborum natus.','1990-07-21 21:17:35'),(16,6,6,'Non qui fuga quis quis possimus debitis quia. Vel quis nostrum aut quia harum itaque. Ratione minima magni quod est. Esse delectus provident saepe. Officia odio et temporibus consequatur illum odio non.','2017-12-17 08:34:13'),(17,7,7,'In doloribus facilis temporibus perferendis voluptas ab aliquid. Autem ea eveniet deleniti est omnis id.','1989-03-20 17:54:31'),(18,8,8,'Error quis exercitationem quibusdam voluptas labore. Eos quas omnis sunt eum molestias ullam. Quas commodi voluptatem laboriosam rem earum.','1998-12-01 12:01:27'),(19,9,9,'Vel qui optio ut et. Fugit consequatur et id perspiciatis voluptatem id sunt. Tempore in soluta consequatur qui explicabo et.','1971-03-06 07:21:42'),(20,10,10,'Doloribus ut enim est recusandae sequi dolorum quos. Dolores possimus ea et deleniti quia voluptas. Voluptas dolorem non libero voluptatem molestiae minima labore. Optio officiis est nisi optio ut rerum soluta.','2017-12-31 23:05:31');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photo_albums`
--

DROP TABLE IF EXISTS `photo_albums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `photo_albums` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_id` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `photo_albums_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photo_albums`
--

LOCK TABLES `photo_albums` WRITE;
/*!40000 ALTER TABLE `photo_albums` DISABLE KEYS */;
INSERT INTO `photo_albums` VALUES (1,'deleniti',1),(2,'consequatur',2),(3,'odit',3),(4,'et',4),(5,'quos',5),(6,'aspernatur',6),(7,'iste',7),(8,'et',8),(9,'modi',9),(10,'quod',10);
/*!40000 ALTER TABLE `photo_albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photos`
--

DROP TABLE IF EXISTS `photos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `photos` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `album_id` bigint(20) unsigned DEFAULT NULL,
  `media_id` bigint(20) unsigned NOT NULL,
  UNIQUE KEY `id` (`id`),
  KEY `album_id` (`album_id`),
  KEY `media_id` (`media_id`),
  CONSTRAINT `photos_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `photo_albums` (`id`),
  CONSTRAINT `photos_ibfk_2` FOREIGN KEY (`media_id`) REFERENCES `media` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photos`
--

LOCK TABLES `photos` WRITE;
/*!40000 ALTER TABLE `photos` DISABLE KEYS */;
INSERT INTO `photos` VALUES (1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5),(6,6,6),(7,7,7),(8,8,8),(9,9,9),(10,10,10),(11,1,1),(12,2,2),(13,3,3),(14,4,4),(15,5,5),(16,6,6),(17,7,7),(18,8,8),(19,9,9),(20,10,10);
/*!40000 ALTER TABLE `photos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles` (
  `user_id` bigint(20) unsigned NOT NULL,
  `gender` char(1) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `photo_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `hometown` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles`
--

LOCK TABLES `profiles` WRITE;
/*!40000 ALTER TABLE `profiles` DISABLE KEYS */;
INSERT INTO `profiles` VALUES (1,'m','2000-07-27',1,'1975-07-16 16:28:23',NULL),(2,'f','2013-01-27',2,'2002-12-16 13:59:24',NULL),(3,'m','1991-01-06',3,'1986-12-23 12:02:45',NULL),(4,'m','2013-11-18',4,'2006-01-01 19:37:59',NULL),(5,'m','1979-08-21',5,'1978-12-27 17:26:41',NULL),(6,'f','1991-04-29',6,'1972-07-12 20:06:31',NULL),(7,'f','1979-09-08',7,'2009-09-09 01:44:25',NULL),(8,'f','1999-09-15',8,'1984-09-14 05:53:16',NULL),(9,'m','1973-03-26',9,'2001-02-24 14:27:53',NULL),(10,'f','1970-04-25',10,'2000-09-27 11:39:28',NULL);
/*!40000 ALTER TABLE `profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lastname` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Фамиль',
  `email` varchar(120) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password_hash` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  KEY `users_firstname_lastname_idx` (`firstname`,`lastname`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='юзеры';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Wilfred','Ledner','zschneider@example.org','3930d0fbab468826a35efe7e06f5073b7b2937d6',79746377673),(2,'Merl','Kerluke','piper.bailey@example.net','1ad1a02d51efe3a533b6398b3a470298098d4b5c',79808814777),(3,'Jackie','Haley','cody88@example.org','0d67b52e7a42a0ee40209a9960490208b3f91162',79091118864),(4,'Maximillian','Stanton','grant.arlo@example.org','18099ddb8d0ec1e48d1b540aff79541de060a843',79534983184),(5,'Leilani','Crist','russ08@example.com','a0052c4526778d63c448ccc03c480d0947f9fd35',79034933905),(6,'Irwin','Kub','iweissnat@example.net','bab89f61736bd65f4fe7defdb078f0ebf3dca768',79544916737),(7,'Vergie','Brakus','douglas.vada@example.net','8bd56eaa1c87f84941b32ed850fac8c498f61436',79753220564),(8,'Leila','Upton','betty20@example.net','80daa6b9757d1ee581b535ba60fedff18586e243',79540460818),(9,'Lia','Hessel','amelia.lesch@example.com','f77a3dfb04688d3013afb1c4faf819fcf7b84e84',79636820184),(10,'Louisa','King','bruen.antonietta@example.com','b43bf6dcd3e0f5ba9f1222b8f205fe6da9b712c4',79839660213);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_communities`
--

DROP TABLE IF EXISTS `users_communities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_communities` (
  `user_id` bigint(20) unsigned NOT NULL,
  `community_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`user_id`,`community_id`),
  KEY `community_id` (`community_id`),
  CONSTRAINT `users_communities_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `users_communities_ibfk_2` FOREIGN KEY (`community_id`) REFERENCES `communities` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_communities`
--

LOCK TABLES `users_communities` WRITE;
/*!40000 ALTER TABLE `users_communities` DISABLE KEYS */;
INSERT INTO `users_communities` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10);
/*!40000 ALTER TABLE `users_communities` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-24 18:43:54
