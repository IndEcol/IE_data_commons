# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:01:15 2018

@author: spauliuk
"""

import pymysql
import datetime
import IEDC_PW


conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

# Add 'Mt' to 'Gg' unit:
cur.execute("UPDATE units SET alt_unitcode = 'Mt' WHERE unitcode = 'Tg'") 

# fix misspelled æ:
cur.execute("UPDATE units SET unitcode = 'µs' WHERE unitcode = 'æs'") 
cur.execute("UPDATE units SET unitcode = 'µg' WHERE unitcode = 'æg'") 
cur.execute("UPDATE units SET unitcode = 'µWs' WHERE unitcode = 'æWs'") 
cur.execute("UPDATE units SET unitcode = 'µJ' WHERE unitcode = 'æJ'") 

cur.execute("SELECT * FROM units")
for row in cur:
    print(row)

## close connection
cur.close()
conn.close()
#
#    
#    
# The End