-- MySQL dump 10.13  Distrib 8.0.33, for macos13 (x86_64)
--
-- Host: localhost    Database: BOT
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `BOT`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `BOT` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `BOT`;

--
-- Table structure for table `ANSWERS_USERS`
--

DROP TABLE IF EXISTS `ANSWERS_USERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ANSWERS_USERS` (
  `ANSWERS_USERS_ID` int NOT NULL AUTO_INCREMENT,
  `USER_ID` int NOT NULL,
  `ANSWER_ID` int NOT NULL,
  `SURVEY_ID` int NOT NULL,
  `QUESTION_ID` int NOT NULL,
  `NUMBER_QUESTION` int NOT NULL,
  PRIMARY KEY (`ANSWERS_USERS_ID`),
  UNIQUE KEY `ANSWERS_USERS_ID_UNIQUE` (`ANSWERS_USERS_ID`),
  KEY `USER_ID` (`USER_ID`),
  CONSTRAINT `answers_users_ibfk_1` FOREIGN KEY (`USER_ID`) REFERENCES `USERS` (`USER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ANSWERS_USERS`
--

LOCK TABLES `ANSWERS_USERS` WRITE;
/*!40000 ALTER TABLE `ANSWERS_USERS` DISABLE KEYS */;
/*!40000 ALTER TABLE `ANSWERS_USERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CONSTANTS`
--

DROP TABLE IF EXISTS `CONSTANTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CONSTANTS` (
  `CONSTANT_ID` int NOT NULL AUTO_INCREMENT,
  `CONSTANT_NAMES` varchar(50) NOT NULL,
  `CONSTANT_VALUES` varchar(250) NOT NULL,
  PRIMARY KEY (`CONSTANT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CONSTANTS`
--

LOCK TABLES `CONSTANTS` WRITE;
/*!40000 ALTER TABLE `CONSTANTS` DISABLE KEYS */;
INSERT INTO `CONSTANTS` VALUES (1,'API_TOKEN_TG','!!!!!___Менять токен ТУТ_____!!!!!!!!!!'),(2,'MY_ID','11111'),(3,'ID','23123'),(4,'TEXT_HI','Привет, это бот который проверит твои знания по английскому языку, а в будущем еще и научит. Используй кнопку помощи, если хочешь узнать что может бот сейчас. Или переходи сразу к тесту и удивись своему уровню!'),(5,'TEXT_HELP','Этот бот умеет переводить словосочетания в инлайн режиме  если упомянуть @ima_bota в сообщениях. А так же запускать тесты. В скором времени будет напоминать о тех словах что нужно выучить.'),(6,'TEXT_ERROR','Ошибка в боте');
/*!40000 ALTER TABLE `CONSTANTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LEVELS`
--

DROP TABLE IF EXISTS `LEVELS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LEVELS` (
  `LEVEL_ID` int NOT NULL AUTO_INCREMENT,
  `LEVEL_NAME` varchar(50) NOT NULL,
  PRIMARY KEY (`LEVEL_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LEVELS`
--

LOCK TABLES `LEVELS` WRITE;
/*!40000 ALTER TABLE `LEVELS` DISABLE KEYS */;
/*!40000 ALTER TABLE `LEVELS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SURVEY_STATUS`
--

DROP TABLE IF EXISTS `SURVEY_STATUS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SURVEY_STATUS` (
  `SURVEY_STATUS_ID` int NOT NULL AUTO_INCREMENT,
  `SURVEY_STATUS` varchar(10) NOT NULL,
  PRIMARY KEY (`SURVEY_STATUS_ID`),
  UNIQUE KEY `SURVEY_STATUS_UNIQUE` (`SURVEY_STATUS`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SURVEY_STATUS`
--

LOCK TABLES `SURVEY_STATUS` WRITE;
/*!40000 ALTER TABLE `SURVEY_STATUS` DISABLE KEYS */;
INSERT INTO `SURVEY_STATUS` VALUES (5,'Deleted'),(2,'Launched'),(4,'Revoked'),(1,'Selected'),(3,'Stoped');
/*!40000 ALTER TABLE `SURVEY_STATUS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SURVEYS`
--

DROP TABLE IF EXISTS `SURVEYS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SURVEYS` (
  `SURVEY_ID` int NOT NULL AUTO_INCREMENT,
  `SURVEY_NAME` varchar(45) NOT NULL,
  `SURVEY_DESCRIPTION` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`SURVEY_ID`),
  UNIQUE KEY `SURVEY_NAME_UNIQUE` (`SURVEY_NAME`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SURVEYS`
--

LOCK TABLES `SURVEYS` WRITE;
/*!40000 ALTER TABLE `SURVEYS` DISABLE KEYS */;
/*!40000 ALTER TABLE `SURVEYS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SURVEYS_ANSWERS`
--

DROP TABLE IF EXISTS `SURVEYS_ANSWERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SURVEYS_ANSWERS` (
  `ANSWER_ID` int NOT NULL AUTO_INCREMENT,
  `NUMBER_ANSWER` int NOT NULL,
  `SURVEY_ID` int NOT NULL,
  `NUMBER_QUESTION` int NOT NULL,
  `ANSWER` varchar(100) NOT NULL,
  PRIMARY KEY (`ANSWER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=370 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SURVEYS_ANSWERS`
--

LOCK TABLES `SURVEYS_ANSWERS` WRITE;
/*!40000 ALTER TABLE `SURVEYS_ANSWERS` DISABLE KEYS */;
/*!40000 ALTER TABLE `SURVEYS_ANSWERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SURVEYS_QUESTIONS`
--

DROP TABLE IF EXISTS `SURVEYS_QUESTIONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SURVEYS_QUESTIONS` (
  `QUESTION_ID` int NOT NULL AUTO_INCREMENT,
  `SURVEY_ID` int NOT NULL,
  `NUMBER_QUESTION` int NOT NULL,
  `SURVEY_QUESTION` varchar(550) NOT NULL,
  PRIMARY KEY (`QUESTION_ID`),
  KEY `SURVEY_ID_idx` (`SURVEY_ID`),
  CONSTRAINT `SURVEY_ID` FOREIGN KEY (`SURVEY_ID`) REFERENCES `SURVEYS` (`SURVEY_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SURVEYS_QUESTIONS`
--

LOCK TABLES `SURVEYS_QUESTIONS` WRITE;
/*!40000 ALTER TABLE `SURVEYS_QUESTIONS` DISABLE KEYS */;
/*!40000 ALTER TABLE `SURVEYS_QUESTIONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SURVEYS_TRUE_ANSWERS`
--

DROP TABLE IF EXISTS `SURVEYS_TRUE_ANSWERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SURVEYS_TRUE_ANSWERS` (
  `TRUE_ANSWER_ID` int NOT NULL AUTO_INCREMENT,
  `SURVEY_ID` int NOT NULL,
  `NUMBER_QUESTION` int NOT NULL,
  `NUMBER_TRUE_ANSWER` int NOT NULL,
  PRIMARY KEY (`TRUE_ANSWER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SURVEYS_TRUE_ANSWERS`
--

LOCK TABLES `SURVEYS_TRUE_ANSWERS` WRITE;
/*!40000 ALTER TABLE `SURVEYS_TRUE_ANSWERS` DISABLE KEYS */;
/*!40000 ALTER TABLE `SURVEYS_TRUE_ANSWERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER_SURVEYS`
--

DROP TABLE IF EXISTS `USER_SURVEYS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USER_SURVEYS` (
  `ID_USER_SURVEY` int NOT NULL AUTO_INCREMENT,
  `ID_USER` int NOT NULL,
  `ID_SURVEY` int NOT NULL,
  `STATUS_SURVEY` int NOT NULL,
  `QUESTION_ID` int NOT NULL,
  `PREVIOUS_QUESTION_ID` int NOT NULL,
  PRIMARY KEY (`ID_USER_SURVEY`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER_SURVEYS`
--

LOCK TABLES `USER_SURVEYS` WRITE;
/*!40000 ALTER TABLE `USER_SURVEYS` DISABLE KEYS */;
/*!40000 ALTER TABLE `USER_SURVEYS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USERS`
--

DROP TABLE IF EXISTS `USERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USERS` (
  `USER_ID` int NOT NULL AUTO_INCREMENT,
  `USER_TG_ID` bigint NOT NULL,
  `USER_FULL_NAME` varchar(45) NOT NULL,
  `USER_LEVEL` int NOT NULL DEFAULT '0',
  `USER_ACCESS` int NOT NULL DEFAULT '0',
  `USER_LOGIN` varchar(25) NOT NULL,
  PRIMARY KEY (`USER_ID`),
  UNIQUE KEY `USER_TG_ID_UNIQUE` (`USER_TG_ID`),
  UNIQUE KEY `USER_LOGIN_UNIQUE` (`USER_LOGIN`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USERS`
--

LOCK TABLES `USERS` WRITE;
/*!40000 ALTER TABLE `USERS` DISABLE KEYS */;
/*!40000 ALTER TABLE `USERS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-25  8:35:47
