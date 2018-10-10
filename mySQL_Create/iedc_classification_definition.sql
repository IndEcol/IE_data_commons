-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: iedc
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `classification_definition`
--

DROP TABLE IF EXISTS `classification_definition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `classification_definition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classification_name` varchar(255) NOT NULL,
  `dimension` int(11) NOT NULL,
  `description` text,
  `mutually_exclusive` tinyint(1) NOT NULL,
  `collectively_exhaustive` tinyint(1) NOT NULL,
  `general` tinyint(1) NOT NULL,
  `created_from_dataset` tinyint(1) NOT NULL,
  `reference` text,
  `reserve1` varchar(255) DEFAULT NULL,
  `reserve2` varchar(255) DEFAULT NULL,
  `reserve3` varchar(255) DEFAULT NULL,
  `meaning_attribute1` varchar(255) NOT NULL,
  `meaning_attribute2` varchar(255) DEFAULT NULL,
  `meaning_attribute3` varchar(255) DEFAULT NULL,
  `meaning_attribute4` varchar(255) DEFAULT NULL,
  `meaning_attribute5` varchar(255) DEFAULT NULL,
  `meaning_attribute6` varchar(255) DEFAULT NULL,
  `meaning_attribute7` varchar(255) DEFAULT NULL,
  `meaning_attribute8` varchar(255) DEFAULT NULL,
  `meaning_attribute9` varchar(255) DEFAULT NULL,
  `meaning_attribute10` varchar(255) DEFAULT NULL,
  `meaning_attribute11` varchar(255) DEFAULT NULL,
  `meaning_attribute12` varchar(255) DEFAULT NULL,
  `meaning_attribute13` varchar(255) DEFAULT NULL,
  `meaning_attribute14` varchar(255) DEFAULT NULL,
  `meaning_attribute15` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UC_classification_definition` (`classification_name`),
  KEY `classification_dimension_id` (`dimension`),
  CONSTRAINT `classification_dimension_id` FOREIGN KEY (`dimension`) REFERENCES `dimensions` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-09 15:53:22
