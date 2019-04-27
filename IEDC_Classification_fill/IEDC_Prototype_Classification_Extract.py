# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:57:29 2017

@author: spauliuk

This script extract a given classification to Excel.
"""

import pymysql
import datetime
import numpy as np
from os import walk, path
import xlrd, xlwt
from datetime import date, timedelta
import csv

import IEDC_PW
import IEDC_Paths

#  Set classification ID:
ClassNo = 2

#conn    = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn    = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')



cur = conn.cursor()


myfont = xlwt.Font()
myfont.bold = True
mystyle = xlwt.XFStyle()
mystyle.font = myfont

Result_workbook  = xlwt.Workbook(encoding = 'ascii') 

Labels = ['id','classification_id','parent_id','description	','reference','attribute1_oto','attribute2_oto','attribute3_oto','attribute4_oto','attribute5_anc','attribute6_anc','attribute7_anc','attribute8_anc','attribute9_anc','attribute10_anc','attribute11_anc','attribute12_anc','attribute13_anc','attribute14_anc','attribute15_anc']

Result_worksheet = Result_workbook.add_sheet('Classification_items')
for m in range(0,len(Labels)):     
    Result_worksheet.write(0, m, label = Labels[m], style = mystyle)

cur.execute("SELECT * FROM classification_items WHERE classification_id = %s",ClassNo)
n = 1
for row in cur:
    print(row)  
    for m in range(0,len(row)):
        Result_worksheet.write(n, m, label = row[m])
    n +=1

Result_workbook.save(IEDC_Paths.Class_ItemPath + 'Classification_' + str(ClassNo) + '_export.xls') 


# Close connection
cur.close()
conn.close()


