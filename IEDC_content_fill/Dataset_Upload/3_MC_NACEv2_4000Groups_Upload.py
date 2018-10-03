# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:57:29 2017

@author: spauliuk
"""

import pymysql
import numpy as np
import xlrd

import IEDC_PW


# Define mySQL command for data item insertion
SQL = "INSERT INTO data (\
dataset_id,\
aspect1,\
aspect2,\
aspect3,\
aspect4,\
aspect5,\
aspect6,\
aspect7,\
aspect8,\
aspect9,\
aspect10,\
aspect11,\
aspect12,\
value,\
unit_nominator,\
unit_denominator,\
stats_array_1,\
stats_array_2,\
stats_array_3,\
stats_array_4,\
comment,\
reserve1,\
reserve2,\
reserve3\
) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

# get TOC entry for dataset:
cur.execute("SELECT id FROM datasets WHERE dataset_name = '3_MC_NACEv2_4000Groups' ")
DS_id = cur.fetchall()[0][0]
cur.execute("SELECT aspect_1_classification FROM datasets WHERE dataset_name = '3_MC_NACEv2_4000Groups' ")
C1id = cur.fetchall()[0][0]
cur.execute("SELECT aspect_2_classification FROM datasets WHERE dataset_name = '3_MC_NACEv2_4000Groups' ")
C2id = cur.fetchall()[0][0]

# 2 Classifications are used, get their items:
cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", C1id)
C1Tuples = cur.fetchall()
C1IDs    = [x[0] for x in C1Tuples]
C1Labels = [x[1] for x in C1Tuples]

cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", C2id)
C2Tuples = cur.fetchall()
C2IDs    = [x[0] for x in C2Tuples]
C2Labels = [x[1] for x in C2Tuples]


# Open excel file with data
FilePath  = 'C:\\Users\\spauliuk\\FILES\\ARBEIT\\PROJECTS\\Database\\IE_DataCommons\\DATA\\Data_Custom_Insertion\\3_MC_NACEv2_4000Groups\\3_MC_NACEv2_4000Groups.xls'
DataFile  = xlrd.open_workbook(FilePath)
DataSheet = DataFile.sheet_by_name('3_MC_NACEv2_4000Groups')

# loop over data from Excel reference dataset file
for m in range(0,4047): # rows
    print(m)
    for n in range(0,11): # cols
	# get row label, column label, and value
        ProductID  = DataSheet.cell_value(m +15,8)
        MaterialID = DataSheet.cell_value(14, n +9)
        ContValue  = DataSheet.cell_value(m +15,n +9)
        
	# match row and column labels to classification_items entry
        Mat_Pos    = C1IDs[C1Labels.index(MaterialID)]
        Prod_Pos   = C2IDs[C2Labels.index(ProductID)]
        
        # Read and parse uncertainty string:
        UncString  = DataSheet.cell_value(m +8115 ,n +9)
        UncParts   = UncString.split(';')
        U1 = 13
        U2 = np.float(UncParts[1])
        U3 = np.float(UncParts[2])
        U4 = None
        
        # Add data into db:
        cur.execute(SQL,(DS_id,Mat_Pos,Prod_Pos,None,None,None,None,None,None,None,None,None,None,ContValue,\
                     2,2,U1,U2,U3,U4,None,None,None,None))

    
# Close connection
cur.close()
conn.close()



# End