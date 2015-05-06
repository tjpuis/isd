﻿DELETE FROM course_grade;
DELETE FROM student;
DELETE FROM course;

INSERT INTO student (sn, no, name)  VALUES (101, 'S001',  '张三');
INSERT INTO student (sn, no, name)  VALUES 
    (102, 'S002',  '李四'), 
    (103, 'S003',  '王五'),
    (104, 'S004',  '马六');

INSERT INTO course (sn, no, name)  VALUES 
    (101, 'C01',  '高数'), 
    (102, 'C02',  '外语');

INSERT INTO course_grade (stu_sn, cou_sn, grade)  VALUES 
    (101, 101,  91), 
    (102, 101,  89),
    (103, 101,  90),
    (101, 102,  89);


    