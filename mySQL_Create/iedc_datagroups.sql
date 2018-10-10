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
-- Table structure for table `datagroups`
--

DROP TABLE IF EXISTS `datagroups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `datagroups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datagroup_name` varchar(255) NOT NULL,
  `datagroup_version` varchar(30) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `data_categories` varchar(255) DEFAULT NULL,
  `data_types` varchar(255) DEFAULT NULL,
  `data_layers` varchar(255) DEFAULT NULL,
  `process_scope` varchar(255) DEFAULT NULL,
  `process_resolution` varchar(255) DEFAULT NULL,
  `product_scope` varchar(255) DEFAULT NULL,
  `product_resolution` varchar(255) DEFAULT NULL,
  `material_scope` varchar(255) DEFAULT NULL,
  `material_resolution` varchar(255) DEFAULT NULL,
  `regional_scope` varchar(255) DEFAULT NULL,
  `regional_resolution` varchar(255) DEFAULT NULL,
  `temporal_scope` varchar(255) DEFAULT NULL,
  `temporal_resolution` varchar(255) DEFAULT NULL,
  `description` text,
  `keywords` varchar(255) NOT NULL,
  `system_definition_picture` varchar(255) DEFAULT NULL,
  `comment` text,
  `type_of_source` int(11) DEFAULT NULL,
  `project_license` int(11) DEFAULT NULL,
  `main_author` varchar(255) DEFAULT NULL,
  `project_link` text,
  `project_report` text,
  `suggested_citation` text,
  `submission_date` datetime NOT NULL,
  `submitting_user` int(11) NOT NULL,
  `reserve1` varchar(255) DEFAULT NULL,
  `reserve2` varchar(255) DEFAULT NULL,
  `reserve3` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UC_datagroups` (`datagroup_name`),
  KEY `datagroups_license_id` (`project_license`),
  KEY `datagroups_sources_id` (`type_of_source`),
  KEY `datagroups_users_id` (`submitting_user`),
  KEY `datagroups_project_id` (`project_id`),
  CONSTRAINT `datagroups_license_id` FOREIGN KEY (`project_license`) REFERENCES `licences` (`id`),
  CONSTRAINT `datagroups_project_id` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`),
  CONSTRAINT `datagroups_sources_id` FOREIGN KEY (`type_of_source`) REFERENCES `source_type` (`id`),
  CONSTRAINT `datagroups_users_id` FOREIGN KEY (`submitting_user`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
