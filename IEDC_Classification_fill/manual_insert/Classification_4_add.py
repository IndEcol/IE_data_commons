# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:47:46 2018

@author: spauliuk

This script is obsolete! Is now class. 23.

"""
import pymysql
import numpy as np
import xlrd, xlwt

import IEDC_PW
import IEDC_Paths

#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

# Update classification items for class. 4:
cur.execute("SELECT attribute1_oto FROM classification_items  WHERE classification_id = 4")
for row in cur:
    print(row)
    
Update_Class_Items = ['magnesium',
'zinc',
'lead',
'gold',
'silver',
'tin',
'lithium',
'nickel',
'cobalt',
'neodymium',
'platinum',
'paladium',
'rhodium',
'arsenic',
'antimony',
'silicon',
'fiberglass',
'silica sand',
'zinc oxide',
'sulphur',
'naphtha',
'paraffin',
'sulphuric acid',
'boron',
'ethylene glycol',
'poly acrylic acid',
'carboxymethyl cellulose',
'polyvinylidene difluoride',
'carbon black',
'graphite',
'textiles',
'electronic misc.']


for m in range(0,len(Update_Class_Items)):
    Ucount = m + 1
    OldAttName = 'reserved_' + str(Ucount)
    #cur.execute("UPDATE classification_items SET attribute1_oto = %s WHERE classification_id = 4 AND attribute1_oto = %s",(Update_Class_Items[m],OldAttName))
  
# Close connection
cur.close()
conn.close()

