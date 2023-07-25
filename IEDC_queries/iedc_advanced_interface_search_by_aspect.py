# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:17:49 2023

@author: spauliuk

SQL commands and Python code for advanced iedc search, with graphical interface description
"""

import pymysql
import datetime
import IEDC_PW
import numpy as np

conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

# SQL command to fetch all data types
type_list = []
cur.execute("SELECT * FROM types")
for row in cur:
    print(row) 
    print(row[0])
    type_list.append(row[1] + ' (' + str(row[3]) + '_' + row[4] + ')')
    
    
'''
################################################################################################
#    Text display:
<h2 or so> Search for available data within all datasets of a given type

<p> Data in the iedc are organized into pre-defined (data types) [https://www.database.industrialecology.uni-freiburg.de/datatypes.aspx / open in new tab], such as data for flows, stocks, material composition, or unit process inventories. 
<p> In this interface, you first select a data type, upon which all the different aspects (time, region, material, etc.) used to describe the different datasets for this data type are shown.
After selecting a specific aspect, the different classification items (specific regions, materials, etc.)
for which data are available are listed.
After selecting one ore more classification items, all available datasets that contain data for this
classification item in the given aspect are shown and can be previewed.
Download is then possible via the main interface.
################################################################################################

#########################################################
#    Dropdown list with type_list, select 1 item (p)    #
#########################################################

'''    
    
# simulate user action: select a datatype, which leads to a value for p (simply the position in the list.
# Here, we test for p = 5: material composition
p = 5 

# check how many datasets of this type there are, p+1 because of list index start 0 (Python) to 1 (iedc)
cur.execute("SELECT COUNT(*) FROM datasets WHERE data_type = %s", p+1)
for row in cur:
    print(row[0])    

'''
################################################################################################
#    Text display: "Total number of datasets available for chosen data type:" print(row[0])    #
################################################################################################

'''   
    
# Fetch all aspects used for these datasets:
ids = []
cur.execute("SELECT id FROM datasets WHERE data_type = %s", p+1)
for row in cur:
    ids.append(row[0])        
    
all_aspects = []
all_classfs = []
for id in ids:
    cur.execute("SELECT aspect_1, aspect_2, aspect_3, aspect_4, aspect_5, aspect_6, aspect_7, aspect_8, aspect_9, aspect_10, aspect_11, aspect_12, aspect_1_classification, aspect_2_classification, aspect_3_classification, aspect_4_classification, aspect_5_classification, aspect_6_classification, aspect_7_classification, aspect_8_classification, aspect_9_classification, aspect_10_classification, aspect_11_classification, aspect_12_classification FROM datasets WHERE id = %s", id)
    for row in cur:
        for m in range(0,12):
            all_aspects.append(row[m])    
        for m in range(12,24):
            all_classfs.append(row[m])    
all_aspects_u = list(set(all_aspects)) # remove duplicates, unique list        
all_aspects_u = [i for i in all_aspects_u if isinstance(i, int)] # remove noneType

aspects = []
for m in all_aspects_u:
    cur.execute("SELECT aspect FROM aspects WHERE id = %s", m)
    for row in cur:
        aspects.append(row[0])

# Set Default values for aspects to search for (if any):
a1 = None
a2 = None
a3 = None

'''
##########################################################################################
#    Populate three dropdown lists with aspects, select 1 item from each (a1, a2, a3)    #
##########################################################################################

################################################
#    Button "Retrieve classification items"    #
################################################

For 'press search to have an effect, at least one of the dropdown lists must have been selected: a1 = [value], a2 and a3 can be set or can be none'
'''

# here: simulate user action:
a1 = 2 # region
a2 = 0 # age-cohort

# Now, compile all possible classification items for the selected aspects:
    
if a1 is not None:
    a1 = all_aspects_u[a1] # map from position to aspect id
    a1_classf = []
    a1_classi = []
    for m in range(0,len(all_aspects)):
        if all_aspects[m] == a1:
            a1_classf.append(all_classfs[m])
    a1_classf = list(set(a1_classf))
    for m in a1_classf:
        cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_id = %s", m)
        for row in cur:
            a1_classi.append(row[0])
    
if a2 is not None:
    a2 = all_aspects_u[a2] # map from position to aspect id
    a2_classf = []
    a2_classi = []    
    for m in range(0,len(all_aspects)):
        if all_aspects[m] == a2:
            a2_classf.append(all_classfs[m])
    a2_classf = list(set(a2_classf))
    for m in a2_classf:
        cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_id = %s", m)
        for row in cur:
            a2_classi.append(row[0])
            
if a3 is not None:
    a3 = all_aspects_u[a3] # map from position to aspect id
    a3_classf = []
    a3_classi = []    
    for m in range(0,len(all_aspects)):
        if all_aspects[m] == a3:
            a3_classf.append(all_classfs[m])
    a3_classf = list(set(a3_classf))    
    for m in a3_classf:
        cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_id = %s", m)
        for row in cur:
            a3_classi.append(row[0])

'''
#################################################################################################################################################################
#    Populate up to three dropdown lists with a1_classi/a2_.../a3_... (if exists!), select SEVERAL items from each, which are returned as lists (b1, b2, b3)    #
#################################################################################################################################################################

###################################
#    Button "Find datasets"       #
###################################
'''

# here: simulate user action:
b1 = [59] # region: China
b2 = np.arange(290,321,1).tolist()  # age-cohort: 1990 to 2020

# Loop over all datasets to find relevant aspect and items covered:
matchlist_id = [] # List with dataset ids that contain a match for the search
matchlist_na = [] # dataset names
for m in ids:
    all_a = []
    cur.execute("SELECT aspect_1, aspect_2, aspect_3, aspect_4, aspect_5, aspect_6, aspect_7, aspect_8, aspect_9, aspect_10, aspect_11, aspect_12, aspect_1_classification, aspect_2_classification, aspect_3_classification, aspect_4_classification, aspect_5_classification, aspect_6_classification, aspect_7_classification, aspect_8_classification, aspect_9_classification, aspect_10_classification, aspect_11_classification, aspect_12_classification FROM datasets WHERE id = %s", m)
    for row in cur:
        for n in range(0,12):
            all_a.append(row[n])    
    if a1 is not None:
        a1_loc = all_a.index(a1)
    if a2 is not None:
        a2_loc = all_a.index(a2)
    if a3 is not None:
        a3_loc = all_a.index(a3)       
        
    cur.execute("SELECT COUNT(*) FROM data WHERE dataset_id = %s AND aspect" + str(a1_loc+1) + " = %s", (m, b1[0]))
    print(a1_loc)
    for row in cur:
        print(row[0])          

'''
#################################################################################################################################################################
#    For each entry in the match list: Create a display/text with the dateset id and name    #
#################################################################################################################################################################

#################################################################################################################################
#    Button "Show": Show dataset sample/previous as on main search page, just with specific selected classification items       #
#################################################################################################################################
'''    

#
# The end.
#

