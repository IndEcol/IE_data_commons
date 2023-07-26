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
    # print(row) 
    # print(row[0])
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
    
# simulate user action: select a datatype, which leads to a value for p (simply the position in the list).
# Here, we test for p = 5: material composition
p = 5 # Replace by actual user input later

# check how many datasets of this type there are, p+1 because of list index start 0 (Python) to 1 (iedc)
cur.execute("SELECT COUNT(*) FROM datasets WHERE data_type = %s", p+1)
for row in cur:
    print(row[0])    

print ('    ')

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
a1 = 2 # region, replace by actual user input later
a2 = 0 # age-cohort, replace by actual user input later

# Now, compile all possible classification items for the selected aspects:
    
if a1 is not None:
    a1 = all_aspects_u[a1] # map from position to aspect id
    a1_classf = [] # classification id
    a1_classi = [] # classification items
    a1_classd = [] # classification items id
    for m in range(0,len(all_aspects)):
        if all_aspects[m] == a1:
            a1_classf.append(all_classfs[m])
    a1_classf = list(set(a1_classf))
    for m in a1_classf:
        cur.execute("SELECT id, attribute1_oto FROM classification_items WHERE classification_id = %s", m)
        for row in cur:
            a1_classi.append(row[1])
            a1_classd.append(row[0])
    
if a2 is not None:
    a2 = all_aspects_u[a2] # map from position to aspect id
    a2_classf = []
    a2_classi = []    
    a2_classd = []
    for m in range(0,len(all_aspects)):
        if all_aspects[m] == a2:
            a2_classf.append(all_classfs[m])
    a2_classf = list(set(a2_classf))
    for m in a2_classf:
        cur.execute("SELECT id, attribute1_oto FROM classification_items WHERE classification_id = %s", m)
        for row in cur:
            a2_classi.append(row[1])
            a2_classd.append(row[0])
            
if a3 is not None:
    a3 = all_aspects_u[a3] # map from position to aspect id
    a3_classf = []
    a3_classi = []    
    a3_classd = []    
    for m in range(0,len(all_aspects)):
        if all_aspects[m] == a3:
            a3_classf.append(all_classfs[m])
    a3_classf = list(set(a3_classf))    
    for m in a3_classf:
        cur.execute("SELECT id, attribute1_oto FROM classification_items WHERE classification_id = %s", m)
        for row in cur:
            a3_classi.append(row[1])
            a3_classd.append(row[0])

'''
#################################################################################################################################################################
#    Populate up to three dropdown lists with a1_classi/a2_.../a3_... (if exists!), select SEVERAL items from each, which are returned as lists (b1, b2, b3)    #
#################################################################################################################################################################

###################################
#    Button "Find datasets"       #
###################################
'''

# here: simulate user action, replace by actual user input later
b1 = [59] # region: China
b2 = np.arange(290,321,1).tolist()  # age-cohorts: 1990 to 2020
b3 = [] # nothing selected

# Translate list positions into classficiation item ids
b1id = [a1_classd[i] for i in b1]
b2id = [a2_classd[i] for i in b2]
b3id = [a3_classd[i] for i in b3]

# Loop over all datasets to find relevant aspect and items covered:
matchlist_id = [] # List with dataset ids that contain a match for the search
matchlist_na = [] # dataset names
for m in ids:
    all_a = []
    cur.execute("SELECT aspect_1, aspect_2, aspect_3, aspect_4, aspect_5, aspect_6, aspect_7, aspect_8, aspect_9, aspect_10, aspect_11, aspect_12, aspect_1_classification, aspect_2_classification, aspect_3_classification, aspect_4_classification, aspect_5_classification, aspect_6_classification, aspect_7_classification, aspect_8_classification, aspect_9_classification, aspect_10_classification, aspect_11_classification, aspect_12_classification, dataset_name FROM datasets WHERE id = %s", m)
    for row in cur:
        for n in range(0,12):
            all_a.append(row[n])    
    all_a = [i for i in all_a if i is not None]            
    dsn = row[24] # dataset name
    # Build SQL query
    SQL = 'SELECT COUNT(*) FROM data WHERE dataset_id = %s'
    QP  = (m,)
    try:
        a1_loc = all_a.index(a1)
        SQL += ' AND aspect' + str(a1_loc+1) + ' IN %s'
        QP  +=  (tuple(b1id),)
    except:
        a1_loc = None
    try:
        a2_loc = all_a.index(a2)
        SQL += ' AND aspect' + str(a2_loc+1) + ' IN %s'
        QP  +=  (tuple(b2id),)
    except:
        a2_loc = None
    try:
        a3_loc = all_a.index(a3)
        SQL += ' AND aspect' + str(a3_loc+1) + ' IN %s'
        QP  +=  (tuple(b3id),)
    except:
        a3_loc = None
        
    if len(QP) > 1: # if there is at least one matching aspct in the dataset
        cur.execute(SQL,QP)
        for row in cur:
            # print(row[0])          
            if row[0] > 0: # We have a match!
                matchlist_id.append(m)
                matchlist_na.append(dsn)

for ii in range(0,len(matchlist_id)):
    print(matchlist_id[ii], matchlist_na[ii])       
print ('    ')

'''
#################################################################################################################################################################
#    For each entry in the match list: Create a display/text with the dateset id and name    #
#################################################################################################################################################################

#################################################################################################################################
#    Next to each dataset id/name displayed: Create a button "Show": Show dataset sample/previous as on main search page, 
#    just with specific selected classification items as above and example below             #
#################################################################################################################################
'''    

m = 213 #(example)

all_a = []
cur.execute("SELECT aspect_1, aspect_2, aspect_3, aspect_4, aspect_5, aspect_6, aspect_7, aspect_8, aspect_9, aspect_10, aspect_11, aspect_12, aspect_1_classification, aspect_2_classification, aspect_3_classification, aspect_4_classification, aspect_5_classification, aspect_6_classification, aspect_7_classification, aspect_8_classification, aspect_9_classification, aspect_10_classification, aspect_11_classification, aspect_12_classification, dataset_name FROM datasets WHERE id = %s", m)
for row in cur:
    for n in range(0,12):
        all_a.append(row[n])    
all_a = [i for i in all_a if i is not None]            
dsn = row[24] # dataset name
# Build SQL query
SQL = 'SELECT value, unit_nominator FROM data WHERE dataset_id = %s'
QP  = (m,)
try:
    a1_loc = all_a.index(a1)
    SQL += ' AND aspect' + str(a1_loc+1) + ' IN %s'
    QP  +=  (tuple(b1id),)
except:
    a1_loc = None
try:
    a2_loc = all_a.index(a2)
    SQL += ' AND aspect' + str(a2_loc+1) + ' IN %s'
    QP  +=  (tuple(b2id),)
except:
    a2_loc = None
try:
    a3_loc = all_a.index(a3)
    SQL += ' AND aspect' + str(a3_loc+1) + ' IN %s'
    QP  +=  (tuple(b3id),)
except:
    a3_loc = None
    
if len(QP) > 1: # if there is at least one matching aspct in the dataset
    cur.execute(SQL,QP)
    for row in cur:
        print(row[0], row[1])  # still need to resolve for the different IDs with a join statement, see the query for the sample results on the main iedc page.

#
# The end.
#

# Other code: Only one item for each aspect:
'''
cur.execute('SELECT COUNT(*) FROM data WHERE dataset_id = %s AND aspect4 = %s AND aspect3 = %s',(213, 5917, 6677))


cur.execute('SELECT COUNT(*) FROM data WHERE dataset_id = %s AND aspect4 = %s AND aspect3 IN %s',(213, 5917, (6677,6678,6679,6680)))


for m in ids:
    all_a = []
    cur.execute("SELECT aspect_1, aspect_2, aspect_3, aspect_4, aspect_5, aspect_6, aspect_7, aspect_8, aspect_9, aspect_10, aspect_11, aspect_12, aspect_1_classification, aspect_2_classification, aspect_3_classification, aspect_4_classification, aspect_5_classification, aspect_6_classification, aspect_7_classification, aspect_8_classification, aspect_9_classification, aspect_10_classification, aspect_11_classification, aspect_12_classification, dataset_name FROM datasets WHERE id = %s", m)
    for row in cur:
        for n in range(0,12):
            all_a.append(row[n])    
    all_a = [i for i in all_a if i is not None]            
    dsn = row[24] # dataset name
    # Build SQL query
    SQL = 'SELECT COUNT(*) FROM data WHERE dataset_id = %s'
    QP  = (m,)
    try:
        a1_loc = all_a.index(a1)
        SQL += ' AND aspect' + str(a1_loc+1) + ' = %s'
        QP  +=  (b1id[0],)
    except:
        a1_loc = None
    try:
        a2_loc = all_a.index(a2)
        SQL += ' AND aspect' + str(a2_loc+1) + ' = %s'
        QP  +=  (b2id[0],)
    except:
        a2_loc = None
    try:
        a3_loc = all_a.index(a3)
        SQL += ' AND aspect' + str(a3_loc+1) + ' = %s'
        QP  +=  (b3id[0],)
    except:
        a3_loc = None
'''        

