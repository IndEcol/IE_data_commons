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
-- Table structure for table `classification_items`
--

DROP TABLE IF EXISTS `classification_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `classification_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classification_id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `description` text,
  `reference` varchar(255) DEFAULT NULL,
  `attribute1_oto` varchar(255) NOT NULL,
  `attribute2_oto` text,
  `attribute3_oto` varchar(255) DEFAULT NULL,
  `attribute4_oto` varchar(255) DEFAULT NULL,
  `attribute5_anc` varchar(255) DEFAULT NULL,
  `attribute6_anc` varchar(255) DEFAULT NULL,
  `attribute7_anc` varchar(255) DEFAULT NULL,
  `attribute8_anc` varchar(255) DEFAULT NULL,
  `attribute9_anc` varchar(255) DEFAULT NULL,
  `attribute10_anc` varchar(255) DEFAULT NULL,
  `attribute11_anc` varchar(255) DEFAULT NULL,
  `attribute12_anc` varchar(255) DEFAULT NULL,
  `attribute13_anc` varchar(255) DEFAULT NULL,
  `attribute14_anc` varchar(255) DEFAULT NULL,
  `attribute15_anc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UC_classification_items` (`classification_id`,`attribute1_oto`),
  KEY `classification_items_hierarchy` (`parent_id`),
  CONSTRAINT `classification_items_classification_id` FOREIGN KEY (`classification_id`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `classification_items_hierarchy` FOREIGN KEY (`parent_id`) REFERENCES `classification_items` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7767 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
