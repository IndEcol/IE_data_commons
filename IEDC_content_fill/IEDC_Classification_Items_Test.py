# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:11:13 2018

@author: spauliuk
"""


# Show table creation statement    
cur.execute("SHOW CREATE TABLE classifiation_items")
for row in cur:
    print(row)
    
    
# get total number of class. items
cur.execute("SELECT COUNT(*) FROM classifiation_items")
for row in cur:
    print(row)
   
# get set of classification ids:    
cur.execute("SELECT DISTINCT(classification_id) FROM classifiation_items")
for row in cur:
    print(row) 
    
# get set of classification_items:
cur.execute("SELECT * FROM classifiation_items WHERE classification_id = 3")
for row in cur:
    print(row)
    
    
    
    