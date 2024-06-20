-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2020 at 09:41 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `Student`
--
DROP TABLE IF EXISTS `courseMaterials`;
DROP TABLE IF EXISTS `LoginRecord`;
DROP TABLE IF EXISTS `taking`;
DROP TABLE IF EXISTS `CourseSchedule`;
DROP TABLE IF EXISTS `Teaches`;
DROP TABLE IF EXISTS `Students`;
DROP TABLE IF EXISTS `Teachers`;
DROP TABLE IF EXISTS `Courses`;

CREATE TABLE `Students` (
  `student_id` INT PRIMARY KEY,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` VALUES (1, "Pat", 'winsonsu@connect.hku.hk');

/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE `Teachers` (
  `teacher_id` INT PRIMARY KEY,
  `name` VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Teachers` WRITE;
/*!40000 ALTER TABLE `Teachers` DISABLE KEYS */;
INSERT INTO `Teachers` VALUES (1, "Dr. Ping Luo");
INSERT INTO `Teachers` VALUES (2, "Zhixuan Liang");
INSERT INTO `Teachers` VALUES (3, "Dr. Chenshu WU");
INSERT INTO `Teachers` VALUES (4, "Dr. Ravi Ramanathan");
/*!40000 ALTER TABLE `Teachers` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE `Courses` (
  `course_id` VARCHAR(255) PRIMARY KEY,
  `course_name` VARCHAR(255) NOT NULL,
  `classroom_address` VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Courses` WRITE;
/*!40000 ALTER TABLE `Courses` DISABLE KEYS */;
INSERT INTO `Courses` VALUES ("COMP3278", "Introduction to database management systems","MWT1 and Zoom");
INSERT INTO `Courses` VALUES ("COMP3230", "Principles of operating systems","CYCP1");
INSERT INTO `Courses` VALUES ("COMP3357", "Cryptography","CB 327");
/*!40000 ALTER TABLE `Courses` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE `Teaches` (
  `teacher_id` INT,
  `course_id` VARCHAR(255),
  FOREIGN KEY (`teacher_id`) REFERENCES `Teachers`(`teacher_id`),
  FOREIGN KEY (`course_id`) REFERENCES `Courses`(`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Teaches` WRITE;
/*!40000 ALTER TABLE `Teaches` DISABLE KEYS */;
INSERT INTO `Teaches` VALUES (1, "COMP3278");
INSERT INTO `Teaches` VALUES (2, "COMP3278");
INSERT INTO `Teaches` VALUES (3, "COMP3230");
INSERT INTO `Teaches` VALUES (4, "COMP3357");
/*!40000 ALTER TABLE `Teaches` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE `CourseSchedule` (
  `timetable_id` INT PRIMARY KEY,
  `course_id` VARCHAR(255),
  `start_time` DATETIME NOT NULL,
  `end_time` DATETIME NOT NULL,
  FOREIGN KEY (`course_id`) REFERENCES `Courses`(`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `CourseSchedule` WRITE;
/*!40000 ALTER TABLE `CourseSchedule` DISABLE KEYS */;
INSERT INTO `CourseSchedule` VALUES (1, "COMP3278", "2023-11-23 07:30:00", '2023-11-23 08:20:00');
INSERT INTO `CourseSchedule` VALUES (2, "COMP3278", "2023-11-23 10:30:00", '2023-11-23 12:20:00');
INSERT INTO `CourseSchedule` VALUES (3, "COMP3230", "2023-11-13 14:00:00", '2023-11-23 16:20:00');
INSERT INTO `CourseSchedule` VALUES (4, "COMP3230", "2023-11-24 13:00:00", '2023-11-23 14:20:00');
INSERT INTO `CourseSchedule` VALUES (5, "COMP3357", "2023-11-16 13:30:00", '2023-11-23 15:20:00');
INSERT INTO `CourseSchedule` VALUES (6, "COMP3357", "2023-11-22 11:00:00", '2023-11-23 12:50:00');
/*!40000 ALTER TABLE `CourseSchedule` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE `taking` (
  `course_id` VARCHAR(255),
  `student_id` INT,
  FOREIGN KEY (`course_id`) REFERENCES `Courses`(`course_id`),
  FOREIGN KEY (`student_id`) REFERENCES `Students`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


LOCK TABLES `taking` WRITE;
/*!40000 ALTER TABLE `taking` DISABLE KEYS */;
INSERT INTO `taking` VALUES ("COMP3278", 1);
INSERT INTO `taking` VALUES ("COMP3357", 1);
/*!40000 ALTER TABLE `taking` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE `courseMaterials` (
  `material_id` INT PRIMARY KEY,
  `course_id` VARCHAR(255),
  `material_type` VARCHAR(255) NOT NULL,
  `material_link` VARCHAR(255) NOT NULL,
  FOREIGN KEY (`course_id`) REFERENCES `Courses`(`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `courseMaterials` WRITE;
/*!40000 ALTER TABLE `courseMaterials` DISABLE KEYS */;
INSERT INTO `courseMaterials` VALUES (1, "COMP3278", "pdf", 'https://connecthkuhk-my.sharepoint.com/:f:/g/personal/winsonsu_connect_hku_hk/Er5x7in_4KVHvUn1hAnD0PEBEP8TtfmeWo3psnbU7P8ZQw?e=yLgdk0');
INSERT INTO `courseMaterials` VALUES (2, "COMP3278", "zoom", 'https://hku.zoom.us/j/98307568693?pwd=QmlqZERWeDdWRVZ3SGdqWG51YUtndz09');
INSERT INTO `courseMaterials` VALUES (3, "COMP3278", "msg", 'Good luck');

/*!40000 ALTER TABLE `courseMaterials` ENABLE KEYS */;
UNLOCK TABLES;


CREATE TABLE `LoginRecord`(
  `login_id` INT PRIMARY KEY AUTO_INCREMENT,
  `student_id` INT,
  `login_time` DATETIME NOT NULL,
  `logout_time` DATETIME,
  FOREIGN KEY (`student_id`) REFERENCES `Students`(`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


LOCK TABLES `LoginRecord` WRITE;
/*!40000 ALTER TABLE `LoginRecord` DISABLE KEYS */;
INSERT INTO `LoginRecord` VALUES (1, 1, "2023-10-28 14:56:59", '2023-10-28 15:56:59');
INSERT INTO `LoginRecord` VALUES (2, 1, "2023-10-29 10:27:36", '2023-10-29 12:19:13');
INSERT INTO `LoginRecord` VALUES (3, 1, "2023-11-01 17:07:15", '2023-11-01 19:01:01');
INSERT INTO `LoginRecord` VALUES (4, 1, "2023-11-10 12:33:21", '2023-11-10 12:34:20');
/*!40000 ALTER TABLE `LoginRecord` ENABLE KEYS */;
UNLOCK TABLES;




/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
