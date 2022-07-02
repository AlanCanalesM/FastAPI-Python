from peewee import *

database = MySQLDatabase(database='fastapi', 
                         user='root',
                         password='',
                         host='localhost',
                         port=3306)
