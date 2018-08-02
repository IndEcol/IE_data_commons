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
cur.execute("SELECT id FROM datasets WHERE dataset_name = '2_P_HistoricPopulation_SteelCycle' ")
DS_id = cur.fetchall()[0][0]
cur.execute("SELECT aspect_1_classification FROM datasets WHERE dataset_name = '2_P_HistoricPopulation_SteelCycle' ")
C1id = cur.fetchall()[0][0]
cur.execute("SELECT aspect_2_classification FROM datasets WHERE dataset_name = '2_P_HistoricPopulation_SteelCycle' ")
C2id = cur.fetchall()[0][0]

# 2 Classifications are used, get their items:
cur.execute("SELECT id,attribute4 FROM classification_items WHERE classification_id = %s ", C1id)
C1Tuples = cur.fetchall()
C1IDs    = [x[0] for x in C1Tuples]
C1Labels = [int(x[1]) for x in C1Tuples]

cur.execute("SELECT id,attribute1 FROM classification_items WHERE classification_id = %s ", C2id)
C2Tuples = cur.fetchall()
C2IDs    = [x[0] for x in C2Tuples]
C2Labels = [int(x[1]) for x in C2Tuples]


# Open csv file with data
FilePath = 'C:\\Users\\spauliuk\\FILES\\ARBEIT\\PROJECTS\\Database\\IE_DataCommons\\DATA\\Data_Custom_Insertion\\2_P_HistoricPopulation_SteelCycle\\2_P_HistoricPopulation_SteelCycle.csv'
lines = open(FilePath,'r').read().split('\n')
for line in lines:
    if line != '':
        cols = line.split(';')
        CountryID = int(cols[3])
        YearID    = int(cols[4])
        PopValue  = np.float(cols[8])
        
        Country_Pos = C1IDs[C1Labels.index(CountryID)]
        Time_Pos    = C2IDs[C2Labels.index(YearID)]
        
        # Add data into db:
    cur.execute(SQL,(DS_id,Country_Pos,Time_Pos,None,None,None,None,None,None,None,None,None,None,PopValue,\
                     32,1,1,0,0,0,None,None,None,None))

    
    
# Close connection
cur.close()
conn.close()



# End