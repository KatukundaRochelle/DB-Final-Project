CREATE TABLE `patients` (
  `patient_id` int PRIMARY KEY,
  `patient_name` text,
  `gender` text,
  `age` int,
  `p_department` text
);

CREATE TABLE `doctors` (
  `doctor_id` int PRIMARY KEY,
  `doctor_name` text,
  `field` text
);

CREATE TABLE `treatment` (
  `patient_id` int,
  `doctor_id` int,
  `admission_id` text
);

CREATE TABLE `admission` (
  `admission_id` int PRIMARY KEY,
  `p_department` text,
  `fee` int
);

ALTER TABLE `treatment` ADD FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`);

ALTER TABLE `treatment` ADD FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`);

ALTER TABLE `treatment` ADD FOREIGN KEY (`admission_id`) REFERENCES `admission` (`admission_id`);
