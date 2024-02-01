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
  `ANSWER_ID` int NOT NULL,
  `ID_USER_SURVEY` int NOT NULL,
  `NUMBER_QUESTION` int NOT NULL,
  PRIMARY KEY (`ANSWERS_USERS_ID`),
  UNIQUE KEY `ANSWERS_USERS_ID_UNIQUE` (`ANSWERS_USERS_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=290 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


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
INSERT INTO `CONSTANTS` VALUES (1,'API_TOKEN_TG',!!!!!СЮДА ВБИВАТЬ ТОКЕН В ОДИНАРНЫХ КОВЫЧКАХ),(2,'MY_ID','ВАШ ИД'),(3,'ID','ИД ГРУППЫ'),(4,'TEXT_HI','Привет, @FIO! Это бот который проверит твои знания по английскому языку, а в будущем еще и научит. Используй кнопку помощи, если хочешь узнать что может бот сейчас. Или переходи сразу к тесту и удивись своему уровню!'),(5,'TEXT_HELP','Этот бот умеет переводить словосочетания в инлайн режиме  если упомянуть @English_bot_help_HW_bot в сообщениях. А так же запускать тесты. В скором времени будет напоминать о тех словах что нужно выучить.'),(6,'TEXT_ERROR','Ошибка в боте');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SURVEY_STATUS`
--

LOCK TABLES `SURVEY_STATUS` WRITE;
/*!40000 ALTER TABLE `SURVEY_STATUS` DISABLE KEYS */;
INSERT INTO `SURVEY_STATUS` VALUES (5,'Completed'),(6,'Deleted'),(2,'Launched'),(4,'Revoked'),(1,'Selected'),(3,'Stoped');
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SURVEYS`
--

LOCK TABLES `SURVEYS` WRITE;
/*!40000 ALTER TABLE `SURVEYS` DISABLE KEYS */;
INSERT INTO `SURVEYS` VALUES (1,'miniTest','Маленький проверочный тест для проверки всего'),(2,'Test2','Test for testing'),(17,'English Level test. Grammar','Проверка грамматики');
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
INSERT INTO `SURVEYS_ANSWERS` VALUES (1,1,1,1,'How do you'),(2,2,1,1,'How are you'),(3,3,1,1,'How you are'),(4,4,1,1,'How is it'),(5,1,1,2,'you'),(6,2,1,2,'your'),(7,3,1,2,'yours'),(8,4,1,2,'you\'re'),(9,1,1,3,'I twenty'),(10,2,1,3,'Me is twenty'),(11,3,1,3,'I\'ve twenty'),(12,4,1,3,'I\'m twenty'),(13,1,1,4,'No, it isn\'t'),(14,2,1,4,'No, isn\'t it'),(15,3,1,4,'No, he isn\'t'),(16,4,1,4,'No, there isn\'t'),(17,1,1,5,'It is'),(18,2,1,5,'Her is'),(19,3,1,5,'He is'),(20,4,1,5,'She is'),(21,1,1,6,'How'),(22,2,1,6,'Who'),(23,3,1,6,'What'),(24,4,1,6,'That'),(25,1,1,7,'His'),(26,2,1,7,'He\'s'),(27,3,1,7,'He'),(28,4,1,7,'Her'),(34,1,2,1,'...'),(35,2,2,1,'Doctor'),(36,3,2,1,'Vadim'),(37,4,2,1,'Volan de Mort'),(42,1,2,2,'I'),(43,2,2,2,'You'),(44,3,2,2,'Vadim'),(45,4,2,2,'Volan de Mort'),(50,1,17,1,'How do you'),(51,2,17,1,'How are you'),(52,3,17,1,'How you are'),(53,4,17,1,'How is it'),(54,1,17,2,'you'),(55,2,17,2,'your'),(56,3,17,2,'yours'),(57,4,17,2,'you\'re'),(58,1,17,3,'I twenty'),(59,2,17,3,'Me is twenty'),(60,3,17,3,'I\'ve twenty'),(61,4,17,3,'I\'m twenty'),(62,1,17,4,'No, it isn\'t'),(63,2,17,4,'No, isn\'t it'),(64,3,17,4,'No, he isn\'t'),(65,4,17,4,'No, there isn\'t'),(66,1,17,5,'It is'),(67,2,17,5,'Her is'),(68,3,17,5,'He is'),(69,4,17,5,'She is'),(70,1,17,6,'How'),(71,2,17,6,'Who'),(72,3,17,6,'What'),(73,4,17,6,'That'),(74,1,17,7,'His'),(75,2,17,7,'He\'s'),(76,3,17,7,'He'),(77,4,17,7,'Her'),(78,1,17,8,'aren\'t'),(79,2,17,8,'isn\'t'),(80,3,17,8,'not'),(81,4,17,8,'doesn\'t'),(82,1,17,9,'They'),(83,2,17,9,'Their'),(84,3,17,9,'Them'),(85,4,17,9,'This'),(86,1,17,10,'I got'),(87,2,17,10,'I\'ve got'),(88,3,17,10,'I\'ve'),(89,4,17,10,'I have'),(90,1,17,11,'They are'),(91,2,17,11,'It is'),(92,3,17,11,'There are'),(93,4,17,11,'There is'),(94,1,17,12,'I live'),(95,2,17,12,'I don\'t'),(96,3,17,12,'I do live'),(97,4,17,12,'I do'),(98,1,17,13,'they'),(99,2,17,13,'their'),(100,3,17,13,'there'),(101,4,17,13,'they\'re'),(102,1,17,14,'Where'),(103,2,17,14,'How big'),(104,3,17,14,'How much'),(105,4,17,14,'What'),(106,1,17,15,'a actress'),(107,2,17,15,'actress'),(108,3,17,15,'the actress'),(109,4,17,15,'an actress'),(110,1,17,16,'Which is'),(111,2,17,16,'Who\'s'),(112,3,17,16,'When\'s'),(113,4,17,16,'Where\'s'),(114,1,17,17,'Whose'),(115,2,17,17,'What\'s'),(116,3,17,17,'Who\'s'),(117,4,17,17,'Who'),(118,1,17,18,'They are'),(119,2,17,18,'There are'),(120,3,17,18,'There is'),(121,4,17,18,'It is'),(122,1,17,19,'got'),(123,2,17,19,'have got'),(124,3,17,19,'has got'),(125,4,17,19,'is got'),(126,1,17,20,'How much'),(127,2,17,20,'How old'),(128,3,17,20,'How are'),(129,4,17,20,'How many'),(130,1,17,21,'No, there isn\'t'),(131,2,17,21,'Yes, there is any'),(132,3,17,21,'Yes, they is'),(133,4,17,21,'No, there aren\'t'),(134,1,17,22,'they'),(135,2,17,22,'them'),(136,3,17,22,'it'),(137,4,17,22,'some'),(138,1,17,23,'many'),(139,2,17,23,'a lot'),(140,3,17,23,'much'),(141,4,17,23,'the many'),(142,1,17,24,'some children'),(143,2,17,24,'any children'),(144,3,17,24,'a children'),(145,4,17,24,'one children'),(146,1,17,25,'don\'t speak'),(147,2,17,25,'not'),(148,3,17,25,'speak not'),(149,4,17,25,'don\'t'),(150,1,17,26,'He\'s teacher'),(151,2,17,26,'He\'s a teacher'),(152,3,17,26,'He\'s teaching'),(153,4,17,26,'Yes, he does'),(154,1,17,27,'working'),(155,2,17,27,'works'),(156,3,17,27,'work'),(157,4,17,27,'am working'),(158,1,17,28,'to shop'),(159,2,17,28,'shop'),(160,3,17,28,'to shopping'),(161,4,17,28,'shopping'),(162,1,17,29,'at'),(163,2,17,29,'to'),(164,3,17,29,'in'),(165,4,17,29,'on'),(166,1,17,30,'at'),(167,2,17,30,'to'),(168,3,17,30,'in'),(169,4,17,30,'on'),(170,1,17,31,'at'),(171,2,17,31,'to'),(172,3,17,31,'in'),(173,4,17,31,'on'),(174,1,17,32,'at'),(175,2,17,32,'to'),(176,3,17,32,'in'),(177,4,17,32,'on'),(178,1,17,33,'By car'),(179,2,17,33,'In car'),(180,3,17,33,'By the car'),(181,4,17,33,'On car'),(182,1,17,34,'Yes, I likes'),(183,2,17,34,'Yes, I like'),(184,3,17,34,'Yes, I does'),(185,4,17,34,'Yes, I do'),(186,1,17,35,'is stand'),(187,2,17,35,'is standing'),(188,3,17,35,'stand'),(189,4,17,35,'standing'),(190,1,17,36,'I like'),(191,2,17,36,'I\'d want'),(192,3,17,36,'I\'d like'),(193,4,17,36,'I\'m like'),(194,1,17,37,'had'),(195,2,17,37,'is'),(196,3,17,37,'was'),(197,4,17,37,'did'),(198,1,17,38,'as small'),(199,2,17,38,'smallest'),(200,3,17,38,'more small'),(201,4,17,38,'smaller'),(202,1,17,39,'most expensive'),(203,2,17,39,'expensivest'),(204,3,17,39,'more expensive'),(205,4,17,39,'as expensive'),(206,1,17,40,'easy'),(207,2,17,40,'easier'),(208,3,17,40,'good'),(209,4,17,40,'easily'),(210,1,17,41,'did'),(211,2,17,41,'was'),(212,3,17,41,'went'),(213,4,17,41,'have'),(214,1,17,42,'No, she didn\'t'),(215,2,17,42,'No, she didn\'t stay'),(216,3,17,42,'No, she stayed not'),(217,4,17,42,'No, she didn\'t stayed'),(218,1,17,43,'gone'),(219,2,17,43,'was'),(220,3,17,43,'been'),(221,4,17,43,'went'),(222,1,17,44,'I\'ll get'),(223,2,17,44,'I\'m getting'),(224,3,17,44,'I get'),(225,4,17,44,'I\'d get'),(226,1,17,45,'Did'),(227,2,17,45,'Do'),(228,3,17,45,'Were'),(229,4,17,45,'Have'),(230,1,17,46,'to drive'),(231,2,17,46,'driving'),(232,3,17,46,'drive'),(233,4,17,46,'the driving'),(234,1,17,47,'to walk'),(235,2,17,47,'walking'),(236,3,17,47,'walk'),(237,4,17,47,'to walking'),(238,1,17,48,'by day'),(239,2,17,48,'the day'),(240,3,17,48,'in day'),(241,4,17,48,'a day'),(242,1,17,49,'too many'),(243,2,17,49,'too much'),(244,3,17,49,'enough'),(245,4,17,49,'too'),(246,1,17,50,'since'),(247,2,17,50,'to'),(248,3,17,50,'towards'),(249,4,17,50,'until'),(250,1,17,51,'are eating, have'),(251,2,17,51,'eat, have'),(252,3,17,51,'eat, are having'),(253,4,17,51,'are eating, are having'),(254,1,17,52,'because'),(255,2,17,52,'so'),(256,3,17,52,'that'),(257,4,17,52,'until'),(258,1,17,53,'need'),(259,2,17,53,'are needing'),(260,3,17,53,'will need'),(261,4,17,53,'will have needed'),(262,1,17,54,'as fashionable than'),(263,2,17,54,'as fashionable as'),(264,3,17,54,'more fashionable as'),(265,4,17,54,'fashionable'),(266,1,17,55,'you, she'),(267,2,17,55,'you, her'),(268,3,17,55,'yours, she'),(269,4,17,55,'yourself, hers'),(270,1,17,56,'had, rang'),(271,2,17,56,'were having, rang'),(272,3,17,56,'were having, was ringing'),(273,4,17,56,'had, has rung'),(274,1,17,57,'must'),(275,2,17,57,'mustn\'t'),(276,3,17,57,'should'),(277,4,17,57,'don\'t have to'),(278,1,17,58,'won\'t'),(279,2,17,58,'don\'t'),(280,3,17,58,'shouldn\'t'),(281,4,17,58,'couldn\'t'),(282,1,17,59,'will go'),(283,2,17,59,'go'),(284,3,17,59,'would go'),(285,4,17,59,'went'),(286,1,17,60,'but, so'),(287,2,17,60,'so, because'),(288,3,17,60,'unless, but'),(289,4,17,60,'for, as'),(290,1,17,61,'However'),(291,2,17,61,'Although'),(292,3,17,61,'But'),(293,4,17,61,'When'),(294,1,17,62,'As we were waiting'),(295,2,17,62,'When we waited'),(296,3,17,62,'As soon as we waited'),(297,4,17,62,'Until we waited'),(298,1,17,63,'I ever saw'),(299,2,17,63,'I\'ve ever seen'),(300,3,17,63,'I\'ve never seen'),(301,4,17,63,'I\'ve already seen'),(302,1,17,64,'during, the'),(303,2,17,64,'for, during'),(304,3,17,64,'for, last'),(305,4,17,64,'last, during'),(306,1,17,65,'won\'t be'),(307,2,17,65,'will be'),(308,3,17,65,'be'),(309,4,17,65,'is'),(310,1,17,66,'what she like'),(311,2,17,66,'how is she'),(312,3,17,66,'how she is'),(313,4,17,66,'how does she'),(314,1,17,67,'us'),(315,2,17,67,'ourselves'),(316,3,17,67,'ourself'),(317,4,17,67,'our own'),(318,1,17,68,'however'),(319,2,17,68,'despite'),(320,3,17,68,'in case'),(321,4,17,68,'as'),(322,1,17,69,'nearly never'),(323,2,17,69,'hardly never'),(324,3,17,69,'hardly ever'),(325,4,17,69,'ever'),(326,1,17,70,'looks'),(327,2,17,70,'looks like'),(328,3,17,70,'is like'),(329,4,17,70,'like'),(330,1,17,71,'don\'t have to'),(331,2,17,71,'couldn\'t'),(332,3,17,71,'don\'t'),(333,4,17,71,'mustn\'t'),(334,1,17,72,'for'),(335,2,17,72,'during'),(336,3,17,72,'since'),(337,4,17,72,'until'),(338,1,17,73,'needs be doing'),(339,2,17,73,'needs done'),(340,3,17,73,'needs doing'),(341,4,17,73,'needs to do'),(342,1,17,74,'mend'),(343,2,17,74,'to mend'),(344,3,17,74,'for mending'),(345,4,17,74,'mending'),(346,1,17,75,'must'),(347,2,17,75,'haven\'t to'),(348,3,17,75,'aren\'t supposed to'),(349,4,17,75,'don\'t have to'),(350,1,17,76,'had been waiting'),(351,2,17,76,'is waiting'),(352,3,17,76,'has been waiting'),(353,4,17,76,'was waiting'),(354,1,17,77,'can\'t'),(355,2,17,77,'must'),(356,3,17,77,'won\'t'),(357,4,17,77,'probably'),(358,1,17,78,'have to'),(359,2,17,78,'are supposed to'),(360,3,17,78,'should'),(361,4,17,78,'are allowed to'),(362,1,17,79,'In spite of'),(363,2,17,79,'Even though'),(364,3,17,79,'However'),(365,4,17,79,'Because'),(366,1,17,80,'as if'),(367,2,17,80,'if only'),(368,3,17,80,'in case'),(369,4,17,80,'although');
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
INSERT INTO `SURVEYS_QUESTIONS` VALUES (1,1,1,'\"Hello Sara, ______?\" - \"I\'m very well, thank you.\"'),(2,1,2,'\"What\'s ______ name?\" - \"Jane Edwards.\"'),(3,1,3,'\"How old are you?\" - \"______.\"'),(4,1,4,'\"Is this your book?\" - \"______.\"'),(5,1,5,'\"Where is Anna from?\" - \"______ from Rome.\"'),(6,1,6,'\"______ is your address?\" - \"12, Sundown Street, Bristol.\"'),(7,1,7,'______ name is John Smith.'),(8,2,1,'Doctor WHO? ______'),(12,2,2,'Who I am? ______'),(14,17,1,'\"Hello Sara, ______?\" - \"I\'m very well, thank you.\"'),(15,17,2,'\"What\'s ______ name?\" - \"Jane Edwards.\"'),(16,17,3,'\"How old are you?\" - \"______.\"'),(17,17,4,'\"Is this your book?\" - \"______.\"'),(18,17,5,'\"Where is Anna from?\" - \"______ from Rome.\"'),(19,17,6,'\"______ is your address?\" - \"12, Sundown Street, Bristol.\"'),(20,17,7,'______ name is John Smith.'),(21,17,8,'Sam ______ a doctor, he\'s a teacher at the university.'),(22,17,9,'Here are Juan and Mercedes. ______ are from Valencia in Spain.'),(23,17,10,'\"Have you got a computer?\" - \"Yes, ______.\"'),(24,17,11,'______ two hundred students in my school.'),(25,17,12,'\"Do you live in Munich?\" - \"Yes, ______.\"'),(26,17,13,'\"Is that ______ car?\" - \"No, it isn\'t.\"'),(27,17,14,'\"______ is this blue bag?\" - \"It\'s $5.50.\"'),(28,17,15,'\"What\'s her job?\" - \"She\'s ______.\"'),(29,17,16,'\"______ your car?\" - \"It\'s in the car park.\"'),(30,17,17,'\"______ bag is this?\" - \"It\'s mine.\"'),(31,17,18,'______ only three chairs in my room.'),(32,17,19,'She ______ a house in the town centre.'),(33,17,20,'\"______ brothers have you got?\" - \"Only one.\"'),(34,17,21,'\"Is there any food left?\" - \"______.\"'),(35,17,22,'My favourite painters are Monet and Renoir but John doesn\'t like ______ at all.'),(36,17,23,'There aren\'t ______ people here today.'),(37,17,24,'We haven\'t got ______.'),(38,17,25,'\"Do you speak Japanese?\" - \"No, I ______.\"'),(39,17,26,'\"What does he do?\" - \"______.\"'),(40,17,27,'He ______ in an office every morning from eight to twelve.'),(41,17,28,'\"Do you like ______?\" - \"Yes, I do.\"'),(42,17,29,'I go ______ school in Vienna.'),(43,17,30,'We have lunch ______ one o\'clock.'),(44,17,31,'She works ______ Saturday.'),(45,17,32,'I stay at home ______ the morning.'),(46,17,33,'\"How do you get to work?\" - \"______.\"'),(47,17,34,'\"Do you like classical music?\" - \"______.\"'),(48,17,35,'\"Where is Mary?\" - \"She ______ over there.\"'),(49,17,36,'I\'m hungry. ______ something to eat, please'),(50,17,37,'He ______ born in 1963 in Spain.'),(51,17,38,'Switzerland is ______ than Britain.'),(52,17,39,'Motor racing is the ______ sport in the world.'),(53,17,40,'He passed his English exam very ______.'),(54,17,41,'\"When ______ you go to the USA?\" - \"Last year.\"'),(55,17,42,'\"Did she stay with friends?\" - \"______.\"'),(56,17,43,'She\'s never ______ to New York.'),(57,17,44,'\"I haven\'t got any money.\" - \"Never mind. ______ some from the bank.\"'),(58,17,45,'______ you ever visited London?'),(59,17,46,'He\'s learning ______ a lorry.'),(60,17,47,'I can\'t stand ______ in hot weather.'),(61,17,48,'He smokes more than ten cigarettes ______.'),(62,17,49,'Let\'s go somewhere else. There\'s ______ noise in this room.'),(63,17,50,'It\'s a very long day for Jack. He doesn\'t get home from school ______ six o\'clock.'),(64,17,51,'They usually ______ at home but today they ______ lunch in a restaurant.'),(65,17,52,'We didn\'t stay late ______ we were very tired.'),(66,17,53,'I think most people ______ English for their jobs in the future.'),(67,17,54,'Teenagers today like wearing casual clothes so leather shoes aren\'t ______ trainers.'),(68,17,55,'A friend of ______ phoned this morning but ______ didn\'t leave a message.'),(69,17,56,'We ______ lunch when the phone ______.'),(70,17,57,'You ______ open the door before the train gets into the station. It\'s very dangerous.'),(71,17,58,'If you don\'t want to burn yourself, you ______ lie in the sun all day.'),(72,17,59,'If I have enough money next year, I ______ to the USA.'),(73,17,60,'It\'s usually quite warm in September ______ it often rains, ______ bring a waterproof.'),(74,17,61,'______ she likes coffee, she prefers tea.'),(75,17,62,'______ for the bus, a man with a gun ran out of the bank opposite us.'),(76,17,63,'It\'s the best film ______. You should go and see it.'),(77,17,64,'They went to Australia ______ a month ______ summer.'),(78,17,65,'I don\'t think life ______ better in the future.'),(79,17,66,'I haven\'t heard from Jane for ages. I wonder ______.'),(80,17,67,'We\'re not paying a builder to mend the fireplace. We\'ve decided to do it ______.'),(81,17,68,'I always take an umbrella ______ it rains.'),(82,17,69,'We ______ go out to a restaurant during the week because when we get home from work we\'re too tired.'),(83,17,70,'That sofa ______ comfortable. Can I try it?'),(84,17,71,'I ______ be late for work this morning. I\'ve got a lot to do before midday.'),(85,17,72,'They\'ve lived in that house ______ they were children.'),(86,17,73,'A lot ______ to the house before we can move in.'),(87,17,74,'I\'ll get an electrician ______ the heating.'),(88,17,75,'You ______ come with us if you don\'t want to.'),(89,17,76,'When he arrived a crowd ______ for several hours to greet him.'),(90,17,77,'She\'s just bought a brand new car so she ______ be able to drive.'),(91,17,78,'You ______ show your passport at the frontier if you want to get across.'),(92,17,79,'______ she was an hour late, she didn\'t apologise.'),(93,17,80,'They don\'t like him at all. He treats them ______ they were children.');
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
INSERT INTO `SURVEYS_TRUE_ANSWERS` VALUES (1,1,1,2),(2,1,2,2),(3,1,3,4),(4,1,4,1),(5,1,5,4),(6,1,6,3),(7,1,7,1),(8,2,1,3),(9,2,1,3),(10,2,1,3),(12,2,2,1),(14,17,1,2),(15,17,2,2),(16,17,3,4),(17,17,4,1),(18,17,5,4),(19,17,6,3),(20,17,7,1),(21,17,8,2),(22,17,9,1),(23,17,10,4),(24,17,11,3),(25,17,12,4),(26,17,13,2),(27,17,14,3),(28,17,15,4),(29,17,16,4),(30,17,17,1),(31,17,18,2),(32,17,19,3),(33,17,20,4),(34,17,21,1),(35,17,22,2),(36,17,23,1),(37,17,24,2),(38,17,25,4),(39,17,26,2),(40,17,27,2),(41,17,28,4),(42,17,29,2),(43,17,30,1),(44,17,31,4),(45,17,32,3),(46,17,33,1),(47,17,34,4),(48,17,35,2),(49,17,36,3),(50,17,37,3),(51,17,38,4),(52,17,39,1),(53,17,40,4),(54,17,41,1),(55,17,42,1),(56,17,43,3),(57,17,44,1),(58,17,45,4),(59,17,46,1),(60,17,47,2),(61,17,48,4),(62,17,49,2),(63,17,50,4),(64,17,51,3),(65,17,52,1),(66,17,53,3),(67,17,54,2),(68,17,55,3),(69,17,56,2),(70,17,57,2),(71,17,58,3),(72,17,59,1),(73,17,60,1),(74,17,61,2),(75,17,62,1),(76,17,63,2),(77,17,64,3),(78,17,65,2),(79,17,66,3),(80,17,67,2),(81,17,68,3),(82,17,69,3),(83,17,70,1),(84,17,71,4),(85,17,72,3),(86,17,73,3),(87,17,74,2),(88,17,75,4),(89,17,76,1),(90,17,77,2),(91,17,78,1),(92,17,79,2),(93,17,80,1);
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
  `ID_USER` bigint NOT NULL,
  `ID_SURVEY` int NOT NULL,
  `STATUS_SURVEY` int NOT NULL,
  `NUMBER_QUESTION` int DEFAULT '0',
  `QUESTION_ID` int DEFAULT NULL,
  `PREVIOUS_QUESTION_ID` int DEFAULT NULL,
  `BALLS` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID_USER_SURVEY`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `MESSAGE_START_ID` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`USER_ID`),
  UNIQUE KEY `USER_TG_ID_UNIQUE` (`USER_TG_ID`),
  UNIQUE KEY `USER_LOGIN_UNIQUE` (`USER_LOGIN`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-01 19:26:33
