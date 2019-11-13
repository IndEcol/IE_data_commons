# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:57:29 2017

@author: spauliuk
"""

import pymysql
import datetime
import numpy as np
from os import walk, path
import xlrd
from datetime import date, timedelta
import csv

import IEDC_PW
import IEDC_Paths

def from_excel_ordinal(ordinal, _epoch=date(1900, 1, 1)):
    if ordinal > 59:
        ordinal -= 1  # Excel leap year bug, 1900 is not a leap year!
    return _epoch + timedelta(days=ordinal - 1)  # epoch is day 1

# Define mySQL command for dataset insertion
SQL = "INSERT INTO classification_items (\
classification_id,\
parent_id,\
description,\
reference,\
attribute1_oto,\
attribute2_oto,\
attribute3_oto,\
attribute4_oto,\
attribute5_anc,\
attribute6_anc,\
attribute7_anc,\
attribute8_anc,\
attribute9_anc,\
attribute10_anc,\
attribute11_anc,\
attribute12_anc,\
attribute13_anc,\
attribute14_anc,\
attribute15_anc) Values(\
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

# Scan folder for .csv files
f = []
for (dirpath, dirnames, filenames) in walk(IEDC_Paths.Class_ItemPath):
    f.extend(filenames)
    break

for filename in f:
    FilePath = path.join(IEDC_Paths.Class_ItemPath,filename)
    print(FilePath)
    reservedcount = 1
    DInsert = False
    with open(FilePath, encoding = 'utf-8') as fi:
        reader = csv.reader(fi, delimiter=';', quotechar='"')
        for cols in reader:
            # parse row with items and insert into mysql
            try:  # Check whether line contains classification item
                Id = int(cols[1])
            except:
                Id = -1
            if Id != -1:
                D = [] # Data items list
                D.append(Id)
                for m in range(2,20):
                    if cols[m] == '':
                        D.append(None)
                    elif cols[m] == 'reserved':
                        D.append('reserved_' + str(reservedcount))
                        reservedcount +=1
                    else:
                        D.append(cols[m])
                # Add data into db:
#                cur.execute(SQL,(D[0],D[1],D[2],D[3],D[4],D[5],D[6],D[7],D[8],D[9],D[10],\
#                         D[11],D[12],D[13],D[14],D[15],D[16],D[17],D[18]))
                print(D[4])
                
            

# Check
cur.execute("SELECT COUNT(*) FROM classification_items")
for row in cur:
    print(row)    

# Other
#cur.execute("SELECT * FROM classification_items")
#for row in cur:
#    print(row)  
#    
#cur.execute("DELETE FROM classification_items")    
#cur.execute("ALTER TABLE classification_items AUTO_INCREMENT = 1")
    
#    FilePath = 'C:\\Users\\spauliuk\\FILES\\ARBEIT\\PROJECTS\\Database\\IE_DataCommons\\Software\\IEDC_Classification_fill\\generic_materials_waste_data.csv'    

# Extra: Add leading 0 where missing for classification NACEv2 (id = 5)
#cur.execute("SELECT COUNT(*) FROM classification_items WHERE classification_id = 5 AND LENGTH(attribute1_oto) = 7")
#for row in cur:
#    print(row)   
#    
#cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_id = 5 AND LENGTH(attribute1_oto) = 7")    
#for row in cur:    
#    print(row[0])
#    cur.execute("UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s",('0' + row[0], row[0])) 

# Close connection
cur.close()
conn.close()


