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


# PART 2: Flows

# Get dataset lists:
FlowFileList    = ['F_11_12_D_1700']
 
FlowDataSetList = ['1_F_steel_200R_F_11_12_final_steel_consumption_pre_1900']

FlowMatlList    = ['all steel-containing products']

for ds in range(0,len(FlowFileList)):
    print(FlowDataSetList[ds])
    # get TOC entry for dataset:
    cur.execute("SELECT id FROM datasets WHERE dataset_name = %s ",(FlowDataSetList[ds]))
    DS_id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_1_classification FROM datasets WHERE dataset_name = %s ",(FlowDataSetList[ds]))
    C1id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_2_classification FROM datasets WHERE dataset_name = %s ",(FlowDataSetList[ds]))
    C2id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_3_classification FROM datasets WHERE dataset_name = %s ",(FlowDataSetList[ds]))
    C3id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_4_classification FROM datasets WHERE dataset_name = %s ",(FlowDataSetList[ds]))
    C4id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_5_classification FROM datasets WHERE dataset_name = %s ",(FlowDataSetList[ds]))
    C5id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_6_classification FROM datasets WHERE dataset_name = %s ",(FlowDataSetList[ds]))
    C6id = cur.fetchall()[0][0]
    cur.execute("SELECT aspect_7_classification FROM datasets WHERE dataset_name = %s ",(FlowDataSetList[ds]))
    C7id = cur.fetchall()[0][0]
    
    # 5 Classifications are used, get their items:
    cur.execute("SELECT id,attribute3_oto FROM classification_items WHERE classification_id = %s ", C1id)
    C1Tuples = cur.fetchall()
    C1IDs    = [x[0] for x in C1Tuples]
    C1Labels = [x[1] for x in C1Tuples]
    
    cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", C2id)
    C2Tuples = cur.fetchall()
    C2IDs    = [x[0] for x in C2Tuples]
    C2Labels = [x[1] for x in C2Tuples]
    
    cur.execute("SELECT id,attribute2_oto FROM classification_items WHERE classification_id = %s ", C3id)
    C3Tuples = cur.fetchall()
    C3IDs    = [x[0] for x in C3Tuples]
    C3Labels = [int(x[1]) for x in C3Tuples]

    cur.execute("SELECT id,attribute4_oto FROM classification_items WHERE classification_id = %s ", C4id)
    C4Tuples = cur.fetchall()
    C4IDs    = [x[0] for x in C4Tuples]
    C4Labels = [int(x[1]) for x in C4Tuples]

    cur.execute("SELECT id,attribute2_oto FROM classification_items WHERE classification_id = %s ", C5id)
    C5Tuples = cur.fetchall()
    C5IDs    = [x[0] for x in C5Tuples]
    C5Labels = [int(x[1]) for x in C5Tuples]
    
    cur.execute("SELECT id,attribute4_oto FROM classification_items WHERE classification_id = %s ", C6id)
    C6Tuples = cur.fetchall()
    C6IDs    = [x[0] for x in C6Tuples]
    C6Labels = [int(x[1]) for x in C6Tuples]

    cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", C7id)
    C7Tuples = cur.fetchall()
    C7IDs    = [x[0] for x in C7Tuples]
    C7Labels = [int(x[1]) for x in C7Tuples]    
    
    # Open csv file with data
    FilePath = 'C:\\Users\\spauliuk\\FILES\\ARBEIT\\PROJECTS\\Database\\IndEcolFreiburg_Database_TestCase\\CSVExport\\' + FlowFileList[ds] + '.csv'
    lines = open(FilePath,'r').read().split('\n')
    for line in lines:
        if line != '':
            cols = line.split(',')
            ElementID = 'Fe'
            ProductID = FlowMatlList[ds]
            OrProceID = int(cols[2])
            OrRegID   = int(cols[4])
            DestProID = int(cols[3])
            DestRegID = int(cols[5])
            YearID    = int(cols[6])
            
            FlowValue= np.float(cols[9])
    
    	# match labels to classification_items entry
            Elem_Pos    = C1IDs[C1Labels.index(ElementID)]
            Prod_Pos    = C2IDs[C2Labels.index(ProductID)]
            OrPr_Pos    = C3IDs[C3Labels.index(OrProceID)]
            OrRe_Pos    = C4IDs[C4Labels.index(OrRegID)]            
            DesP_Pos    = C5IDs[C5Labels.index(DestProID)]            
            DesR_Pos    = C6IDs[C6Labels.index(DestRegID)]
            Year_Pos    = C7IDs[C7Labels.index(YearID)]
            
            # Set unit
            UnitnID  = 47
            UnitdnID = 44
            # Set uncertainty string:
            
            U1 = 1
            U2 = None
            U3 = None
            U4 = None
            
            # Add data into db:
            if FlowValue > 0: # only nonzero values are reported
                cur.execute(SQL,(DS_id,Elem_Pos,Prod_Pos,OrPr_Pos,OrRe_Pos,DesP_Pos,DesR_Pos,Year_Pos,None,None,None,None,None,FlowValue,\
                             UnitnID,UnitdnID,U1,U2,U3,U4,None,None,None,None))
        
# Close connection
cur.close()
conn.close()



# End



