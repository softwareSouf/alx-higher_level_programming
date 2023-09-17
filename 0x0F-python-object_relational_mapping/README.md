# Database and Python Integration Project

Welcome to the Database and Python Integration Project! This project will guide you through connecting Python to a MySQL database, performing SQL operations, and exploring Object-Relational Mapping (ORM) with SQLAlchemy. Below, you will find important information to get started with this project.

## General Information

### Why Python Programming is Awesome

Python is a versatile and powerful programming language known for its simplicity and readability. It is widely used in various domains, including web development, data analysis, machine learning, and more. Learning Python allows you to leverage its extensive libraries and frameworks to solve a wide range of real-world problems efficiently.

### Connecting to a MySQL Database

You will learn how to connect to a MySQL database from a Python script using the MySQLdb module. This will enable you to establish a connection to your database and execute SQL queries.

### SELECT and INSERT Operations

You will gain proficiency in performing SELECT and INSERT operations on MySQL tables from within your Python scripts. This knowledge will empower you to retrieve and manipulate data stored in the database.

### Understanding Object Relational Mappers (ORMs)

ORMs, such as SQLAlchemy, are essential tools for simplifying database interactions in Python. They abstract the underlying database structure, allowing you to work with Python objects rather than writing SQL queries. This project will introduce you to the concept of ORM and its benefits.

### Python Virtual Environment

You will create a Python Virtual Environment (venv) to manage project-specific dependencies. This isolates your project's environment, ensuring that it remains consistent and avoids conflicts with other Python projects.

## Project Requirements

Here are some important requirements for this project:

- **Editors**: You are free to use vi, vim, or emacs as your code editor.
- **Python Version**: All code will be interpreted using Python 3.8.5.
- **MySQLdb Version**: Your code should work with MySQLdb version 2.0.x.
- **SQLAlchemy Version**: Your code should work with SQLAlchemy version 1.4.x.
- **File Format**: All code files should end with a new line.
- **Shebang Line**: The first line of all your code files should begin with `#!/usr/bin/python3`.
- **README.md**: You must create a README.md file at the root of your project folder to document your project.
- **Code Style**: Ensure your code follows the PEP 8 style guide using pycodestyle.
- **Executable Files**: All your code files must be executable.
- **Documentation**: Provide comprehensive documentation for your modules, classes, and functions.
- **No SQL Execute**: Do not use `execute` with SQLAlchemy.

## Getting Started

Here are some initial steps to set up your project:

### Create a Python Virtual Environment

To create a Python Virtual Environment, use the following commands:

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

### Install MySQLdb Module (version 2.0.x)

Install the MySQLdb module with the following commands:

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```

### Install SQLAlchemy Module (version 1.4.x)

Install the SQLAlchemy module using pip:

```bash
$ sudo pip3 install SQLAlchemy
```

## Conclusion

This project will equip you with the skills to seamlessly integrate Python with MySQL databases, whether using the MySQLdb module or the SQLAlchemy ORM. By the end, you'll understand the power of abstraction provided by ORMs and how to create a clean, isolated project environment using Python Virtual Environments.

