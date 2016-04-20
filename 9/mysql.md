## Mysql

### Installation

    apt-get install mysql-server

## Creating and showing databases

    mysql -u root -p1q2w3e -e 'CREATE DATABASE mydb;'


    mysql -u root -p1q2w3e -e 'SHOW DATABASES;'

    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mydb               |
    | mysql              |
    | performance_schema |
    +--------------------+


## Creating table


    mysql -u root -p1q2w3e -e 'CREATE TABLE user (name VARCHAR(20), sex CHAR(1), birth DATE, death DATE) mydb'

    ERROR 1046 (3D000) at line 1: No database selected
    
    Warning: Using a password on the command line interface can be insecure.


## Showing tables

    

    mysql -u root -p1q2w3e -e  'SHOW TABLES;' mydb

    +----------------+
    | Tables_in_mydb |
    +----------------+
    | user           |
    +----------------+

## Describing tables 

    mysql -u root -p1q2w3e -e  'describe user;' mydb
    

    +-------+-------------+------+-----+---------+-------+
    | Field | Type        | Null | Key | Default | Extra |
    +-------+-------------+------+-----+---------+-------+
    | name  | varchar(20) | YES  |     | NULL    |       |
    | sex   | char(1)     | YES  |     | NULL    |       |
    | birth | date        | YES  |     | NULL    |       |
    | death | date        | YES  |     | NULL    |       |
    +-------+-------------+------+-----+---------+-------+

## Alter table

    mysql -u root -p1q2w3e -e  'alter table user add column religion varchar (250)' mydb

    mysql -u root -p1q2w3e -e  'describe user;' 

    +----------+--------------+------+-----+---------+-------+
    | Field    | Type         | Null | Key | Default | Extra |
    +----------+--------------+------+-----+---------+-------+
    | name     | varchar(20)  | YES  |     | NULL    |       |
    | sex      | char(1)      | YES  |     | NULL    |       |
    | birth    | date         | YES  |     | NULL    |       |
    | death    | date         | YES  |     | NULL    |       |
    | religion | varchar(250) | YES  |     | NULL    |       |
    +----------+--------------+------+-----+---------+-------+

## Insert record

    mysql -u root -p1q2w3e -e 'INSERT INTO user (name,sex,birth,religion) VALUES ("sergey","m","1977-05-23","agnostic")' mydb;


## Select records 

    mysql -u root -p1q2w3e -e 'SELECT * FROM user' mydb;


    +--------+------+------------+-------+----------+
    | name   | sex  | birth      | death | religion |
    +--------+------+------------+-------+----------+
    | dmitry | m    | 1977-05-23 | NULL  | agnostic |
    | sergey | m    | 1977-05-23 | NULL  | agnostic |
    +--------+------+------------+-------+----------+


    
    

