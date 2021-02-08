-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: traveller_io
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `flight_bookings`
--

DROP TABLE IF EXISTS `flight_bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight_bookings` (
  `PNR` varchar(30) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Dept` varchar(20) DEFAULT NULL,
  `Arr` varchar(20) DEFAULT NULL,
  `dept_date` varchar(10) DEFAULT NULL,
  `dept_time` time DEFAULT NULL,
  `arr_time` time DEFAULT NULL,
  `Age` decimal(3,0) DEFAULT NULL,
  `Gender` varchar(6) DEFAULT NULL,
  `mob` decimal(10,0) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `Flight_no` varchar(7) DEFAULT NULL,
  `Airline` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`PNR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_bookings`
--

LOCK TABLES `flight_bookings` WRITE;
/*!40000 ALTER TABLE `flight_bookings` DISABLE KEYS */;
INSERT INTO `flight_bookings` VALUES ('RGGT3462562','Amal Thomas','Amritsar(ATO)','Bangalore(BLR)','14-02-2020','08:35:00','11:05:00',14,'Male',1234567890,'thomasamal479@gmail.com','SX245','Spice Jet'),('RGRE2744674','Amal','Bangalore(BLR)','Amritsar(ATO)','14-02-2027','13:54:00','16:44:00',0,'Male',0,'wewegfhe','6E0506','Indigo'),('SSF4237070','Amal Thomas','Bangalore(BLR)','Chennai(MAA)','10-02-2021','20:00:00','20:50:00',17,'Male',9910223472,'thomasamal479@gmail.com','SX5769','Spice Jet');
/*!40000 ALTER TABLE `flight_bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight_schedule`
--

DROP TABLE IF EXISTS `flight_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight_schedule` (
  `Flight_no` varchar(20) NOT NULL,
  `Airline` varchar(20) DEFAULT NULL,
  `city_dep` varchar(20) DEFAULT NULL,
  `city_arr` varchar(20) DEFAULT NULL,
  `date_dep` date DEFAULT NULL,
  `time_dep` time DEFAULT NULL,
  `date_arr` date DEFAULT NULL,
  `time_arr` time DEFAULT NULL,
  PRIMARY KEY (`Flight_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_schedule`
--

LOCK TABLES `flight_schedule` WRITE;
/*!40000 ALTER TABLE `flight_schedule` DISABLE KEYS */;
INSERT INTO `flight_schedule` VALUES ('6E0506','Indigo','Bangalore(BLR)','Amritsar(ATO)',NULL,'13:54:00',NULL,'16:44:00'),('6E223','Indigo','Amritsar(ATO)','Bangalore(BLR)',NULL,'18:30:30',NULL,'20:30:00'),('6E4852','Indigo','Bangalore(BLR)','New Delhi(DEL)',NULL,'06:45:00',NULL,'09:10:00'),('6E5353','Indigo','Bangalore(BLR)','Chennai(MAA)',NULL,'09:04:00',NULL,'09:54:00'),('6E5456','Indigo','Bangalore(BLR)','Hyderabad(HYD)',NULL,'22:45:00',NULL,'23:35:00'),('6E584','Indigo','Amritsar(ATO)','Hyderabad(HYD)',NULL,'14:28:00',NULL,'16:56:00'),('6E5858','Indigo','Bangalore(BLR)','Vasco Da Gama(GOI)',NULL,'21:00:00',NULL,'22:00:00'),('6E8394','Indigo','Bangalore(BLR)','Kolkata(CCU)',NULL,'14:25:00',NULL,'16:45:00'),('6E8490','Indigo','Amritsar(ATO)','Kolkata(CCU)',NULL,'08:58:00',NULL,'11:29:00'),('6E884','Indigo','Amritsar(ATO)','Calicut(CCJ)',NULL,'16:35:00',NULL,'20:01:00'),('AE0445','Air India','Amritsar(ATO)','New Delhi(DEL)',NULL,'17:04:00',NULL,'17:54:00'),('AE325','Air India','Amritsar(ATO)','Calicut(CCJ)',NULL,'11:25:00',NULL,'14:51:00'),('AE3423','Air India','Bangalore(BLR)','Kolkata(CCU)',NULL,'10:34:00',NULL,'12:54:00'),('AE4595','Air India','Bangalore(BLR)','Hyderabad(HYD)',NULL,'16:34:00',NULL,'17:24:00'),('AE4646','Air India','Bangalore(BLR)','Mumbai(BOM)',NULL,'23:04:00',NULL,'00:29:00'),('AE5355','Air India','Bangalore(BLR)','Amritsar(ATO)',NULL,'09:03:00',NULL,'11:53:00'),('AE583','Air India','Amritsar(ATO)','Hyderabad(HYD)',NULL,'10:25:00',NULL,'12:58:00'),('AE6598','Air India','Bangalore(BLR)','Calicut(CCJ)',NULL,'17:35:00',NULL,'18:02:00'),('AE7336','Air India','Amritsar(ATO)','Cochin(COK)',NULL,'19:02:00',NULL,'22:38:00'),('AE774','Air India','Bangalore(BLR)','Vasco Da Gama(GOI)',NULL,'15:55:00',NULL,'16:55:00'),('AE8479','Air India','Amritsar(ATO)','Mumbai(BOM)',NULL,'14:00:00',NULL,'16:07:00'),('GE0405','Go Air','Bangalore(BLR)','Kolkata(CCU)',NULL,'22:04:00',NULL,'00:24:00'),('GE0492','Go Air','Amritsar(ATO)','Vasco Da Gama(GOI)',NULL,'08:45:00',NULL,'11:28:00'),('GE0595','Go Air','Bangalore(BLR)','Amritsar(ATO)',NULL,'18:45:00',NULL,'21:35:00'),('GE335','Go Air','Amritsar(ATO)','Bangalore(BLR)',NULL,'14:45:00',NULL,'17:15:00'),('GE543','Go Air','Amritsar(ATO)','Hyderabad(HYD)',NULL,'18:52:00',NULL,'21:20:00'),('GE546','Go Air','Amritsar(ATO)','Mumbai(BOM)',NULL,'18:45:00',NULL,'20:52:00'),('GE564','Go Air','Amritsar(ATO)','Chennai(MAA)',NULL,'10:45:00',NULL,'13:58:00'),('GE7449','Go Air','Bangalore(BLR)','Cochin(COK)',NULL,'10:34:00',NULL,'11:34:00'),('GE8459','Go Air','Bangalore(BLR)','Chennai(MAA)',NULL,'14:04:00',NULL,'14:54:00'),('GE9485','Go Air','Amritsar(ATO)','Kolkata(CCU)',NULL,'14:54:00',NULL,'17:25:00'),('GX558','Go Air','Calicut(CCJ)','Chennai(MAA)',NULL,'05:34:00',NULL,'06:19:00'),('GX5875','Go Air','Bangalore(BLR)','New Delhi(DEL)',NULL,'11:30:00',NULL,'13:55:00'),('SX245','Spice Jet','Amritsar(ATO)','Bangalore(BLR)',NULL,'08:35:00',NULL,'11:05:00'),('SX3355','Spice Jet','Bangalore(BLR)','Mumbai(BOM)',NULL,'07:56:00',NULL,'09:21:00'),('SX468','Spice Jet','Amritsar(ATO)','Cochin(COK)',NULL,'09:20:00',NULL,'12:56:00'),('SX4957','Vistara','Bangalore(BLR)','Calicut(CCJ)',NULL,'07:35:00',NULL,'08:02:00'),('SX5585','Spice Jet','Amritsar(ATO)','Vasco Da Gama(GOI)',NULL,'11:34:00',NULL,'14:17:00'),('SX565','Spice Jet','Amritsar(ATO)','Chennai(MAA)',NULL,'14:23:00',NULL,'17:36:00'),('SX5769','Spice Jet','Bangalore(BLR)','Chennai(MAA)',NULL,'20:00:00',NULL,'20:50:00'),('SX588','Spice Jet','Calicut(CCJ)','Chennai(MAA)',NULL,'11:45:00',NULL,'12:30:00'),('SX7894','Spice Jet','Amritsar(ATO)','Kolkata(CCU)',NULL,'20:00:00',NULL,'22:31:00'),('SX828','Spice Jet','Bangalore(BLR)','New Delhi(DEL)',NULL,'18:55:00',NULL,'21:20:00'),('SX9495','Spice Jet','Bangalore(BLR)','Cochin(COK)',NULL,'14:54:00',NULL,'15:54:00'),('SX9586','Spice Jet','Amritsar(ATO)','New Delhi(DEL)',NULL,'06:03:00',NULL,'06:53:00'),('UK495','Vistara','Amritsar(ATO)','Mumbai(BOM)',NULL,'11:04:00',NULL,'13:11:00'),('UK5564','Vistara','Bangalore(BLR)','Cochin(COK)',NULL,'20:34:00',NULL,'21:34:00'),('UK5584','Vistara','Bangalore(BLR)','Mumbai(BOM)',NULL,'14:34:00',NULL,'15:59:00'),('UK564','Vistara','Amritsar(ATO)','Calicut(CCJ)',NULL,'05:45:00',NULL,'09:09:00'),('UK5858','Vistara','Bangalore(BLR)','Calicut(CCJ)',NULL,'11:42:00',NULL,'12:09:00'),('UK588','Vistara','Calicut(CCJ)','Chennai(MAA)',NULL,'19:25:00',NULL,'20:10:00'),('UK6754','Vistara','Amritsar(ATO)','New Delhi(DEL)',NULL,'10:04:00',NULL,'10:54:00'),('UK855','Vistara','Bangalore(BLR)','Vasco Da Gama(GOI)',NULL,'10:40:00',NULL,'11:40:00'),('UK857','Vistara','Amritsar(ATO)','Chennai(MAA)',NULL,'18:45:00',NULL,'22:03:00'),('UK947','Vistara','Amritsar(ATO)','Cochin(COK)',NULL,'15:00:00',NULL,'18:36:00'),('UK9475','Vistara','Bangalore(BLR)','Hyderabad(HYD)',NULL,'11:45:00',NULL,'12:35:00'),('UK9585','Vistara','Amritsar(ATO)','Vasco Da Gama(GOI)',NULL,'17:00:00',NULL,'19:43:00');
/*!40000 ALTER TABLE `flight_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `name` varchar(320) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-08 17:38:10
