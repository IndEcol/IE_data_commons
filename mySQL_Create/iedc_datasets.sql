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
-- Table structure for table `datasets`
--

DROP TABLE IF EXISTS `datasets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `datasets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dataset_name` varchar(255) NOT NULL,
  `dataset_version` varchar(30) DEFAULT NULL,
  `datagroup_id` int(11) DEFAULT NULL,
  `data_category` int(11) NOT NULL,
  `data_type` int(11) NOT NULL,
  `data_layer` int(11) NOT NULL,
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
  `data_provenance` int(11) NOT NULL,
  `dataset_size` int(11) NOT NULL,
  `comment` text,
  `aspect_1` int(11) NOT NULL,
  `aspect_1_classification` int(11) NOT NULL,
  `aspect_2` int(11) DEFAULT NULL,
  `aspect_2_classification` int(11) DEFAULT NULL,
  `aspect_3` int(11) DEFAULT NULL,
  `aspect_3_classification` int(11) DEFAULT NULL,
  `aspect_4` int(11) DEFAULT NULL,
  `aspect_4_classification` int(11) DEFAULT NULL,
  `aspect_5` int(11) DEFAULT NULL,
  `aspect_5_classification` int(11) DEFAULT NULL,
  `aspect_6` int(11) DEFAULT NULL,
  `aspect_6_classification` int(11) DEFAULT NULL,
  `aspect_7` int(11) DEFAULT NULL,
  `aspect_7_classification` int(11) DEFAULT NULL,
  `aspect_8` int(11) DEFAULT NULL,
  `aspect_8_classification` int(11) DEFAULT NULL,
  `aspect_9` int(11) DEFAULT NULL,
  `aspect_9_classification` int(11) DEFAULT NULL,
  `aspect_10` int(11) DEFAULT NULL,
  `aspect_10_classification` int(11) DEFAULT NULL,
  `aspect_11` int(11) DEFAULT NULL,
  `aspect_11_classification` int(11) DEFAULT NULL,
  `aspect_12` int(11) DEFAULT NULL,
  `aspect_12_classification` int(11) DEFAULT NULL,
  `tupel_notation` varchar(30) NOT NULL,
  `semantic_string_example` text NOT NULL,
  `semantic_string_general` text NOT NULL,
  `type_of_source` int(11) NOT NULL,
  `project_license` int(11) NOT NULL,
  `main_author` varchar(255) NOT NULL,
  `dataset_link` text,
  `dataset_format` varchar(255) NOT NULL,
  `project_report` text,
  `suggested_citation` text NOT NULL,
  `visible` tinyint(1) NOT NULL,
  `access_date` datetime DEFAULT NULL,
  `submission_date` datetime NOT NULL,
  `submitting_user` int(11) NOT NULL,
  `dataset_conversion_info` varchar(255) NOT NULL,
  `review_date` datetime DEFAULT NULL,
  `review_user` int(11) DEFAULT NULL,
  `review_comment` text,
  `reserve1` varchar(255) DEFAULT NULL,
  `reserve2` varchar(255) DEFAULT NULL,
  `reserve3` varchar(255) DEFAULT NULL,
  `reserve4` varchar(255) DEFAULT NULL,
  `reserve5` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UC_datasets` (`dataset_name`,`dataset_version`),
  KEY `datasets_datagroups_id` (`datagroup_id`),
  KEY `datasets_categories_id` (`data_category`),
  KEY `datasets_types_id` (`data_type`),
  KEY `datasets_layers_id` (`data_layer`),
  KEY `datasets_provenance_id` (`data_provenance`),
  KEY `datasets_source_id` (`type_of_source`),
  KEY `datasets_licenses_id` (`project_license`),
  KEY `datasets_submitting_user_id` (`submitting_user`),
  KEY `datasets_reviewing_user_id` (`review_user`),
  KEY `datasets_aspect1` (`aspect_1`),
  KEY `datasets_aspect2` (`aspect_2`),
  KEY `datasets_aspect3` (`aspect_3`),
  KEY `datasets_aspect4` (`aspect_4`),
  KEY `datasets_aspect5` (`aspect_5`),
  KEY `datasets_aspect6` (`aspect_6`),
  KEY `datasets_aspect7` (`aspect_7`),
  KEY `datasets_aspect8` (`aspect_8`),
  KEY `datasets_aspect9` (`aspect_9`),
  KEY `datasets_aspect10` (`aspect_10`),
  KEY `datasets_aspect11` (`aspect_11`),
  KEY `datasets_aspect12` (`aspect_12`),
  KEY `datasets_aspect1_classf` (`aspect_1_classification`),
  KEY `datasets_aspect2_classf` (`aspect_2_classification`),
  KEY `datasets_aspect3_classf` (`aspect_3_classification`),
  KEY `datasets_aspect4_classf` (`aspect_4_classification`),
  KEY `datasets_aspect5_classf` (`aspect_5_classification`),
  KEY `datasets_aspect6_classf` (`aspect_6_classification`),
  KEY `datasets_aspect7_classf` (`aspect_7_classification`),
  KEY `datasets_aspect8_classf` (`aspect_8_classification`),
  KEY `datasets_aspect9_classf` (`aspect_9_classification`),
  KEY `datasets_aspect10_classf` (`aspect_10_classification`),
  KEY `datasets_aspect11_classf` (`aspect_11_classification`),
  KEY `datasets_aspect12_classf` (`aspect_12_classification`),
  CONSTRAINT `datasets_aspect1` FOREIGN KEY (`aspect_1`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect10` FOREIGN KEY (`aspect_10`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect10_classf` FOREIGN KEY (`aspect_10_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect11` FOREIGN KEY (`aspect_11`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect11_classf` FOREIGN KEY (`aspect_11_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect12` FOREIGN KEY (`aspect_12`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect12_classf` FOREIGN KEY (`aspect_12_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect1_classf` FOREIGN KEY (`aspect_1_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect2` FOREIGN KEY (`aspect_2`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect2_classf` FOREIGN KEY (`aspect_2_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect3` FOREIGN KEY (`aspect_3`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect3_classf` FOREIGN KEY (`aspect_3_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect4` FOREIGN KEY (`aspect_4`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect4_classf` FOREIGN KEY (`aspect_4_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect5` FOREIGN KEY (`aspect_5`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect5_classf` FOREIGN KEY (`aspect_5_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect6` FOREIGN KEY (`aspect_6`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect6_classf` FOREIGN KEY (`aspect_6_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect7` FOREIGN KEY (`aspect_7`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect7_classf` FOREIGN KEY (`aspect_7_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect8` FOREIGN KEY (`aspect_8`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect8_classf` FOREIGN KEY (`aspect_8_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_aspect9` FOREIGN KEY (`aspect_9`) REFERENCES `aspects` (`id`),
  CONSTRAINT `datasets_aspect9_classf` FOREIGN KEY (`aspect_9_classification`) REFERENCES `classification_definition` (`id`),
  CONSTRAINT `datasets_categories_id` FOREIGN KEY (`data_category`) REFERENCES `categories` (`id`),
  CONSTRAINT `datasets_datagroups_id` FOREIGN KEY (`datagroup_id`) REFERENCES `datagroups` (`id`),
  CONSTRAINT `datasets_layers_id` FOREIGN KEY (`data_layer`) REFERENCES `layers` (`id`),
  CONSTRAINT `datasets_licenses_id` FOREIGN KEY (`project_license`) REFERENCES `licences` (`id`),
  CONSTRAINT `datasets_provenance_id` FOREIGN KEY (`data_provenance`) REFERENCES `provenance` (`id`),
  CONSTRAINT `datasets_reviewing_user_id` FOREIGN KEY (`review_user`) REFERENCES `users` (`id`),
  CONSTRAINT `datasets_source_id` FOREIGN KEY (`type_of_source`) REFERENCES `source_type` (`id`),
  CONSTRAINT `datasets_submitting_user_id` FOREIGN KEY (`submitting_user`) REFERENCES `users` (`id`),
  CONSTRAINT `datasets_types_id` FOREIGN KEY (`data_type`) REFERENCES `types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
