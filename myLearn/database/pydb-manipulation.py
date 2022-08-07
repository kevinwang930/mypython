# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:38:25 2020

@author: kevin
"""
from __future__ import print_function
from datetime import date, datetime, timedelta
from db import mydb,mycursor
db_name = 'pydb'
mycursor.execute("use {}".format(db_name))

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")
add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

mycursor.execute(add_employee,data_employee)
emp_no = mycursor.lastrowid

# Insert salary information
data_salary = {
  'emp_no': emp_no,
  'salary': 50000,
  'from_date': tomorrow,
  'to_date': date(9999, 1, 1),
}

mycursor.execute(add_salary,data_salary)

mydb.commit()
mycursor.close()
mydb.close()