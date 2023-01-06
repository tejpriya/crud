from django.shortcuts import render
from django.shortcuts import render, redirect  
from crud.forms import EmployeeForm  
from crud.models import Employee  
import traceback
import sqlite3
import sqliteconnection
import os
def sqliteconnection():
    try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
                                id INTEGER PRIMARY KEY,
                                cid INTEGER,
                                cname TEXT NOT NULL,
                                cemail text NOT NULL UNIQUE,
                                ccontact INTEGER,);'''
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()
except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
def show():
    try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO customer
                        VALUES  (1, 123,'DemoText','ss2@gmail.com',35467,)"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table")
    print("Exception class is: ", error.__class__)
    print("Exception is", error.args)
    print('Printing detailed SQLite exception traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")



