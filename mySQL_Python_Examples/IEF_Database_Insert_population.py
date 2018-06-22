# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:57:29 2017

@author: spauliuk
"""

import pymysql
import datetime
import numpy as np

conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user='root', passwd='industrial', db='iefdatabase_test')

cur = conn.cursor()

# 0) add new unit to unit table:
sql = "INSERT INTO iefdatabase_test.unit_classification (UnitID,SiUnitID,UnitCode,UnitName,Factor)VALUES(49,1,'k','thousand',1000);"
cur.execute(sql)

# 1) Add new data set to dataset table:
sql = "INSERT INTO iefdatabase_test.dataset (System_ID,System_definition,Dataset_name,Reference_date,Most_recent_update,Corresponding_author_info,Other_author_info,Document_reference,region,Time_period_of_analysis,Indicator_element,Comment)VALUES(2, 'XXX.png', 'Historic population by country', %s, %s, 'Pauliuk, Stefan', 'Tao Wang, Daniel B Müller', '10.1016/j.resconrec.2012.11.008', 'World', '1700-2008', 'Population', 'Compiled from other statistical sources');"
cur.execute(sql,(datetime.datetime(2012, 8, 5, 0, 0),datetime.datetime(2012, 8, 5, 0, 0)))

# 2) Add processes for new data set to process table:
sql = "INSERT INTO iefdatabase_test.process_list (system_id,process_id,process_name,process_code,process_type,comment,color,angle,width,height,xPos,yPos)VALUES(2,1,'Population', '', '', '', '[(35,35,35)]', '[0]', '[100.00]', '[100.00]', '[300]', '[200]');"
cur.execute(sql)

# 3) Read population dataset from xls and insert into db stocks:
system_id = 2
stock_dataset_number = 1
Process_id = 1

FilePath = 'C:\\Users\\spauliuk\\FILES\\ARBEIT\\PROJECTS\\Database\\IndEcolFreiburg_Database\\CSVexport_SteelCycle_Population\\P1_D.csv'
lines = open(FilePath,'r').read().split('\n')
for line in lines:
    if line != '':
        cols = line.split(',')
        CountryID = int(cols[3])
        YearID    = int(cols[4])
        PopValue  = np.float(cols[8])
        # Add data into db:
        sql = "INSERT INTO iefdatabase_test.stocks (system_id,stock_dataset_number,process_id,country_iso_code,year,age_cohort,indicator_element,aspect_of_dataset,value,error_type,error_value_1,error_value_2,data_quality,unit_id,comment )VALUES(%s,%s,%s,'%s',%s,'','Population','Stock',%s,'','','','',49,'');"
        cur.execute(sql,(system_id,stock_dataset_number,Process_id,CountryID,YearID,PopValue))
        stock_dataset_number += 1

# 4) close connection
cur.close()
conn.close()

