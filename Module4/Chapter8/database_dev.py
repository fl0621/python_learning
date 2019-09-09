#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import pymysql


def mysql_db():
    db_conf = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'abc@123',
        'db': 'test1'
    }
    conn1 = pymysql.connect(**db_conf, charset='utf8')
    return conn1


def read_data():
    # with "pymysql.cursors.DictCursor" the result set will be dict format otherwise it's a tuple
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from employee where age >= %s and dep_id!=%s'
    rows = cursor.execute(sql, (age, dep_id))  # 'rows' is the quantity of affected rows
    print(rows)
    res = cursor.fetchone()
    print(res)
    # cursor.scroll(3, mode='absolute')
    cursor.scroll(2, mode='relative')
    res = cursor.fetchone()
    print(res)
    cursor.close()


def modify():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'insert into employee(name,sex,age,dep_id) values ("fengfeng","male",%s,%s)'
    rows = cursor.execute(sql, (age, dep_id))
    print(rows)
    print(cursor.lastrowid)
    cursor.close()
    conn.commit()  # must do commit action otherwise modifies can't be write to database.


if __name__ == '__main__':
    conn = mysql_db()
    age = input('input age:').strip()
    dep_id = input('input dep_id:').strip()
    read_data()
    # modify()
    conn.close()
