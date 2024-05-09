-- CREATE DATABASE `assessment_testing` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
CREATE TABLE `studio` (
  `idstudio` int NOT NULL AUTO_INCREMENT,
  `studio_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idstudio`),
  UNIQUE KEY `studio_name_UNIQUE` (`studio_name`)
) ENGINE=InnoDB AUTO_INCREMENT=759 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `discipline` (
  `iddiscipline` int NOT NULL AUTO_INCREMENT,
  `discipline_name` varchar(45) NOT NULL,
  PRIMARY KEY (`iddiscipline`),
  UNIQUE KEY `discipline_name_UNIQUE` (`discipline_name`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `studio_discipline` (
  `studio_id` int NOT NULL,
  `discipline_id` int NOT NULL,
  PRIMARY KEY (`studio_id`,`discipline_id`),
  KEY `discipline_id_idx` (`discipline_id`),
  CONSTRAINT `discipline` FOREIGN KEY (`discipline_id`) REFERENCES `discipline` (`iddiscipline`),
  CONSTRAINT `studio` FOREIGN KEY (`studio_id`) REFERENCES `studio` (`idstudio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `assessment_form` (
  `idassessment_form` int NOT NULL AUTO_INCREMENT,
  `assessment_form_title` varchar(45) NOT NULL,
  `discipline_name` varchar(45) DEFAULT NULL,
  `assessment_formcol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idassessment_form`),
  KEY `discipline_id_idx` (`discipline_name`),
  CONSTRAINT `discipline_id` FOREIGN KEY (`discipline_name`) REFERENCES `discipline` (`discipline_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `category` (
  `idcategory` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(45) DEFAULT NULL,
  `category_descriptoin` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idcategory`),
  UNIQUE KEY `idcategory_UNIQUE` (`idcategory`),
  UNIQUE KEY `category_name_UNIQUE` (`category_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `assessment_form_categories` (
  `assessment_form_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`assessment_form_id`,`category_id`),
  KEY `category_idx` (`category_id`),
  CONSTRAINT `assessment_form` FOREIGN KEY (`assessment_form_id`) REFERENCES `assessment_form` (`idassessment_form`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `key_areas` (
  `idkey_area` int NOT NULL AUTO_INCREMENT,
  `key_area_name` varchar(45) NOT NULL,
  `key_area_description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idkey_area`,`key_area_name`),
  UNIQUE KEY `key_area_name_UNIQUE` (`key_area_name`),
  UNIQUE KEY `idkey_area_UNIQUE` (`idkey_area`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `assessment_form_key_areas` (
  `assessment_form_id` int NOT NULL,
  `category_id` int NOT NULL,
  `key_area_id` int NOT NULL,
  `sequence` int DEFAULT NULL,
  PRIMARY KEY (`category_id`,`assessment_form_id`,`key_area_id`),
  KEY `assessment_form_id_idx` (`assessment_form_id`),
  KEY `key_area_idx` (`key_area_id`),
  CONSTRAINT `af` FOREIGN KEY (`assessment_form_id`) REFERENCES `assessment_form` (`idassessment_form`),
  CONSTRAINT `cat` FOREIGN KEY (`category_id`) REFERENCES `category` (`idcategory`),
  CONSTRAINT `ka` FOREIGN KEY (`key_area_id`) REFERENCES `key_areas` (`idkey_area`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `maturity_level` (
  `idmaturity_level` int NOT NULL AUTO_INCREMENT,
  `maturity_level_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idmaturity_level`),
  UNIQUE KEY `maturity_level_name_UNIQUE` (`maturity_level_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `checkpoints` (
  `idcheckpoints` int NOT NULL AUTO_INCREMENT,
  `checkpoint_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idcheckpoints`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `assessment_form_checkpoints` (
  `checkpoint_id` int NOT NULL,
  `sequence` varchar(45) NOT NULL,
  `maturity_level_id` int NOT NULL,
  `key_area_id` int NOT NULL,
  `assessment_form_id` int NOT NULL,
  PRIMARY KEY (`checkpoint_id`,`sequence`,`maturity_level_id`,`key_area_id`,`assessment_form_id`),
  KEY `key_area_id_idx` (`key_area_id`),
  KEY `maturity_id_idx` (`maturity_level_id`),
  KEY `assessment_form_idx` (`assessment_form_id`),
  CONSTRAINT `afc_assessment_form` FOREIGN KEY (`assessment_form_id`) REFERENCES `assessment_form` (`idassessment_form`),
  CONSTRAINT `afc_checkpoint` FOREIGN KEY (`checkpoint_id`) REFERENCES `checkpoints` (`idcheckpoints`),
  CONSTRAINT `afc_key_area` FOREIGN KEY (`key_area_id`) REFERENCES `key_areas` (`idkey_area`),
  CONSTRAINT `afc_maturity_level` FOREIGN KEY (`maturity_level_id`) REFERENCES `maturity_level` (`idmaturity_level`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
