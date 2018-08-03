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

#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

# Show auto_increments:
cur.execute("SELECT table_name, Auto_increment FROM information_schema.tables WHERE table_schema = DATABASE()")    
for row in cur:
    print(row) 
        
SQL_def = "INSERT INTO classification_definition (\
id,\
classification_Name,\
dimension,\
description,\
mutually_exclusive,\
collectively_exhaustive,\
reference,\
reserve1,\
reserve2,\
reserve3,\
reserve4,\
reserve5,\
meaning_attribute1,\
meaning_attribute2,\
meaning_attribute3,\
meaning_attribute4,\
meaning_attribute5,\
meaning_attribute6,\
meaning_attribute7,\
meaning_attribute8,\
meaning_attribute9,\
meaning_attribute10,\
meaning_attribute11,\
meaning_attribute12,\
meaning_attribute13,\
meaning_attribute14,\
meaning_attribute15\
) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    
# Create new classification: 17
# Change auto_increment    
cur.execute("ALTER TABLE classification_definition AUTO_INCREMENT = 17")
Class_no = 17
Class_name = 'steel_cycle_200R_materials_products'
Class_items_meaning = 'names of materials and products'
Class_description = 'materials and products for stocks and flows in dataset for global steel cycle'
Class_Items = ['landfill loss',
 'steel products',
 'products, packaging, appliances, other',
 'fabrication scrap',
 'obsolete products',
 'iron and steel castings',
 'pig iron',
 'crude steel',
 'transport equipment',
 'parts of manufactured goods',
 'all steel-containing products',
 'slag',
 'castings',
 'machinery',
 'finished steel',
 'steel scrap',
 'manufactured goods',
 'building and construction',
 'EoL products']

#cur.execute(SQL_def,(17,Class_name,6,Class_description,0,0,None,1,None,None,None,None,Class_items_meaning,None,\
#                     None,None,None,None,None,None,None,None,None,None,None,None,None))


# Add classification_items to classification_items:
cur.execute("SELECT DISTINCT(classification_id) FROM classification_items")
for row in cur:
    print(row)      
  
SQL_items = "INSERT INTO classification_items (\
classification_id,\
parent_id,\
description,\
reference,\
attribute1,\
attribute2,\
attribute3,\
attribute4,\
attribute5,\
attribute6,\
attribute7,\
attribute8,\
attribute9,\
attribute10,\
attribute11,\
attribute12,\
attribute13,\
attribute14,\
attribute15\
) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

#for m in range(0,len(Class_Items)):
#    cur.execute(SQL_items,(17,0,None,None,Class_Items[m],None,None,None,None,None,None,None,None,None,None,None,None,None,None))


  
# Close connection
cur.close()
conn.close()

