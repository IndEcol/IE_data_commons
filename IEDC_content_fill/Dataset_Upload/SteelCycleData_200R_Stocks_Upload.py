# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:57:29 2017

@author: spauliuk
"""

import pymysql
import numpy as np

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

# PART 1: Stocks

# Get dataset lists:
StockFileList    = ['S_12_D','S_18_D','S_19_D','S_20_D']  
StockDataSetList = ['2_IUS_steel_200R','2_S_steel_200R_Slag','2_S_steel_200R_Obsolete','2_S_steel_200R_Landfills']
StockMatlList    = ['all steel-containing products','slag','obsolete products','landfill loss']

for ds in range(0,len(StockFileList)):
    print(StockDataSetList[ds])
    # get TOC entry for dataset:
    cur.execute("SELECT id FROM datasets WHERE dataset_name = %s ",(StockDataSetList[ds]))
    DS_id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_1_classification FROM datasets WHERE dataset_name = %s ",(StockDataSetList[ds]))
    C1id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_2_classification FROM datasets WHERE dataset_name = %s ",(StockDataSetList[ds]))
    C2id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_3_classification FROM datasets WHERE dataset_name = %s ",(StockDataSetList[ds]))
    C3id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_4_classification FROM datasets WHERE dataset_name = %s ",(StockDataSetList[ds]))
    C4id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_5_classification FROM datasets WHERE dataset_name = %s ",(StockDataSetList[ds]))
    C5id = cur.fetchall()[0][0]

    
    # 5 Classifications are used, get their items:
    cur.execute("SELECT id,attribute2_oto FROM classification_items WHERE classification_id = %s ", C1id)
    C1Tuples = cur.fetchall()
    C1IDs    = [x[0] for x in C1Tuples]
    C1Labels = [int(x[1]) for x in C1Tuples]
    
    cur.execute("SELECT id,attribute3_oto FROM classification_items WHERE classification_id = %s ", C2id)
    C2Tuples = cur.fetchall()
    C2IDs    = [x[0] for x in C2Tuples]
    C2Labels = [x[1] for x in C2Tuples]
    
    cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", C3id)
    C3Tuples = cur.fetchall()
    C3IDs    = [x[0] for x in C3Tuples]
    C3Labels = [int(x[1]) for x in C3Tuples]

    cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", C4id)
    C4Tuples = cur.fetchall()
    C4IDs    = [x[0] for x in C4Tuples]
    C4Labels = [x[1] for x in C4Tuples]

    cur.execute("SELECT id,attribute4_oto FROM classification_items WHERE classification_id = %s ", C5id)
    C5Tuples = cur.fetchall()
    C5IDs    = [x[0] for x in C5Tuples]
    C5Labels = [int(x[1]) for x in C5Tuples]
    
    # Open csv file with data
    FilePath = 'C:\\Users\\spauliuk\\FILES\\ARBEIT\\PROJECTS\\Database\\IndEcolFreiburg_Database_TestCase\\CSVExport\\' + StockFileList[ds] + '.csv'
    lines = open(FilePath,'r').read().split('\n')
    for line in lines:
        if line != '':
            cols = line.split(',')
            ProcessID = int(cols[2])
            ElementID = 'Fe'
            YearID    = int(cols[4])
            ProductID = StockMatlList[ds]
            CountryID = int(cols[3])
            
            StockValue= np.float(cols[8])
    
    	# match labels to classification_items entry
            Proc_Pos    = C1IDs[C1Labels.index(ProcessID)]
            Elem_Pos    = C2IDs[C2Labels.index(ElementID)]
            Year_Pos    = C3IDs[C3Labels.index(YearID)]
            Prod_Pos    = C4IDs[C4Labels.index(ProductID)]
            Coun_Pos    = C5IDs[C5Labels.index(CountryID)]
            
            # Set unit
            UnitnID  = 47
            UnitdnID = 1
            # Set uncertainty string:
            
            U1 = 1
            U2 = None
            U3 = None
            U4 = None
            
            # Add data into db:
#            cur.execute(SQL,(DS_id,Proc_Pos,Elem_Pos,Year_Pos,Prod_Pos,Coun_Pos,None,None,None,None,None,None,None,StockValue,\
#                         UnitnID,UnitdnID,U1,U2,U3,U4,None,None,None,None))

 
# Close connection
cur.close()
conn.close()



# End



