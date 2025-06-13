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
--> offer dropdown with these classifications, user needs to pick one.
--> Then, populate another dropdown with all entries from the chosen classification
For the example below, let's assume the user has picked the label 'copper' from class. 4'
'''
this_cid = 4
this_lab = 'copper'
#this_lab = 'glass'

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
for n in range(0,nods):
    cur.execute("SELECT COUNT(*) FROM data WHERE dataset_id = %s AND aspect%s = %s",(datasetlist[n],dataposlist[n],this_lid))
    for row in cur:
        this_count = row[0]
        print(this_count)
        if this_count > 0:
            match_ds.append(datasetlist[n])
            match_ds_count.append(this_count)
    
# Third, print some info about all datasets with a match:
nomds = len(match_ds)
print('Found {} datasets with data on {} in classification {}.'.format(nomds,this_lab,this_cid))
print('')
        
for o in range(0,nomds):
    cur.execute("SELECT id, dataset_name, dataset_version, data_category, data_type, description FROM datasets WHERE id = %s",(match_ds[o]))
    for row in cur:
        print(row)
        print('This dataset contains {} entries for {}.'.format(match_ds_count[o],this_lab))
        print('')

# Extra feature: Group these datasets by data type and category!

# Then: next to each dataset, offer a preview and download button.

#        