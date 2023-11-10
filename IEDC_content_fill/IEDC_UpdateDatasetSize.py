# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:01:15 2018

@author: spauliuk

The purpose of this script is to scan the entire dataset table and for each entry, determine how many data items are contained in the data table, and then update this number in the dataset table entry
"""

import pymysql
import IEDC_PW

#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')
cur = conn.cursor()

# Get current auto_increment value:        
cur.execute("SELECT table_name, Auto_increment FROM information_schema.tables WHERE table_schema = DATABASE()")    
for row in cur:
    print(row)
    if row[0] == 'datasets':
        AI = row[1]

A0 = 300
AI = 350
# Get dataset size and update datasets entry:        
for m in range(A0,AI):
    cur.execute("SELECT count(*) FROM data WHERE dataset_id = %s",m)
    for row in cur:
        Ts = row[0] #Ts stands for 'this size'
        print(Ts)
        cur.execute("UPDATE datasets SET dataset_size = %s WHERE id = %s",(Ts,m)) 

# Close connection
cur.close()
conn.close()
#
#    
#    
# The End