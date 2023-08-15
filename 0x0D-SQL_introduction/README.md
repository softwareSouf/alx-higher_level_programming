# Project Title

Brief description of the project.

## Learning Objectives

At the end of this project, you will be able to explain:

- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create a database in MySQL
- The meanings of DDL and DML
- How to CREATE or ALTER a table
- How to SELECT, INSERT, UPDATE, or DELETE data
- What subqueries are and how to use them
- How to use MySQL functions

## Getting Started

### Prerequisites

- Ubuntu 20.04 LTS
- MySQL 8.0 (version 8.0.25)

### Installation

Follow these steps to install MySQL 8.0 on Ubuntu 20.04:

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
```

### Usage

1. Connect to MySQL server:

```bash
$ sudo mysql
```

2. Create a database:

```sql
-- Create a new database
CREATE DATABASE my_database;
```

3. Start MySQL in a container:

```bash
$ service mysql start
```

4. Run SQL scripts:

```bash
$ cat my_script.sql | mysql -uroot -p
```

## Visual Content

Here are some visual aids to help you understand the concepts:

### Database Structure

![Database Structure](link_to_image)

### SQL Statements

![SQL Statements](link_to_image)

### Container Usage

![Container Usage](link_to_image)

## Resources

- [What is Database & SQL?](link_to_resource)
- [Basic MySQL Tutorial](link_to_resource)
- [MySQL Cheat Sheet](link_to_resource)

## Author
softwareSouf
```

