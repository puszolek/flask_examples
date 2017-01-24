# -*- coding: utf-8 -*-

import pymysql as mariadb
import requests
import string
import json
import sys


#connect to db
def connect_db(host, user, password, db):
    con = mariadb.connect(host=host, user=user, password=password, db=db, charset='utf8')

    cursor = con.cursor()
    cursor.execute("set names utf8;")
    cursor.execute("set autocommit=1")
    return cursor, con

#get data
def get_data_db(cursor, table, column):
    sql = ("""SELECT %s FROM %s""" %(column, table))
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()


def main():

    host = ''
    user = ''
    password = ''
    db = ''

    cursor, con = connect_db(host, user, password, db)

    cursor.execute(""" """)

    con.close()
