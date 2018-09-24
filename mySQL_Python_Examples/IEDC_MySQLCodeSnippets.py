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

cur.execute("SELECT index_letter FROM aspects")
for row in cur:
    print(row)
    
cur.execute("SELECT index_letter FROM aspects WHERE index_letter = 'D' ")
for row in cur:
    print(row)

cur.execute("SELECT * FROM types")
for row in cur:
    print(row)    
    
cur.execute("SELECT * FROM datasets")
for row in cur:
    print(row)
    
cur.execute("SELECT * FROM classification_definition")
for row in cur:
    print(row)

cur.execute("SELECT attribute1 FROM classification_items WHERE classification_id = 17")
for row in cur:
    print(row)
    
# Show table creation statement    
cur.execute("SHOW CREATE TABLE users")
for row in cur:
    print(row)   
    
cur.execute("SHOW CREATE TABLE datasets")
for row in cur:
    print(row)  
    
cur.execute("SHOW CREATE TABLE datagroups")
for row in cur:
    print(row)      
    
cur.execute("SHOW CREATE TABLE classification_items")
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
    
# get total number of classification_items
cur.execute("SELECT COUNT(*) FROM classification_items")
for row in cur:
    print(row)    

# Change auto_increment    
#cur.execute("ALTER TABLE iedc_review.licences AUTO_INCREMENT = 5")
#cur.execute("ALTER TABLE iedc_review.datasets AUTO_INCREMENT = 1")
    
# Insert data into tables with auto_increment and default NULL columns:
#SQL = "INSERT INTO iedc_review.licences (name,description) VALUES ('Crown Copyright','')"
#cur.execute(SQL)
#D = ['Test','']
#SQL = "INSERT INTO iedc_review.licences (name,description) VALUES (%s,%s)"
#cur.execute(SQL,('Test',''))
    
# Delete
#cur.execute("DELETE FROM iedc_review.licences WHERE id = 5")    
#cur.execute("DELETE FROM iedc_review.datasets WHERE id = 1") 
#
#cur.execute("DELETE FROM datagroups")
#cur.execute("DELETE FROM datasets")
#cur.execute("DELETE FROM classification_items")
#
#cur.execute("DELETE FROM iedc_review.data")
#cur.execute("ALTER TABLE datagroups AUTO_INCREMENT = 1")
#
#
#cur.execute("DELETE FROM data")
#cur.execute("ALTER TABLE datasets AUTO_INCREMENT = 1")
    
# get units
cur.execute("SELECT * FROM licences")
for row in cur:
    print(row)
    
    cur.execute("SELECT DISTINCT(process_id) FROM stocks")
for row in cur:
    print(row)    

# Insert into datasets:
# id is not set because of auto_increment

cur.execute("SELECT dataset_name,aspect_4_classification FROM datasets WHERE id = 11") 
for row in cur:
    print(row) 
    
#cur.execute("UPDATE datasets SET aspect_4_classification = 14 WHERE id = 10") 


conn.commit()

# Create new read only user
'''
CREATE USER 'iedc_guest'@'www.industrialecology.uni-freiburg.de' IDENTIFIED BY '...';
GRANT ALL ON iedc.* TO 'iedc_guest'@'www.industrialecology.uni-freiburg.de';
FLUSH PRIVILEGES;

CREATE USER 'iedc_guest'@'%' IDENTIFIED BY '...';
GRANT ALL ON iedc.* TO 'iedc_guest'@'%';
FLUSH PRIVILEGES;
'''


cur.execute("SELECT * FROM datagroups")
for row in cur:
    print(row)

m=10
print('Aspect and classification mismatch for dataset %s and aspect %s.' % ((m+1), m))

## 4) close connection
cur.close()
conn.close()
#
#    
#    
# The End