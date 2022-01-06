-- MySQL Script generated by MySQL Workbench
-- Fri Aug 27 11:58:03 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Crypto
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Crypto` ;

-- -----------------------------------------------------
-- Schema Crypto
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Crypto` DEFAULT CHARACTER SET utf8 ;
USE `Crypto` ;

-- -----------------------------------------------------
-- Table `Crypto`.`CryptoCurrencyPair`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Crypto`.`CryptoCurrencyPair` ;

CREATE TABLE IF NOT EXISTS `Crypto`.`CryptoCurrencyPair` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `quotecurrency` VARCHAR(8) NOT NULL,
  `basecurrency` VARCHAR(8) NOT NULL,
  `description` TEXT(128) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Crypto`.`QuoteMap`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Crypto`.`QuoteMap` ;

CREATE TABLE IF NOT EXISTS `Crypto`.`QuoteMap` (
  `quoteref` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cryptocurrencyid` BIGINT(8) UNSIGNED NOT NULL,
  `datafield` VARCHAR(64) NOT NULL,
  `market` VARCHAR(45) NULL,
  PRIMARY KEY (`quoteref`),
  INDEX `FK_CryptoCurrency_idx` (`cryptocurrencyid` ASC) VISIBLE,
  CONSTRAINT `FK_CryptoCurrency`
    FOREIGN KEY (`cryptocurrencyid`)
    REFERENCES `Crypto`.`CryptoCurrencyPair` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Crypto`.`QuoteHistory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Crypto`.`QuoteHistory` ;

CREATE TABLE IF NOT EXISTS `Crypto`.`QuoteHistory` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `timestamp` DATETIME NOT NULL,
  `quote` VARCHAR(45) NOT NULL,
  `quoteref` BIGINT(5) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_quoteref_idx` (`quoteref` ASC) VISIBLE,
  CONSTRAINT `FK_quoteref`
    FOREIGN KEY (`quoteref`)
    REFERENCES `Crypto`.`QuoteMap` (`quoteref`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
