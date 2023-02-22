import sqlite3
from sqlite3 import Error
import os
import json
from datetime import datetime


# returns json of an array of the company names
def get_companies():
    return_dictionary = {"info": []}
    return_array = []
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        c.execute(
            "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
        )
        rows = c.fetchall()
        for row in rows:
            return_array.append(row)
        connection.close()
    return_dictionary["info"] = return_array
    return json.dumps(return_dictionary, indent=4)


# return json of an array of info between the dates from the companyName
def get_history(start_date: datetime, end_date: datetime, company_name: str):
    return_dictionary = {"info": []}
    return_array = []
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        c.execute(
            # "SELECT * FROM " + company_name + " WHERE date > " + convert_date(start_date)
            # + " AND date < " + convert_date(end_date)
            f"SELECT * FROM {company_name} WHERE date >= {convert_date(start_date)} AND date <= {convert_date(end_date)}"
        )
        rows = c.fetchall()
        for row in rows:
            return_array.append(row)
        connection.close()
    return_dictionary["info"] = return_array
    return json.dumps(return_dictionary, indent=4)


def get_prediction(company_name):
    return_dictionary = {"info": []}
    return_array = []
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite.db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        c.execute(
            "Select * FROM <COMPANY> WHERE <NAME> = '" + company_name + "'"
        )
        rows = c.fetchall()
        for row in rows:
            return_array.append(row)
        connection.close()
    return_dictionary["info"] = return_array
    return json.dumps(return_dictionary, indent = 4)


def convert_date(date: datetime):
    """
    Converts a datetime object to unix epoch time, for use in our database
    """
    # if not isinstance(date, datetime):
    #     date = datetime.strptime(date, '%Y.%m.%d')
    return int(date.timestamp())
