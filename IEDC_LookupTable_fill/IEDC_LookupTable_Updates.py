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

## Add 'Mt' to 'Gg' unit:
#cur.execute("UPDATE units SET alt_unitcode = 'Mt' WHERE unitcode = 'Tg'") 
#
## fix misspelled æ:
#cur.execute("UPDATE units SET unitcode = 'µs' WHERE unitcode = 'æs'") 
#cur.execute("UPDATE units SET unitcode = 'µg' WHERE unitcode = 'æg'") 
#cur.execute("UPDATE units SET unitcode = 'µWs' WHERE unitcode = 'æWs'") 
#cur.execute("UPDATE units SET unitcode = 'µJ' WHERE unitcode = 'æJ'") 
#
#cur.execute("SELECT * FROM units")
#for row in cur:
#    print(row)


#cur.execute("SELECT * FROM stats_array")
#for row in cur:
#    print(row)
    
#
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (5,'l','litre',0.001)"
#cur.execute(SQL)

# Add new uncertainty options to stats_array
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('1stddev','symmetric uncertainty range, +/-1 standard deviation, same unit as value','standard deviation (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('2stddevs','symmetric uncertainty range, +/-2 standard deviations, same unit as value','2 standard deviations (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('3stddevs','symmetric uncertainty range, +/-3 standard deviations, same unit as value','3 standard deviations (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('1stddev%','symmetric uncertainty range, +/-1 standard deviation, in % of value','standard deviation in % (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('2stddevs%','symmetric uncertainty range, +/-2 standard deviations, in % of value','2 standard deviations in % (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('3stddevs%','symmetric uncertainty range, +/-3 standard deviations, in % of value','3 standard deviations in % (half the uncertainty range)')") 

## close connection
cur.close()
conn.close()
#
#    
#    
# The End
