# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:17:49 2023

@author: spauliuk

SQL commands and Python code for 3 aspect search in the 2026 revision
"""

import pymysql
import IEDC_PW
import numpy as np

conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

'''
################################################################################################
# Section: fetch datatypes: SQL command to fetch all data types
################################################################################################
''' 

type_list = []
cur.execute("SELECT * FROM types")
for row in cur:
    # print(row) 
    # print(row[0])
    type_list.append(row[1] + ' (' + str(row[3]) + '_' + row[4] + ')')
    
# pick one to simulate user choice:
tX = 5 # 3_MC    

# check how many datasets of this type there are, tX+1 because of list index start 0 (Python) to 1 (iedc)
cur.execute("SELECT COUNT(*) FROM datasets WHERE data_type = %s", tX+1)
for row in cur:
    NoD = row[0] # number of matching datasets
    print(NoD)    

print ('    ')
#    Text display: "Total number of datasets available for chosen data type:" print(row[0])    #
    
# Fetch all aspects and classifications used for these datasets:
ids = [] # list of lists
all_aspects = [] # list of lists of aspects by dataset
all_classfs = [] # list of lists of resp. classification id for each aspect
cur.execute("SELECT id FROM datasets WHERE data_type = %s", tX+1)
for row in cur:
    ids.append(row[0])        
    
for pos in np.arange(0,len(ids)):
    all_aspects.append([])    
    all_classfs.append([])   
    cur.execute("SELECT aspect_1, aspect_2, aspect_3, aspect_4, aspect_5, aspect_6, aspect_7, aspect_8, aspect_9, aspect_10, aspect_11, aspect_12, aspect_1_classification, aspect_2_classification, aspect_3_classification, aspect_4_classification, aspect_5_classification, aspect_6_classification, aspect_7_classification, aspect_8_classification, aspect_9_classification, aspect_10_classification, aspect_11_classification, aspect_12_classification FROM datasets WHERE id = %s", ids[pos])
    for row in cur:
        for m in range(0,12):
            all_aspects[pos].append(row[m])    
        for m in range(12,24):
            all_classfs[pos].append(row[m])   
all_aspects_flat = [element for innerList in all_aspects for element in innerList]            
all_aspects_u = list(set(all_aspects_flat)) # remove duplicates, unique list        
all_aspects_u = [i for i in all_aspects_u if isinstance(i, int)] # remove noneType

aspects = []
for m in all_aspects_u:
    cur.execute("SELECT aspect FROM aspects WHERE id = %s", m)
    for row in cur:
        aspects.append(row[0])
        
'''
################################################################################################
# Section: display labels after choosing first aspect
################################################################################################
'''         
# First, display the above aspects (list) as dropdown, let the user pick one, which we call aX and we simulate here as
aX = 11 # commodity

#For this aspect, all datasets with that aspect are identified:
DS_match_aspect1_select     = [] # list dataset ids that have this aspect
DS_match_aspect1_select_pos = [] # list the aspect number for the matching dataset+aspect
for pos in np.arange(0,len(ids)):
    if aX in all_aspects[pos]:
        DS_match_aspect1_select.append(ids[pos])
        DS_match_aspect1_select_pos.append(all_aspects[pos].index(aX)+1)     # convert from start at 0 to 1.
        
# Extract labels and display:
ClItemIDs_aspect1_select   = []    
Labels_aspect1_select      = []
Labels_aspect1_select_flat = []
Labels_aspect1_select_u    = []

for pos in np.arange(0,len(DS_match_aspect1_select)):
    Labels_aspect1_select.append([])  
    ClItemIDs_aspect1_select.append([])
    aspect_string = 'aspect' + str(DS_match_aspect1_select_pos[pos])    
    #cur.execute("SELECT " + aspect_string + " FROM data WHERE dataset_id = %s", (DS_match_aspect1_select[pos]))
    #cur.execute("SELECT attribute1_oto FROM classification_items JOIN data ON classification_items.id = data." + aspect_string + " WHERE dataset_id = %s", (DS_match_aspect1_select[pos])) 
    cur.execute("SELECT ci.attribute1_oto, d." + aspect_string + " FROM data d INNER JOIN classification_items ci ON d." + aspect_string + " = ci.id WHERE d.dataset_id = %s", (DS_match_aspect1_select[pos])) 
    for row in cur:
        Labels_aspect1_select[pos].append(row[0])     # get the label into the right container for the user to select
        ClItemIDs_aspect1_select[pos].append(row[1])  # get the classification ID into the right container to find the dataset later          

Labels_aspect1_select_flat = [element for innerList in Labels_aspect1_select for element in innerList]    # flatten list        
Labels_aspect1_select_u = sorted(list(set(Labels_aspect1_select_flat))) # remove duplicates, unique list        

# Display this list (Labels_aspect1_select_u) in alphabetical order (words first, then numbers) and let the user select the fist label: L1.

'''
################################################################################################
# Section: After choosing the first label
################################################################################################
''' 
L1 = 'single-family house'
L1 = 'passenger vehicles'

# Find all datasets that contain this label
L1_matches_id =  [] # dataset ids
L1_matches_pos = [] # position in master list
for pos in np.arange(0,len(DS_match_aspect1_select)):
    if L1 in Labels_aspect1_select[pos]:
        L1_matches_pos.append(pos)
        L1_matches_id.append(DS_match_aspect1_select[pos])

# 1. For the list L1_matches, which contains at least 1 element, display the usual list of datasets contained in L1_matches_id, 
# plus the download and filter buttons. See the author and DOI search page, for example. The user can go with these datasets or continue with selecting another aspect if they wish:

# 2. Determine what other aspects are there for this dataset and prepare the second aspect search:
all_aspects2 = [all_aspects[i] for i in L1_matches_pos]
all_aspects2_flat = [element for innerList in all_aspects2 for element in innerList]            
all_aspects2_u = list(set(all_aspects2_flat)) # remove duplicates, unique list        
all_aspects2_u = [i for i in all_aspects2_u if isinstance(i, int)] # remove noneType
all_aspects2_u.remove(aX) # remove aspect that is already chosen

aspects2_labels = []
aspects2_ids    = []
for m in all_aspects2_u:
    cur.execute("SELECT id, aspect FROM aspects WHERE id = %s", m)
    for row in cur:
        aspects2_ids.append(row[0])
        aspects2_labels.append(row[1])
        
'''
################################################################################################
# Section: Choosing a second aspect
################################################################################################
'''         

# First, display the above aspects (list) as dropdown, let the user pick one, which we call aY and we simulate here as
aY = 5 # region
aY = 2 # age-cohort

# Now, we can repeat the above procedure, code from line 78 adapted:
#For this aspect, all datasets with that aspect are identified:
DS_match_aspect2_select     = [] # list dataset ids that have this aspect
DS_match_aspect2_select_pos = [] # list the aspect number for the matching dataset+aspect
for pos in np.arange(0,len(L1_matches_id)):
    if aY in all_aspects[L1_matches_pos[pos]]:
        DS_match_aspect2_select.append(ids[L1_matches_pos[pos]])
        DS_match_aspect2_select_pos.append(all_aspects[L1_matches_pos[pos]].index(aY)+1)     # convert from start at 0 to 1.   
        
# Extract labels and display:
ClItemIDs_aspect2_select   = []    
Labels_aspect2_select      = []
Labels_aspect2_select_flat = []
Labels_aspect2_select_u    = []

for pos in np.arange(0,len(DS_match_aspect2_select)):
    Labels_aspect2_select.append([])  
    ClItemIDs_aspect2_select.append([])
    aspect_string = 'aspect' + str(DS_match_aspect2_select_pos[pos])    
    cur.execute("SELECT ci.attribute1_oto, d." + aspect_string + " FROM data d INNER JOIN classification_items ci ON d." + aspect_string + " = ci.id WHERE d.dataset_id = %s", (DS_match_aspect2_select[pos])) 
    for row in cur:
        Labels_aspect2_select[pos].append(row[0])     # get the label into the right container for the user to select
        ClItemIDs_aspect2_select[pos].append(row[1])  # get the classification ID into the right container to find the dataset later          

Labels_aspect2_select_flat = [element for innerList in Labels_aspect2_select for element in innerList]            
Labels_aspect2_select_u = sorted(list(set(Labels_aspect2_select_flat))) # remove duplicates, unique list        

'''
################################################################################################
# Section: After choosing the second label
################################################################################################
''' 
L2 = 'Austria'
L2 = '2011 - 2020'
# Find all datasets that contain this label
L2_matches_id =  [] # dataset ids
L2_matches_pos = [] # position in master list
for pos in np.arange(0,len(DS_match_aspect2_select)):
    if L2 in Labels_aspect2_select[pos]:
        L2_matches_pos.append(ids.index(DS_match_aspect2_select[pos]))
        L2_matches_id.append(DS_match_aspect2_select[pos])

# 1. For the list L2_matches, which contains at least 1 element, display the usual list of datasets contained in L1_matches_id, 
# plus the download and filter buttons. See the author and DOI search page, for example. The user can go with these datasets or continue with selecting another aspect if they wish:

# 2. Determine what other aspects are there for this dataset and prepare the second aspect search:
all_aspects3 = [all_aspects[i] for i in L2_matches_pos]
all_aspects3_flat = [element for innerList in all_aspects3 for element in innerList]            
all_aspects3_u = list(set(all_aspects3_flat)) # remove duplicates, unique list        
all_aspects3_u = [i for i in all_aspects3_u if isinstance(i, int)] # remove noneType
all_aspects3_u.remove(aX) # remove aspect that is already chosen
all_aspects3_u.remove(aY) # remove aspect that is already chosen

aspects3_labels = []
aspects3_ids    = []
for m in all_aspects3_u:
    cur.execute("SELECT id, aspect FROM aspects WHERE id = %s", m)
    for row in cur:
        aspects3_ids.append(row[0])
        aspects3_labels.append(row[1])
        
'''
################################################################################################
# Section: Choosing a third aspect
################################################################################################
'''         

# First, display the above aspects (list) as dropdown, let the user pick one, which we call aY and we simulate here as
aZ = 12 # engineering_material

# Now, we can repeat the above procedure, code from line 78 adapted:
#For this aspect, all datasets with that aspect are identified:
DS_match_aspect3_select     = [] # list dataset ids that have this aspect
DS_match_aspect3_select_pos = [] # list the aspect number for the matching dataset+aspect
for pos in np.arange(0,len(L2_matches_id)):
    if aZ in all_aspects[L2_matches_pos[pos]]:
        DS_match_aspect3_select.append(ids[L2_matches_pos[pos]])
        DS_match_aspect3_select_pos.append(all_aspects[L2_matches_pos[pos]].index(aZ)+1)     # convert from start at 0 to 1.   
        
# Extract labels and display:
ClItemIDs_aspect3_select   = []    
Labels_aspect3_select      = []
Labels_aspect3_select_flat = []
Labels_aspect3_select_u    = []

for pos in np.arange(0,len(DS_match_aspect3_select)):
    Labels_aspect3_select.append([])  
    ClItemIDs_aspect3_select.append([])
    aspect_string = 'aspect' + str(DS_match_aspect3_select_pos[pos])    
    cur.execute("SELECT ci.attribute1_oto, d." + aspect_string + " FROM data d INNER JOIN classification_items ci ON d." + aspect_string + " = ci.id WHERE d.dataset_id = %s", (DS_match_aspect3_select[pos])) 
    for row in cur:
        Labels_aspect3_select[pos].append(row[0])     # get the label into the right container for the user to select
        ClItemIDs_aspect3_select[pos].append(row[1])  # get the classification ID into the right container to find the dataset later          
   
Labels_aspect3_select_flat = [element for innerList in Labels_aspect3_select for element in innerList]            
Labels_aspect3_select_u = sorted(list(set(Labels_aspect3_select_flat))) # remove duplicates, unique list          
 
'''
################################################################################################
# Section: After choosing the third label
################################################################################################
''' 
L3 = 'concrete'
L3 = 'plastics'
# Find all datasets that contain this label
L3_matches_id =  [] # dataset ids
L3_matches_pos = [] # position in master list
for pos in np.arange(0,len(DS_match_aspect3_select)):
    if L3 in Labels_aspect3_select[pos]:
        L3_matches_pos.append(ids.index(DS_match_aspect3_select[pos]))
        L3_matches_id.append(DS_match_aspect3_select[pos])
              

# 1. For the list L3_matches, which contains at least 1 element, display the usual list of datasets, 
# plus the download and filter buttons. See the author and DOI search page, for example. 
# The user now has a list of datasets filtered by three aspects and labels, which concludes this search function.

# Also, please implement a hierarchical reset: E.g. when the user makes a new choice in step 2, the results from all subsequent steps are deleted.


#
#