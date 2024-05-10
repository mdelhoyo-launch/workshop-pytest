CREATE TABLE `studio` (
  `idstudio` int NOT NULL AUTO_INCREMENT,
  `studio_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idstudio`),
  UNIQUE KEY `studio_name_UNIQUE` (`studio_name`)
) ENGINE=InnoDB AUTO_INCREMENT=759 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
commit;
CREATE TABLE `discipline` (
  `iddiscipline` int NOT NULL AUTO_INCREMENT,
  `discipline_name` varchar(45) NOT NULL,
  `studio_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`iddiscipline`),
  UNIQUE KEY `discipline_name_UNIQUE` (`discipline_name`),
  KEY `studio_idx` (`studio_name`),
  CONSTRAINT `studio` FOREIGN KEY (`studio_name`) REFERENCES `studio` (`studio_name`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
commit;
CREATE TABLE `consultant` (
  `idconsultant` int NOT NULL AUTO_INCREMENT,
  `consultant_name` varchar(45) NOT NULL,
  `consultant_title` varchar(45) DEFAULT NULL,
  `consultant_location` varchar(45) DEFAULT NULL,
  `consultant_discipline` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idconsultant`),
  UNIQUE KEY `consultant_name_UNIQUE` (`consultant_name`),
  KEY `discipline_idx` (`consultant_discipline`),
  CONSTRAINT `discipline` FOREIGN KEY (`consultant_discipline`) REFERENCES `discipline` (`discipline_name`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
commit;