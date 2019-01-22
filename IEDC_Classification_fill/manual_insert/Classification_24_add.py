# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:47:46 2018

@author: spauliuk


"""
import pymysql
import numpy as np
import xlrd, xlwt

import IEDC_PW
import IEDC_Paths

conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

# Create new classification id 24:
cur.execute("SELECT * FROM classification_definition  WHERE id = 24")
for row in cur:
    print(row)

cur.execute("SELECT attribute1_oto FROM classification_items  WHERE classification_id = 24")
for row in cur:
    print(row)
    
# update definition:
cur.execute("UPDATE classification_definition SET classification_name = 'global_steel_cycle_Regions', dimension = 4, description = 'regions used in global steel cycle project', mutually_exclusive = 0, collectively_exhaustive = 0, general = 0, created_from_dataset = 0, meaning_attribute1 = 'region name' WHERE id = 24")    
    
# delete items if present:
cur.execute("DELETE FROM classification_items WHERE classification_id = 24")

# define and insert new items:
    
New_Class_Items = ['North America (USA and Canada)',
'Latin America (the entire Americas without the US and Canada)',
'Western Europe (all European countries which have not been part of the former Soviet Union, not Turkey and Cyprus)',
'Commonwealth of Independent States (CIS) and other states that were part of the Soviet Union',
'Africa',
'Middle East, including Turkey and Cyprus',
'India',
'China',
'Developed Asia and Oceania: Japan, South Korea, Australia, New Zealand',
'Developing Asia and Oceania',
'Global']


for m in range(0,len(New_Class_Items)):
    cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(24,New_Class_Items[m]))
  
# Close connection
cur.close()
conn.close()

