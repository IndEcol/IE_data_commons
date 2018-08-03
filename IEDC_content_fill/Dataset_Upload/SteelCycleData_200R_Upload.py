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
    cur.execute("SELECT id,attribute2 FROM classification_items WHERE classification_id = %s ", C1id)
    C1Tuples = cur.fetchall()
    C1IDs    = [x[0] for x in C1Tuples]
    C1Labels = [int(x[1]) for x in C1Tuples]
    
    cur.execute("SELECT id,attribute3 FROM classification_items WHERE classification_id = %s ", C2id)
    C2Tuples = cur.fetchall()
    C2IDs    = [x[0] for x in C2Tuples]
    C2Labels = [x[1] for x in C2Tuples]
    
    cur.execute("SELECT id,attribute1 FROM classification_items WHERE classification_id = %s ", C3id)
    C3Tuples = cur.fetchall()
    C3IDs    = [x[0] for x in C3Tuples]
    C3Labels = [int(x[1]) for x in C3Tuples]

    cur.execute("SELECT id,attribute1 FROM classification_items WHERE classification_id = %s ", C4id)
    C4Tuples = cur.fetchall()
    C4IDs    = [x[0] for x in C4Tuples]
    C4Labels = [x[1] for x in C4Tuples]

    cur.execute("SELECT id,attribute4 FROM classification_items WHERE classification_id = %s ", C5id)
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

# PART 2: Flows

# Get dataset lists:
FlowFileList    = ['F_1_2_D','F_2_3_D','F_2_16_D','F_3_18_D','F_3_4_D','F_15_3_D','F_15_16_D','F_4_5_D','F_5_18_D','F_5_15_D','F_16_17_D','F_17_8_D',\
                 'F_5_6_D','F_6_7_D','F_7_8_D','F_8_9_D','F_9_10_D','F_9_15_D','F_10_11_D','F_11_12_D','F_12_13_D','F_13_19_D','F_13_14_D','F_14_15_D',\
                 'F_14_20_D','F_21_2_D','F_2_30_D','F_22_4_D','F_4_31_D','F_23_17_D','F_17_32_D','F_29_15_D','F_15_38_D','F_24_6_D','F_6_33_D','F_25_7_D',\
                 'F_7_34_D','F_26_10_D','F_10_35_D','F_27_11_D','F_11_36_D']
 
FlowDataSetList = ['1_F_steel_200R_F_1_2_pig_iron_production',
'1_F_steel_200R_F_2_3_pig_iron_to_crude_steel',
'1_F_steel_200R_F_2_16_pig_iron_to_casting',
'1_F_steel_200R_F_3_18_steel_slag_generation',
'1_F_steel_200R_F_3_4_crude_steel_production',
'1_F_steel_200R_F_15_3_scrap_use_by_crude_steel_production',
'1_F_steel_200R_F_15_16_scrap_to_casting',
'1_F_steel_200R_F_4_5_crude_steel_consumption',
'1_F_steel_200R_F_5_18_forming_losses',
'1_F_steel_200R_F_5_15_forming_scrap_generation',
'1_F_steel_200R_F_16_17_casting_output',
'1_F_steel_200R_F_17_8_castings_consumption',
'1_F_steel_200R_F_5_6_finished_steel_production',
'1_F_steel_200R_F_6_7_finished_steel_to_products',
'1_F_steel_200R_F_7_8_finished_steel_to_sector_split',
'1_F_steel_200R_F_8_9_steel_input_manufacturing',
'1_F_steel_200R_F_9_10_output_manufacturing',
'1_F_steel_200R_F_9_15_fabrication_scrap_generation',
'1_F_steel_200R_F_10_11_manufactured_goods',
'1_F_steel_200R_F_11_12_final_steel_consumption',
'1_F_steel_200R_F_12_13_EoL_products',
'1_F_steel_200R_F_13_19_obsolete_stock_formation',
'1_F_steel_200R_F_13_14_inflow_waste_mgt',
'1_F_steel_200R_F_14_15_EoL_steel_scrap',
'1_F_steel_200R_F_14_20_landfill_loss_accumulation',
'1_F_steel_200R_F_21_2_pig_iron_import',
'1_F_steel_200R_F_2_30_pig_iron_export',
'1_F_steel_200R_F_22_4_crude_steel_import',
'1_F_steel_200R_F_4_31_crude_steel_export',
'1_F_steel_200R_F_23_17_iron_steel_castings_import',
'1_F_steel_200R_F_17_32_iron_steel_castings_export',
'1_F_steel_200R_F_29_15_steel_scrap_import',
'1_F_steel_200R_F_15_38_steel_scrap_export',
'1_F_steel_200R_F_24_6_finished_steel_import',
'1_F_steel_200R_F_6_33_finished_steel_export',
'1_F_steel_200R_F_25_7_steel_products_import',
'1_F_steel_200R_F_7_34_steel_products_export',
'1_F_steel_200R_F_26_10_part_manufactured_goods_import',
'1_F_steel_200R_F_10_35_parts_manufactured_goods_export',
'1_F_steel_200R_F_27_11_manufactured_goods_import',
'1_F_steel_200R_F_11_36_manufactured_goods_export']

FlowMatlList    = ['pig iron',
'pig iron',
'pig iron',
'slag',
'crude steel',
'steel scrap',
'steel scrap',
'crude steel',
'slag',
'steel scrap',
'iron and steel castings',
'castings',
'finished steel',
'finished steel',
'finished steel',
'finished steel',
'manufactured goods',
'fabrication scrap',
'manufactured goods',
'manufactured goods',
'EoL products',
'obsolete products',
'EoL products',
'steel scrap',
'landfill loss',
'pig iron',
'pig iron',
'crude steel',
'crude steel',
'iron and steel castings',
'iron and steel castings',
'steel scrap',
'steel scrap',
'finished steel',
'finished steel',
'steel products',
'steel products',
'parts of manufactured goods',
'parts of manufactured goods',
'manufactured goods',
'manufactured goods']

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
    cur.execute("SELECT id,attribute3 FROM classification_items WHERE classification_id = %s ", C1id)
    C1Tuples = cur.fetchall()
    C1IDs    = [x[0] for x in C1Tuples]
    C1Labels = [x[1] for x in C1Tuples]
    
    cur.execute("SELECT id,attribute1 FROM classification_items WHERE classification_id = %s ", C2id)
    C2Tuples = cur.fetchall()
    C2IDs    = [x[0] for x in C2Tuples]
    C2Labels = [x[1] for x in C2Tuples]
    
    cur.execute("SELECT id,attribute2 FROM classification_items WHERE classification_id = %s ", C3id)
    C3Tuples = cur.fetchall()
    C3IDs    = [x[0] for x in C3Tuples]
    C3Labels = [int(x[1]) for x in C3Tuples]

    cur.execute("SELECT id,attribute4 FROM classification_items WHERE classification_id = %s ", C4id)
    C4Tuples = cur.fetchall()
    C4IDs    = [x[0] for x in C4Tuples]
    C4Labels = [int(x[1]) for x in C4Tuples]

    cur.execute("SELECT id,attribute2 FROM classification_items WHERE classification_id = %s ", C5id)
    C5Tuples = cur.fetchall()
    C5IDs    = [x[0] for x in C5Tuples]
    C5Labels = [int(x[1]) for x in C5Tuples]
    
    cur.execute("SELECT id,attribute4 FROM classification_items WHERE classification_id = %s ", C6id)
    C6Tuples = cur.fetchall()
    C6IDs    = [x[0] for x in C6Tuples]
    C6Labels = [int(x[1]) for x in C6Tuples]

    cur.execute("SELECT id,attribute1 FROM classification_items WHERE classification_id = %s ", C7id)
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
#            cur.execute(SQL,(DS_id,Elem_Pos,Prod_Pos,OrPr_Pos,OrRe_Pos,DesP_Pos,DesR_Pos,Year_Pos,None,None,None,None,None,FlowValue,\
#                         UnitnID,UnitdnID,U1,U2,U3,U4,None,None,None,None))
    
# Close connection
cur.close()
conn.close()



# End



