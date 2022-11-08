CREATE DATABASE flower;


CREATE TABLE `flower` (
  `flower_id` varchar(200) NOT NULL,
  `flower_name` varchar(200) NOT NULL,
  `quantity` varchar(200) NOT NULL,
  `price` varchar(200) NOT NULL,
  `Timestamp` varchar(200) NOT NULL,
   PRIMARY KEY (`flower_id`)
);

INSERT INTO `flower` (`flower_id`, `flower_name`, `quantity`, `price`, `Timestamp`)
VALUES('1', 'lotus', 30,25,'2022-2-16'),
('6','orchids' ,45,25,'2021-3-27');
