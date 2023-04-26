-- Use the 'crowd_count' database
DROP SCHEMA IF EXISTS `admin`;
CREATE SCHEMA `admin`;
USE `admin` ;

CREATE TABLE IF NOT EXISTS `admin`.`adminids` (
  `loginid` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`loginid`))
ENGINE=InnoDB
AUTO_INCREMENT = 1;


INSERT INTO adminids VALUES (101,9999);
