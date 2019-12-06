# -*- coding: utf-8 -*-
"""

@author: spauliuk
"""

import pymysql
import datetime
import numpy as np
from os import walk, path
import xlrd
from datetime import date, timedelta
import csv
import pandas as pd

import IEDC_PW

def UMISLabelToHierarchyCodes(label):
    """
    This function takes a UMIS process label, like "1.ENV.5;1.D.12;12"
    and extracts from it the reference material id, the aggregate 
    subsystem module id representing the material life cycle stage,
    the subsystem code, the process type, and the process code
    Matching to YSTAFDB/IEDC reference elements:
    Sp[0]: material ID, attribute3_oto in classification 38
    For this material the hierarchy table needs to be read.
    Col A of the hierarchy table
    Sp[1]: aggregate 
    subsystem module id representing the material life cycle stage
    one of ten: ENV, PEM, F&M, WMR, USE, PRM, AGP, SCO, IPR
    Col.B of the hierarchy table
    Sp[2]: the subsystem code
    Sp[3]: T for transformative, D for distributive processes
    Sp[4]: number indicating process code, is transformed to process number:
    for T labels 1,3,5,7,... the corresponding process numbers are 1,2,3,4, ...
    for D labels 2,4,6,8,... the corresponding process numbers are 1,2,3,4, ...
    """
    Sp = label.split('.')
    if Sp[3] == 'D':
        Sp[4] = int(Sp[4].split(';')[0]) / 2
    if Sp[3] == 'T':
        Sp[4] = (int(Sp[4].split(';')[0]) -1) / 2 + 1
    return Sp

WorkingFolder = 'C:\\Users\\spauliuk.AD\\FILES\\ARBEIT\\PROJECTS\\Database\\IE_DataCommons\\NEW\\'

ClassFolder   = 'C:\\Users\\spauliuk.AD\\FILES\\ARBEIT\\PROJECTS\\Database\\IE_DataCommons\\IEDC_software\\IEDC_Classification_fill\\manual_insert\\'

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

# 0) Connect: 

#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

# 1) load classifications/lookup tables
cur.execute("SELECT id, unitcode FROM units") # Units
UnTuples = cur.fetchall()
UIDs     = [x[0] for x in UnTuples]
UCodes   = [x[1] for x in UnTuples]

cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", 38) # Materials
C1Tuples = cur.fetchall()
C1IDs    = [x[0] for x in C1Tuples]
C1Labels = [x[1] for x in C1Tuples]
    
cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", 44) # Time
C2Tuples = cur.fetchall()
C2IDs    = [x[0] for x in C2Tuples]
C2Labels = [x[1] for x in C2Tuples]  
    
cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", 45) # Region
C3Tuples = cur.fetchall()
C3IDs    = [x[0] for x in C3Tuples]
C3Labels = [x[1] for x in C3Tuples]  

cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", 46) # Commodity
C4Tuples = cur.fetchall()
C4IDs    = [x[0] for x in C4Tuples]
C4Labels = [x[1] for x in C4Tuples]  

cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", 47) # Process
C5Tuples = cur.fetchall()
C5IDs    = [x[0] for x in C5Tuples]
C5Labels = [x[1] for x in C5Tuples]  

cur.execute("SELECT id,attribute1_oto FROM classification_items WHERE classification_id = %s ", 48) # Stock change layers
C6Tuples = cur.fetchall()
C6IDs    = [x[0] for x in C6Tuples]
C6Labels = [x[1] for x in C6Tuples]  

# 2) Load dataset info and other ancillary data
Hierarchies = {}
for MMat in C1Labels:
    try:
        Hierarchies[MMat] = pd.read_csv(WorkingFolder+'YSTAFDB\\YSTAFDB_hierarchy_tables\\hierarchy_' + MMat + '.csv', sep = ',', encoding = 'unicode_escape')
    except:
        None


ClassFile       = xlrd.open_workbook(WorkingFolder + 'ClassificationCheck.xlsx')
ClassDefsheet   = ClassFile.sheet_by_name('YSTAFDB')

Materials_Full  = []
Materials_Short = []
for m in range(1,65):
    Materials_Full.append(ClassDefsheet.cell_value(m,14))
    Materials_Short.append(ClassDefsheet.cell_value(m,15))

AggSubsystems_Full  = []
AggSubsystems_Short = [] 
for m in range(1,10):
    AggSubsystems_Full.append(ClassDefsheet.cell_value(m,21))
    AggSubsystems_Short.append(ClassDefsheet.cell_value(m,22))

# 3) Dataset list
DataSets_Stock   = ['2_S_Al_Aluminium_YSTAFDB','2_S_Cu_Copper_YSTAFDB','2_S_Fe_Iron_YSTAFDB','2_S_P_Phosphorus_YSTAFDB','2_S_Zn_Zinc_YSTAFDB','2_S_Cs_Caesium_YSTAFDB','2_S_Minor_Elements_YSTAFDB']
DataSets_StockC  = ['2_DS_Cs_Caesium_YSTAFDB','2_DS_All_Elements_YSTAFDB']
# get Dataset IDs from IEDC:
DSS_Ids = []
for dsname in DataSets_Stock:
    cur.execute("SELECT id FROM datasets WHERE dataset_name = %s ", dsname)
    InfoDS = cur.fetchall()
    DSS_Ids.append(InfoDS[0])

DSSC_Ids = []
for dsname in DataSets_StockC:
    cur.execute("SELECT id FROM datasets WHERE dataset_name = %s ", dsname)
    InfoDS = cur.fetchall()
    DSSC_Ids.append(InfoDS[0])


MatDSList_Stock  = ['Al','Cu','Fe','P','Zn','Cs'] 
MatDSList_StockC = ['Cs'] 


# 4) Load data file flows and parse line by line:
OriginProcessList = []
DestinProcessList = []
NoMatchListOr     = []
NoMatchListDest   = []
NoMatchIndicesOr  = []
NoMatchIndicesDes = []
MatchList         = [] # List with tags: 1 means that process labels could be parsed in hierarchy and can be uploaded, 0: not.
DSMatchList       = [] # List of Dataset matches for stocks/stock changes.
MatList           = []
NumVals           = []

FilePath = WorkingFolder + 'YSTAFDB\\YSTAFDB_core_tables\\processes.csv'
lines    = open(FilePath,'r').read().split('\n')
lc       = -1
for line in lines:
    lc += 1
    if lc > 0: # ignore header
        MatchList.append(1)
        if line != '':
            cols = line.split(',')
            Comment = '' # Python dict: comment = {'publication_id':'YSTAFDB_publication_id: 35','criticality_vsr_id':19,'note':'None'}
            # Check presence of material, no error if part of classification
            try:
                if cols[0].find('(') > 0:
                    Mat = cols[0][0:(cols[0].find('(')-1)]
                else:
                    Mat = cols[0]
            except:
                Mat = cols[0]
                
            MatList.append(Mat)                
            Mat_ID = C1IDs[C1Labels.index(Mat)]
            # Select hierarchy dataframe:
            Hierarchy_df = Hierarchies[Mat]
            
            Stock_Layer = cols[9]
            # Select dataset ID:
            if Stock_Layer == 'total': # Check whether stock or stock change, here: stock.
                try:
                    DSMatchList.append(DSS_Ids[MatDSList_Stock.index(Mat)])
                except:
                    DSMatchList.append(DSS_Ids[6])
            else:
                try:
                    DSMatchList.append(DSSC_Ids[MatDSList_StockC.index(Mat)])
                except:
                    DSMatchList.append(DSSC_Ids[1])
                # Check presence of layer, no error if part of classification
                Layer_ID  = C6IDs[C6Labels.index(Stock_Layer)]    
            
            # Check presence of time, no error if part of classification
            Time    = cols[1]
                
            Tim_ID  = C2IDs[C2Labels.index(Time)]    
    
            # Check presence of region, no error if part of classification
            Regio   = cols[2]
                
            Reg_ID  = C3IDs[C3Labels.index(Regio)]       
    
            # Check presence of unit, no error if part of unit table
            Unt = cols[11]
            if Unt != 'mass fraction (w/w)':
                Unit_ID = UIDs[UCodes.index(Unt)]       
                
            # add commment elements:
            Comment =  'comment = {\'system_boundary_process\':\'' + cols[3]
            Comment += '\'aggregate_subsystem_module_process\':\'' + cols[4] +'\','
            Comment += '\'subsystem_process\':\'' + cols[5] +'\','
            Comment += '\'process_name\':\'' + cols[8] +'\','
            Comment += '\'YSTADFDB_proces_label\':\'' + cols[6] +'\','            
            Comment += '\'Process_type\':\'' + cols[7] +'\','            
            
            # Parse process label:
            ProcessLabel = cols[6]
            # find origin process labels
            OriginProcesshierarchy = UMISLabelToHierarchyCodes(ProcessLabel)
            ProcessCode = str(OriginProcesshierarchy[4]).split('.')[0]
            OriSelect = Hierarchy_df.loc[Hierarchy_df['aggregate_subsystem_module_abbreviation'].isin([OriginProcesshierarchy[1]]) \
                                         & Hierarchy_df['subsystem_code'].isin([OriginProcesshierarchy[2]]) \
                                         & Hierarchy_df['process_number'].isin([ProcessCode])]
            if OriSelect.size == 6:
                OriginProcessList.append(AggSubsystems_Full[AggSubsystems_Short.index(OriSelect.iloc[0]['aggregate_subsystem_module_abbreviation'])] + '; ' + OriSelect.iloc[0]['subsystem_name'] + '; ' + OriSelect.iloc[0]['process_name'])
            else:
                ProcessCode = str(OriginProcesshierarchy[4]).split('.')[0] + "'"
                OriSelect = Hierarchy_df.loc[Hierarchy_df['aggregate_subsystem_module_abbreviation'].isin([OriginProcesshierarchy[1]]) \
                                         & Hierarchy_df['subsystem_code'].isin([OriginProcesshierarchy[2]]) \
                                         & Hierarchy_df['process_number'].isin([ProcessCode])]
                if OriSelect.size == 6:
                    OriginProcessList.append(AggSubsystems_Full[AggSubsystems_Short.index(OriSelect.iloc[0]['aggregate_subsystem_module_abbreviation'])] + '; ' + OriSelect.iloc[0]['subsystem_name'] + '; ' + OriSelect.iloc[0]['process_name'])
                else:    
                    NoMatchListOr.append(ProcessLabel)     
                    OriginProcessList.append(str(OriSelect.size))
                    NoMatchIndicesOr.append(lc)
                    MatchList[-1] = 0
    
        # Check presence of process, no error if part of classification
        if MatchList[-1] == 1:
            Proc    = OriginProcessList[-1]
            Proc_ID = C5IDs[C5Labels.index(Proc)]  
    
        # Value:
        try:
            NumVal  = np.float(cols[10])
        except:
            NumVal  = None
        try:
            ConcVal = np.float(cols[12])
        except:
            ConcVal = None        
        if NumVal is not None and ConcVal is not None:
            NumVal  = NumVal * ConcVal # calculate mass fraction indicating mass of material in commodity.
            
        NumVals.append(NumVal)
            
        if cols[13] == 'mass fraction (w/w)':            
            Comment += '\'mass fraction of material in commodity\':\'' + cols[12] +'\','
            
        # Check if residual stock info is present:
        if cols[18] != '\\':
            Comment += '\'residual_quantity\':\'' + cols[18] +'\','
            Comment += '\'residual_quantity_unit\':\'' + cols[19] +'\','
            Comment += '\'residual_concentration\':\'' + cols[20] +'\','
            Comment += '\'residual_concentration_unit\':\'' + cols[21] +'\','
        
        Comment += '\'reliability\':\'' + cols[17] +'\','
        Comment += '\'method\':\'' + cols[22] +'\','
        Comment += '\'YSTAFDB_publication_id\':\'' + cols[23] +'\','
        Comment += '\'notes\':\'' + cols[24] +'\','
        Comment += '\'YSTAFDB_process_id\':\'' + cols[25] +'\','
        # comment finish
        Comment += '}'   
                
        # uncertainty    
        if cols[16] == 'plus minus':
            U1 = 4
            N2 = None
            if cols[15] == '%':
                U3 = np.float(cols[10]) * (100 - np.float(cols[14])) / 100
                U4 = np.float(cols[10]) * (100 + np.float(cols[14])) / 100
            if cols[15] == 'g':
                # FIX: + Stock Pb (Lead)	1991	Austria; Vienna	inside	use (USE)	aggregate use	35.USE.3.T.1;1  has unit Tg 
                # but uncertainty unit g. The latter is changed to / assumed to be Tg by the script (it is the only g unit for uncertainty). 
                U3 = np.float(cols[10]) - np.float(cols[14])
                U4 = np.float(cols[10]) + np.float(cols[14])
        else:
            U1 = None
            U2 = None
            U3 = None
            U4 = None
        
       
#        # Add data into db:
#        if Unt != 'mass fraction (w/w)': # Only if the unit is not mass fraction, these 530 entries are discarded.
#            if Stock_Layer == 'total': # Check whether stock or stock change, here: stock.
#               cur.execute(SQL,(DSMatchList[-1],Mat_ID,Tim_ID,Reg_ID,Proc_ID,None,None,None,None,None,None,None,None,NumVal,\
#                        Unit_ID,1,U1,U2,U3,U4,Comment,None,None,None))   
#    
#            else: # here: stock change
#               cur.execute(SQL,(DSMatchList[-1],Mat_ID,Tim_ID,Reg_ID,Proc_ID,Layer_ID,None,None,None,None,None,None,None,NumVal,\
#                         Unit_ID,1,U1,U2,U3,U4,Comment,None,None,None))     
                
        if lc % 20 == 0:
            print(lc)



# Close connection
cur.close()
conn.close()

#
#
#
# The end.
#
#
#
#            