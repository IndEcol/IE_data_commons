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
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dataset_id` int(11) NOT NULL,
  `aspect1` int(11) NOT NULL,
  `aspect2` int(11) DEFAULT NULL,
  `aspect3` int(11) DEFAULT NULL,
  `aspect4` int(11) DEFAULT NULL,
  `aspect5` int(11) DEFAULT NULL,
  `aspect6` int(11) DEFAULT NULL,
  `aspect7` int(11) DEFAULT NULL,
  `aspect8` int(11) DEFAULT NULL,
  `aspect9` int(11) DEFAULT NULL,
  `aspect10` int(11) DEFAULT NULL,
  `aspect11` int(11) DEFAULT NULL,
  `aspect12` int(11) DEFAULT NULL,
  `value` double DEFAULT NULL,
  `unit_nominator` int(11) NOT NULL,
  `unit_denominator` int(11) DEFAULT NULL,
  `stats_array_1` int(11) DEFAULT NULL,
  `stats_array_2` double DEFAULT NULL,
  `stats_array_3` double DEFAULT NULL,
  `stats_array_4` double DEFAULT NULL,
  `comment` text,
  `reserve1` varchar(255) DEFAULT NULL,
  `reserve2` varchar(255) DEFAULT NULL,
  `reserve3` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `data_datasets_id` (`dataset_id`),
  KEY `data_unitsnom_id` (`unit_nominator`),
  KEY `data_unitsden_id` (`unit_denominator`),
  KEY `data_stats_array_id` (`stats_array_1`),
  KEY `data_aspect_1` (`aspect1`),
  KEY `data_aspect_2` (`aspect2`),
  KEY `data_aspect_3` (`aspect3`),
  KEY `data_aspect_4` (`aspect4`),
  KEY `data_aspect_5` (`aspect5`),
  KEY `data_aspect_6` (`aspect6`),
  KEY `data_aspect_7` (`aspect7`),
  KEY `data_aspect_8` (`aspect8`),
  KEY `data_aspect_9` (`aspect9`),
  KEY `data_aspect_10` (`aspect10`),
  KEY `data_aspect_11` (`aspect11`),
  KEY `data_aspect_12` (`aspect12`),
  CONSTRAINT `data_aspect_1` FOREIGN KEY (`aspect1`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_10` FOREIGN KEY (`aspect10`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_11` FOREIGN KEY (`aspect11`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_12` FOREIGN KEY (`aspect12`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_2` FOREIGN KEY (`aspect2`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_3` FOREIGN KEY (`aspect3`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_4` FOREIGN KEY (`aspect4`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_5` FOREIGN KEY (`aspect5`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_6` FOREIGN KEY (`aspect6`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_7` FOREIGN KEY (`aspect7`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_8` FOREIGN KEY (`aspect8`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_aspect_9` FOREIGN KEY (`aspect9`) REFERENCES `classification_items` (`id`),
  CONSTRAINT `data_datasets_id` FOREIGN KEY (`dataset_id`) REFERENCES `datasets` (`id`),
  CONSTRAINT `data_stats_array_id` FOREIGN KEY (`stats_array_1`) REFERENCES `stats_array` (`id`),
  CONSTRAINT `data_unitsden_id` FOREIGN KEY (`unit_denominator`) REFERENCES `units` (`id`),
  CONSTRAINT `data_unitsnom_id` FOREIGN KEY (`unit_nominator`) REFERENCES `units` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=707469 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-09 15:53:21
