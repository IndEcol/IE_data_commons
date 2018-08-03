# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:01:15 2018

@author: spauliuk
"""

import pymysql
import datetime
import IEDC_PW


#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')


cur = conn.cursor()

cur.execute("Show tables")
for row in cur:
    print(row)

cur.execute("DESCRIBE iedc_review.datasets")
DSD = []
for row in cur:
    print(row)
    DSD.append(row)

# Select all from table:
cur.execute("DESCRIBE iedc_review.licences")
for row in cur:
    print(row)

cur.execute("SELECT * FROM licences")
for row in cur:
    print(row)
    
cur.execute("SELECT * FROM iedc_review.datasets")
for row in cur:
    print(row)
    
cur.execute("SELECT * FROM classification_definition")
for row in cur:
    print(row)

cur.execute("SELECT * FROM classifiation_items")
for row in cur:
    print(row)
    
# Show table creation statement    
cur.execute("SHOW CREATE TABLE licences")
for row in cur:
    print(row)
    
cur.execute("SHOW CREATE TABLE data")
for row in cur:
    print(row)    
    
cur.execute("SHOW TABLE STATUS FROM iedc_review WHERE `name` LIKE 'datasets'")    
for row in cur:
    print(row)
    
# Get current auto_increment values:    
cur.execute("SELECT table_name, Auto_increment FROM information_schema.tables WHERE table_schema = DATABASE()")    
for row in cur:
    print(row)
    
# get total number of data
cur.execute("SELECT COUNT(*) FROM data")
for row in cur:
    print(row)    
    
# Change auto_increment    
cur.execute("ALTER TABLE iedc_review.licences AUTO_INCREMENT = 5")
cur.execute("ALTER TABLE iedc_review.datasets AUTO_INCREMENT = 1")
    
# Insert data into tables with auto_increment and default NULL columns:
SQL = "INSERT INTO iedc_review.licences (name,description) VALUES ('Crown Copyright','')"
cur.execute(SQL)
D = ['Test','']
SQL = "INSERT INTO iedc_review.licences (name,description) VALUES (%s,%s)"
cur.execute(SQL,('Test',''))
    
# Delete
cur.execute("DELETE FROM iedc_review.licences WHERE id = 5")    
cur.execute("DELETE FROM iedc_review.datasets WHERE id = 1") 

cur.execute("DELETE FROM iedc_review.datasets")

cur.execute("DELETE FROM iedc_review.data")
cur.execute("ALTER TABLE iedc_review.data AUTO_INCREMENT = 1")


cur.execute("DELETE FROM data")
cur.execute("ALTER TABLE data AUTO_INCREMENT = 1")
# get units
cur.execute("SELECT * FROM units")
for row in cur:
    print(row)
    
    
cur.execute("SELECT DISTINCT(process_id) FROM stocks")
for row in cur:
    print(row)    

# Insert into datasets:
# id is not set because of auto_increment






conn.commit()




cur.execute("SELECT count(*) FROM data")
for row in cur:
    print(row)


## 4) close connection
cur.close()
conn.close()
#
#    
#    
# The End