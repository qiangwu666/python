-- MySQL dump 10.16  Distrib 10.1.36-MariaDB, for Win32 (AMD64)
--
-- Host: localhost    Database: blogdb
-- ------------------------------------------------------
-- Server version	10.1.36-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id鍙?,
  `title` varchar(88) NOT NULL COMMENT '鏍囬',
  `abstract` varchar(200) NOT NULL COMMENT '鎽樿',
  `content` text NOT NULL COMMENT '鍗氭枃鍐呭',
  `uid` int(10) unsigned DEFAULT NULL COMMENT '鐢ㄦ埛鏍囪瘑',
  `pcount` int(10) unsigned DEFAULT '0' COMMENT '鐐硅禐鏁?,
  `flag` tinyint(3) unsigned DEFAULT '0' COMMENT '0鏂板缓锛?鍙戝竷锛?鍒犻櫎',
  `cdate` datetime DEFAULT NULL COMMENT '鍒涘缓鏃堕棿',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'bioati1','zhaiyao1','mouwenneirong1',1,5,1,'2018-09-13 08:50:20'),(2,'bioati2','zhaiyao2','mouwenneirong2',2,25,1,'2028-06-23 08:50:26'),(3,'bioati3','zhaiyao3','mouwenneirong3',3,31,1,'2038-06-23 08:50:26'),(4,'bioati4','zhaiyao4','mouwenneirong4',4,21,1,'2032-11-13 08:50:26'),(5,'bioati5','zhaiyao5','mouwenneirong5',5,1,1,'2032-11-13 08:22:16'),(6,'bioati6','zhaiyao6','mouwenneirong6',5,9,1,'2032-11-13 02:02:16'),(7,'bioati7','zhaiyao7','mouwenneirong7',2,11,1,'2032-11-13 02:02:36'),(8,'bioati8','zhaiyao8','mouwenneirong8',3,21,1,'2032-01-13 12:02:36'),(9,'bioati9','zhaiyao9','mouwenneirong9',7,21,1,'2099-01-13 12:02:36'),(10,'bioati10','zhaiyao10','mouwenneirong10',6,21,1,'2029-01-13 12:02:36'),(11,'bioati11','zhaiyao11','mouwenneirong11',4,8,1,'2029-11-23 07:02:36'),(12,'bioati12','zhaiyao12','mouwenneirong12',2,1,1,'2020-11-13 12:02:36'),(13,'bioati13','zhaiyao13','mouwenneirong13',2,8,0,'2029-11-23 07:02:36');
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id鍙?,
  `name` varchar(32) NOT NULL COMMENT '濮撳悕',
  `email` varchar(66) DEFAULT NULL COMMENT '閭鍦板潃',
  `cdate` datetime DEFAULT NULL COMMENT '娉ㄥ唽鏃堕棿',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'zhangsan','1qq.com','2018-09-05 14:56:25'),(2,'lisi','2qq.com','2017-10-05 14:50:05'),(3,'wagnwu','3qq.com','2018-09-15 16:21:45'),(4,'zhaoliu','4qq.com','2012-11-15 16:29:35'),(5,'qiangwu','5qq.com','2018-09-15 22:22:55'),(6,'xiaoming','6qq.com','2008-11-11 20:20:57'),(7,'jingfeng','7qq.com','2066-12-21 10:50:57'),(8,'xiaogou','8qq.com','2014-08-01 10:06:07'),(9,'xiaochen','9qq.com','2004-06-21 23:06:57');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-31 11:05:42
