#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import pymysql


def mysql_db():
    server = '127.0.0.1'
    port = 3306
    user = 'root'
    password = 'abc@123'
    db = 'test1'

    conn1 = pymysql.connect(host=server, port=port, user=user, password=password, database=db, charset='utf8')

    # cursor = conn.cursor()

    return conn1


def read_data():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from employee where age >= %s and dep_id!=%s'
    rows = cursor.execute(sql, (age, dep_id))

    print(rows)
    res = cursor.fetchone()
    print(res)
    print(type(res))

    # cursor.scroll(3, mode='absolute')
    cursor.scroll(2, mode='relative')

    res = cursor.fetchone()
    print(res)
    print(type(res))
    cursor.close()


def modify():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'insert into employee(name,sex,age,dep_id) values ("fengfeng","male",%s,%s)'

    rows = cursor.execute(sql, (age, dep_id))
    print(rows)

    print(cursor.lastrowid)

    cursor.close()


if __name__ == '__main__':
    conn = mysql_db()

    age = input('input age:').strip()
    dep_id = input('input dep_id:').strip()
    read_data()

    conn.commit()
    conn.close()
