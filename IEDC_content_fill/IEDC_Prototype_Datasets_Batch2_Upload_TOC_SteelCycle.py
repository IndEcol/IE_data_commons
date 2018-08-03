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

# Define mySQL command for dataset insertion
SQL = "INSERT INTO datasets (\
dataset_name,\
dataset_version,\
datagroup_id,\
data_category,\
data_type,\
data_layer,\
process_scope,\
process_resolution,\
product_scope,\
product_resolution,\
material_scope,\
material_resolution,\
regional_scope,\
regional_resolution,\
temporal_scope,\
temporal_resolution,\
description,\
keywords,\
data_provenance,\
dataset_size,\
comment,\
aspect_1,\
aspect_1_classification,\
aspect_2,\
aspect_2_classification,\
aspect_3,\
aspect_3_classification,\
aspect_4,\
aspect_4_classification,\
aspect_5,\
aspect_5_classification,\
aspect_6,\
aspect_6_classification,\
aspect_7,\
aspect_7_classification,\
aspect_8,\
aspect_8_classification,\
aspect_9,\
aspect_9_classification,\
aspect_10,\
aspect_10_classification,\
aspect_11,\
aspect_11_classification,\
aspect_12,\
aspect_12_classification,\
tupel_notation,\
semantic_string_example,\
semantic_string_general,\
type_of_source,\
project_license,\
main_author,\
dataset_link,\
dataset_format,\
project_report,\
suggested_citation,\
visible,\
access_date,\
submission_date,\
submitting_user,\
dataset_conversion_info,\
review_date,\
review_user,\
review_comment,\
reserve1,\
reserve2,\
reserve3,\
reserve4,\
reserve5\
) Values(\
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

cur.execute("SELECT table_name, Auto_increment FROM information_schema.tables WHERE table_schema = DATABASE()")    
for row in cur:
    print(row)

# Read ancillary table items:
cur.execute("SELECT id,name FROM types")
Tuples = cur.fetchall()
DTypes = [x[1] for x in Tuples]    
    
cur.execute("SELECT id,name FROM layers")
Tuples = cur.fetchall()
DLayers = [x[1] for x in Tuples] 

cur.execute("SELECT id,name FROM provenance")
Tuples = cur.fetchall()
DProv = [x[1] for x in Tuples] 

cur.execute("SELECT id,name FROM licences")
Tuples = cur.fetchall()
DLicen = [x[1] for x in Tuples] 

cur.execute("SELECT id,name FROM source_type")
Tuples = cur.fetchall()
DSource = [x[1] for x in Tuples] 

cur.execute("SELECT id,name FROM users")
Tuples = cur.fetchall()
DUsers = [x[1] for x in Tuples] 

cur.execute("SELECT id,aspect,dimension FROM aspects")
Tuples    = cur.fetchall()
DAspects  = [x[1] for x in Tuples] 
DAspectsD = [x[2] for x in Tuples] 

cur.execute("SELECT dimension FROM classification_definition")
Tuples = cur.fetchall()
DClassDefsD = [x[0] for x in Tuples] 
    
# Read datasets
TOCFile  = xlrd.open_workbook(IEDC_Paths.DataSetPath + 'IEDC_Prototype_Datasets_Batch1_Upload.xlsx')
TOC = TOCFile.sheet_by_name('DataSets_SteelCycle')

Offset = 0
No_DS = 45

# loop over datasets
for m in range(Offset,No_DS):
    # Define default data:
    D = [] # Data items list
    for n in range(0,69):
        D.append(None)
    # loop over items in dataset:

    # 0 ID: auto_increment
    D[1] = TOC.cell_value(4,m +4) #1: name
    if  TOC.cell_value(5,m +4) != 'NULL': #2: version
        D[2] = TOC.cell_value(5,m +4)
    if  TOC.cell_value(6,m +4) != 'NULL': #3: datagroup
        D[3] = TOC.cell_value(6,m +4)
    
    D[4] = int(TOC.cell_value(7,m +4)) # 4: data category
    D[5] = DTypes.index(TOC.cell_value(8,m +4)) # 5: data type
    D[6] = DLayers.index(TOC.cell_value(9,m +4)) # 6: data layer
    
    for n in range(7,19):
        D[n]   = TOC.cell_value(n +3,m +4) # system location description, dataset description, keywords

    D[19]      = DProv.index(TOC.cell_value(22,m +4)) # 19: data provenance

    D[20]      = int(TOC.cell_value(23,m +4)) # 20: dataset size
    D[21]      = TOC.cell_value(24,m +4) # 21: comment
    
    # Read aspects
    for n in range(0,12):
        a = 2*n   + 22
        c = 2*n+1 + 22
        if TOC.cell_value(a +3,m +4) != 'none':
            D[a]      = DAspects.index(TOC.cell_value(a +3,m +4))  # aspect and classification 1
            if TOC.cell_value(c +3,m +4) == 'custom':
                D[c]  = 0
            else:
                D[c]  =  int(TOC.cell_value(c +3,m +4))
                if DClassDefsD[D[c] -1] !=  DAspectsD[D[a]]:
                    print('Aspect and classification mismatch for dataset %s and aspect %s.' %(m+1) %n)

    D[46]      = TOC.cell_value(49,m +4) # 46: tuple notation
    D[47]      = TOC.cell_value(50,m +4) # 47: semantic string example
    D[48]      = TOC.cell_value(51,m +4) # 48: semantic string general
    D[49]      = DSource.index( TOC.cell_value(52,m +4)) # 49: data source
    D[50]      = DLicen.index(TOC.cell_value(53,m +4)) # 50: License
        
    for n in range(51,57):
        D[n]   = TOC.cell_value(n +3,m +4)  
    
    if TOC.cell_value(57 +3,m +4) != 'NULL':
        D[57]   = datetime.datetime.combine(from_excel_ordinal(TOC.cell_value(57 +3,m +4)), datetime.time())
    D[58]   = datetime.datetime.combine(from_excel_ordinal(TOC.cell_value(58 +3,m +4)), datetime.time())
    D[59]   = DUsers.index(TOC.cell_value(62,m +4)) +1 # 59: User
    D[60]   = TOC.cell_value(60 +3,m +4)  

    cur.execute(SQL,(D[1],D[2],D[3],D[4],D[5],D[6],D[7],D[8],D[9],D[10],\
                     D[11],D[12],D[13],D[14],D[15],D[16],D[17],D[18],D[19],D[20],\
                     D[21],D[22],D[23],D[24],D[25],D[26],D[27],D[28],D[29],D[30],\
                     D[31],D[32],D[33],D[34],D[35],D[36],D[37],D[38],D[39],D[40],\
                     D[41],D[42],D[43],D[44],D[45],D[46],D[47],D[48],D[49],D[50],\
                     D[51],D[52],D[53],D[54],D[55],D[56],D[57],D[58],D[59],D[60],\
                     D[61],D[62],D[63],D[64],D[65],D[66],D[67],D[68]))


    
    
# Close connection
cur.close()
conn.close()

# Correct for dataset "2_S_steel_200R_Landfills", formerly incorrectly labelled as "2_IUS_steel_200R_Landfills"
# cur.execute("UPDATE datasets SET dataset_name = '2_S_steel_200R_Landfills' WHERE id = 62")


