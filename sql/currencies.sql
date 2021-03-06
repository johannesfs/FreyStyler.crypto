-- MySQL Script generated by MySQL Workbench
-- Thu Feb 10 05:57:33 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema RawData
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `RawData` ;

-- -----------------------------------------------------
-- Schema RawData
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `RawData` DEFAULT CHARACTER SET utf8 ;
USE `RawData` ;

-- -----------------------------------------------------
-- Table `RawData`.`StagingYahooPrices`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RawData`.`StagingYahooPrices` ;

CREATE TABLE IF NOT EXISTS `RawData`.`StagingYahooPrices` (
  `Date` DATE NOT NULL,
  `Open` DECIMAL(18,4) NULL,
  `High` DECIMAL(18,4) NULL,
  `Low` DECIMAL(18,4) NULL,
  `Close` DECIMAL(18,4) NULL,
  `Volume` BIGINT(16) NULL,
  `Dividends` DECIMAL(18,4) NULL,
  `Stock splits` DECIMAL(18,4) NULL,
  `ticker` VARCHAR(128) NOT NULL,
  PRIMARY KEY (`Date`, `ticker`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RawData`.`StagingYahooInfo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RawData`.`StagingYahooInfo` ;

CREATE TABLE IF NOT EXISTS `RawData`.`StagingYahooInfo` (
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RawData`.`StagingYahooDividend`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RawData`.`StagingYahooDividend` ;

CREATE TABLE IF NOT EXISTS `RawData`.`StagingYahooDividend` (
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RawData`.`StagingEcbFxRates`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RawData`.`StagingEcbFxRates` ;

CREATE TABLE IF NOT EXISTS `RawData`.`StagingEcbFxRates` (
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RawData`.`Kraken`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RawData`.`Kraken` ;

CREATE TABLE IF NOT EXISTS `RawData`.`Kraken` (
  `unix` BIGINT(10) NOT NULL,
  `open` DECIMAL(18,4) NOT NULL,
  `high` DECIMAL(18,4) NOT NULL,
  `low` DECIMAL(18,4) NOT NULL,
  `close` DECIMAL(18,4) NOT NULL,
  `vwap` DECIMAL(18,4) NULL,
  `volume` DECIMAL(24,8) NOT NULL,
  `tradecount` BIGINT(18) NULL,
  `date` VARCHAR(10) NOT NULL,
  `volume_from` DECIMAL(24,8) NULL,
  PRIMARY KEY (`unix`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
