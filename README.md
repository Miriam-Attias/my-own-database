# my-own-database

This system is fully operational self-made database, build in two intensive days according to generic API suitable for differing relational and non-relational functionalities and pre-written test cases.

## Description

A relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables. In a relational database, each row in the table is a record with a unique ID called the key. The columns of the table hold attributes of the data, and each record usually has a value for each attribute, making it easy to establish the relationships among data points.

This system is like real relational database. organized collection of data supported : CRUD operation, queries, join and index
by effective access to disk, optimization by key-index, and implement actions by abstract way.

## Getting Started

Installing

"pip install dataclasses" (downloand dataclasses library)

Executing program

import our code to your project by the folloing lines:
from db import DataBase
from db_api import DBField, SelectionCriteria, DB_ROOT, DBTable

Test

If you change the code We recommend that you run the attached tests to make sure you have not violated the existing code

Executing test

-pip install pytest
-run "create_db_backup.py"
for run spesific test command "py.test -k {test_name}"
for run all tests command: "py.test"
