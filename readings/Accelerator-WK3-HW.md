# Introduction to Databases

- [Introduction to Databases](#introduction-to-databases)
  - [What is a Database?](#what-is-a-database)
    - [CRUD Operations](#crud-operations)
    - [Relational Databases (SQL)](#relational-databases-sql)
    - [Non-Relational Databases (NoSQL)](#non-relational-databases-nosql)
  - [What is MongoDB?](#what-is-mongodb)
      - [Why is this great for us?](#why-is-this-great-for-us)


## What is a Database?

A **database** is a logically coherent collection of related data whose purpose is to perform specific [**CRUD**](#crud-operations) operations. The database is usually controlled by a **Database Management System** (DBMS). Together, the data and the DBMS are referred to as a **database system**, often shortened to just database.

> For more information on DBMS, see [this link](https://www.appdynamics.com/topics/database-management-systems#~1-what-is-dbms).

---

### CRUD Operations
- **C**reate - Insert data into a database
- **R**ead - Query data from a database
- **U**pdate - Update data in a database
- **D**elete - Delete data from a database

Some other operations databases can do include:

- Performing scheduled backups of the database.
- Maintain redundant copies of the database.
- Control and monitor user access and privileges.
- Create visual reports that incorporate graphs.
- Create data entry forms.

---


There are *two* types of databases:

### Relational Databases (SQL)

The **relational database** model organizes data into multiple related tables. Data values are only stored a *single time* and then referenced from a different table, saving space on the database and preventing integrity errors.

> For more information on relational databases, see [this link](https://www.oracle.com/database/what-is-a-relational-database/). 

### Non-Relational Databases (NoSQL)

The **non-relational database** model organizes data into tables, but unlike the relational model, the non-relational model does not require a fixed schema, and data is not necessarily normalized. This allows for more flexibility and scalability.

> We will expand more on non-relational databases in the next lesson.

---

*Note: The term NoSQL does not referring to being unable to use SQL commands on the database, but just stands for non-relational*.

---

## What is MongoDB?

First of all, what type of database is MongoDB?

Here's a few hints:
- MongoDB is a document database.
- MongoDB stores data in **flexible**, JSON-like documents.
- MongoDB does not have any predefined [schemas](https://www.ibm.com/topics/database-schema).

If you thought it was a non-relational database, you're correct!

---

MongoDB is a **non-relational database** that stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time.

#### Why is this great for us?

As you can recall, Javascript uses **JSON** (Javascript Object Notation) to store data. This means that we are able to map our MongoDB documents to Javascript objects, making it easier to work with our data.

---

That is all for your brief introduction to databases, see you in class next week!
