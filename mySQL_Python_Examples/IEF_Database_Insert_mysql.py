# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:57:29 2017

@author: spauliuk
"""

import pymysql

conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user='root', passwd='industrial', db='iefdatabase_test')

cur = conn.cursor()

cur.execute("Show tables")
cur.execute("DESCRIBE iefdatabase_test.countries")

cur.execute("SELECT * FROM iefdatabase_test.countries WHERE id=111")
cur.execute("SELECT * FROM iefdatabase_test.countries")

sql = "INSERT INTO iefdatabase_test.countries (id,ISO2,ISO3,ISO_code,country_name,continent,UN_region,DESIRE_region,DESIRE_region_name,DESIRE_code,UN_member,Official_Country,Alternative_ISO3,Alternative_Name1,Alternative_Name2,Alternative_Name3,Alternative_Name4,Alternative_Name5,Alternative_Name6,Alternative_Name7)VALUES (1111,'','',11000,'Rest of the world','','','','','',0,0,'','','','','','','','');"
cur.execute(sql)

print(cur.description)

cur.execute("SELECT * FROM iefdatabase_test.countries WHERE id=1111")
cur.execute("SELECT * FROM iefdatabase_test.dataset")
cur.execute("SELECT * FROM iefdatabase_test.unit_classification")
cur.execute("SELECT * FROM iefdatabase_test.stocks WHERE system_id = 2")
cur.execute("SELECT * FROM iefdatabase_test.stocks WHERE system_id = 1 and stock_dataset_number = 12")

for row in cur:
    print(row)

sql = "INSERT INTO iefdatabase_test.countries (id,ISO2,ISO3,ISO_code,country_name,continent,UN_region,DESIRE_region,DESIRE_region_name,DESIRE_code,UN_member,Official_Country,Alternative_ISO3,Alternative_Name1,Alternative_Name2,Alternative_Name3,Alternative_Name4,Alternative_Name5,Alternative_Name6,Alternative_Name7)VALUES (1111,'','',11000,'Rest of the world','','','','','',0,0,'','','','','','','','');"
cur.execute(sql)
(1, 'XXX.png', 'Global multiregional steel cycle model, model (a), mean values', datetime.datetime(2012, 8, 5, 0, 0), datetime.datetime(2012, 8, 5, 0, 0), 'Pauliuk, Stefan', 'Tao Wang, Daniel B Müller', '10.1016/j.resconrec.2012.11.008', 'World', '1700-2008', 'Iron', '')




cur.close()
conn.close()

