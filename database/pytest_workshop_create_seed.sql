-- CREATE DATABASE `pytest_workshop`;
-- commit;
CREATE TABLE `studios` (
  `idstudios` int NOT NULL AUTO_INCREMENT,
  `studio_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idstudios`),
  UNIQUE KEY `studio_name_UNIQUE` (`studio_name`)
) ENGINE=InnoDB AUTO_INCREMENT=759 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
commit;
CREATE TABLE `disciplines` (
  `iddisciplines` int NOT NULL AUTO_INCREMENT,
  `discipline_name` varchar(45) NOT NULL,
  `studio_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`iddisciplines`),
  UNIQUE KEY `discipline_name_UNIQUE` (`discipline_name`),
  KEY `studio_idx` (`studio_name`),
  CONSTRAINT `studio` FOREIGN KEY (`studio_name`) REFERENCES `studios` (`studio_name`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
commit;
CREATE TABLE `consultants` (
  `idconsultant` int NOT NULL AUTO_INCREMENT,
  `consultant_name` varchar(45) NOT NULL,
  `consultant_title` varchar(45) DEFAULT NULL,
  `consultant_location` varchar(45) DEFAULT NULL,
  `consultant_discipline` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idconsultant`),
  UNIQUE KEY `consultant_name_UNIQUE` (`consultant_name`),
  KEY `discipline_idx` (`consultant_discipline`),
  CONSTRAINT `discipline` FOREIGN KEY (`consultant_discipline`) REFERENCES `disciplines` (`discipline_name`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
commit;