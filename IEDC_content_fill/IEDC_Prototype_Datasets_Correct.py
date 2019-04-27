# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:57:29 2017

@author: spauliuk
"""

import pymysql
import datetime
import numpy as np
import xlrd
from datetime import date, timedelta

import IEDC_PW
import IEDC_Paths

def from_excel_ordinal(ordinal, _epoch=date(1900, 1, 1)):
    if ordinal > 59:
        ordinal -= 1  # Excel leap year bug, 1900 is not a leap year!
    return _epoch + timedelta(days=ordinal - 1)  # epoch is day 1


#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

## Change datasets 1_UPI to 4_UPI:
#cur.execute("UPDATE datasets SET dataset_name = '4_UPI_USLCI_Aluminum_cold_rolling_at_plant', data_category = 4 WHERE id = 132")
#cur.execute("UPDATE datasets SET dataset_name = '4_UPI_USLCI_Chainsawing_delimbing', data_category = 4 WHERE id = 133")
#cur.execute("UPDATE datasets SET dataset_name = '4_UPI_USLCI_Electricity_lignite_coal_at_power_plant', data_category = 4 WHERE id = 134")
#cur.execute("UPDATE datasets SET dataset_name = '4_UPI_USLCI_Limestone_at_mine', data_category = 4 WHERE id = 135")    
#cur.execute("UPDATE datasets SET dataset_name = '4_UPI_USLCI_steel_liquid_at_plant', data_category = 4 WHERE id = 136")    

## Add datagroup it to dataset 130 (Steel Sankey Cullen 2012)
#cur.execute("UPDATE datasets SET datagroup_id = 8 WHERE id = 130")    

## Add description of pre 1900 steel cycle datasets 202 and 203:
#cur.execute("UPDATE datasets SET comment = 'only nonzero values are reported, no trade data for the years before 1900 were included' WHERE id = 202")    
#cur.execute("UPDATE datasets SET comment = 'only nonzero values are reported, no trade data for the years before 1900 were included' WHERE id = 203")    

# 4) close connection
cur.close()
conn.close()

