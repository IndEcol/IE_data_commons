# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:17:49 2023

@author: spauliuk

SQL commands and Python code for iedc search for given datatypes by product/commodity, material and process
"""

import pymysql
import datetime
import IEDC_PW
import openpyxl
import numpy as np

conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

'''
For this search, we offer several entire main classifications to pick a label from:
E.g., 4 (materials), 7 (products), 2 (regions).
--> offer dropdown with these classifications, user needs to pick one:
+ Select one from a list of ca. 20 classifications (materials, products, processes, regions, ...): 
    1-2-3-4-5-6-7-8-10-11-12-13-28-72-73-79-85-86-89-90-92-94. 
o	Display in dropdown as name | description |id
--> Then, populate another dropdown with all entries from the chosen classification
(SELECT attribute1_oto, attribute2_oto FROM classification_items WHERE id = [this_id])
For the example below, let's assume the user has picked the label 'copper' from class. 4'
'''

'''
Text for homepage:
<H3> IEDC search for data by single label </H3>

This search function finds all datasets that contain information on a given material, product, process, or region. <br>
Below, you find a list of the IEDC's most commonly used classifications. You can search and select a single label from any of these classifications,
and all datasets that contain information about this label will be displayed for further inspection.
'''

#this_cid = 4
#this_lab = 'copper'
#this_lab = 'glass'
this_cid = 7
#this_lab = 'battery of electric vehicles'
#this_lab = 'bicycle'
this_lab = 'wind turbines, offshore'

# prepare: find classification_item id of this_lab
cur.execute("SELECT id FROM classification_items WHERE classification_id = %s AND attribute1_oto =%s",(this_cid,this_lab))
for row in cur:
    this_lid = row[0] 
    
# First, find all datasets that are linked to this classification:
datasetlist = []
dataposlist = []
for m in range(0,12):
    cur.execute("SELECT id FROM datasets WHERE aspect_%s_classification = %s",(m+1,this_cid))
    for row in cur:
        print(row)
        datasetlist.append(row[0]) # dataset_name    
        dataposlist.append(m+1)
    
# Second, check for each match if the chosen label is included in the dataset and print the relevant datasets:
nods = len(dataposlist)    

match_ds       = []
match_ds_count = []
match_da_name  = []
match_da_vers  = []
match_da_cate  = []
match_da_type  = []
match_da_desc  = []
for n in range(0,nods):
    cur.execute("SELECT COUNT(*) FROM data WHERE dataset_id = %s AND aspect%s = %s",(datasetlist[n],dataposlist[n],this_lid))
    for row in cur:
        this_count = row[0]
        print(this_count)
        if this_count > 0:
            match_ds.append(datasetlist[n])
            match_ds_count.append(this_count)
            # get more info about this dataset to be displayed later:
            cur.execute("SELECT id, dataset_name, dataset_version, data_category, data_type, description FROM datasets WHERE id = %s",(datasetlist[n]))
            for row in cur:
                match_da_name.append(row[1])
                match_da_vers.append(row[2])
                match_da_cate.append(row[3])
                match_da_type.append(row[4])
                match_da_desc.append(row[5])
    
# Third, get all data types in sorted order and group the matching datasets into this order:
# Show (sorted by data type) a list of all datasets that contain information about this particular classification item
# for data categories 1-8:
# Display <H2> List of datasets that contain data for selected label </H2>
for dc in range(1,9): # from 1-8:
    cur.execute("SELECT name FROM categories WHERE id = %s ",(dc))
    for row in cur:
        None
        # Display <H3> Data category [dc]: [name] </H3> , insert values (dc,row[0])
        print('Data category {}: {}.'.format(dc,row[0]))
    # Check if we have matches in this category at all:
    if match_da_cate.count(dc) == 0:
        None
        # Display <p> No matches in this category </p>
        print('No matches in this category')
    else:
        # Get all types in this category and display info about matching datasets:
        cur.execute("SELECT id, name, reference_data_category, symbol FROM types WHERE reference_data_category = %s ",(dc))
        for row in cur:
            matching_indices = [i for i, x in enumerate(match_da_type) if x == row[0]]
            for i in matching_indices:
                # Display <p> [name], version [version], [description] This dataset contains {} entries for {}  </p> , insert values (match_da_name[i], match_da_vers[i], match_da_desc[i], match_ds_count[i], this_lab)
                print('{}, version {}, {}.'.format(match_da_name[i], match_da_vers[i], match_da_desc[i]))
                print('This dataset contains {} entries for {}.'.format(match_ds_count[i],this_lab))
        print('') # empty line before next dataset
    print('') # empty line before next data category

# Preview each dataset upon click, add download button, direct to search 5 (filter dataset) upon click for each dataset.
# SQL: SELECT value, ... FROM data WHERE id = i AND labelx = thislab LIMIT 10




# Other code, for experimenting:
# nomds = len(match_ds)
# print('Found {} datasets with data on {} in classification {}.'.format(nomds,this_lab,this_cid))
# print('')
        
# for o in range(0,nomds):
#     cur.execute("SELECT id, dataset_name, dataset_version, data_category, data_type, description FROM datasets WHERE id = %s",(match_ds[o]))
#     for row in cur:
#         print(row)
#         print('This dataset contains {} entries for {}.'.format(match_ds_count[o],this_lab))
#         print('')



#        