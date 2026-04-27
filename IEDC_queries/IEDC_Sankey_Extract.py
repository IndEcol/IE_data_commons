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
This file documents text and SQL queries for the IEDC-floweaver Sankey link.

Step 1: On the IEDC homepage https://www.database.industrialecology.uni-freiburg.de/
the user selects a dataset from the catalogue. Then the description of the dataset is shown.

Step 2: Check if the selected dataset has a Sankey linked to it, using the following query,
and populate the dropdown menu lists if yes:
'''
this_id = 496 # id of Watari steel Sankey datasets, which has a Sankey link
cur.execute("SELECT reserve1 FROM datasets WHERE id = %s",(this_id))
for row in cur:
    SankeyLink = row[0] 
if SankeyLink == 'floweaver_sankey_link': # 'floweaver_sankey_link' must be given here to activate the Sankey link
    # Success! This dataset is linked to a Sankey. Now, we populate the dropdown menus:
    # First we get the classification ids of the different materials, regions, etc. a
    # Second, we get the classification labels of the different materials,regions.
    # For materials:
    menu_items_material  =  []
    menu_items_materialD =  []
    cur.execute("SELECT DISTINCT aspect2 FROM data WHERE dataset_id = %s",(this_id))  
    for row in cur:
        menu_items_material.append(row[0])
    cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_items.id IN %s",(set(menu_items_material)))        
    for row in cur:
        menu_items_materialD.append(row[0])
    # For layer    
    menu_items_layer  =  []
    menu_items_layerD =  []
    cur.execute("SELECT DISTINCT aspect3 FROM data WHERE dataset_id = %s",(this_id))  
    for row in cur:
        menu_items_layer.append(row[0])
    cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_items.id IN %s",(set(menu_items_layer)))        
    for row in cur:
        menu_items_layerD.append(row[0])        
    # For region    
    menu_items_region  =  []
    menu_items_regionD =  []
    cur.execute("SELECT DISTINCT aspect4 FROM data WHERE dataset_id = %s",(this_id))  
    for row in cur:
        menu_items_region.append(row[0])
    cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_items.id IN %s",(set(menu_items_region)))        
    for row in cur:
        menu_items_regionD.append(row[0])        
    # For time    
    menu_items_time  =  []
    menu_items_timeD =  []
    cur.execute("SELECT DISTINCT aspect5 FROM data WHERE dataset_id = %s",(this_id))  
    for row in cur:
        menu_items_time.append(row[0])
    cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_items.id IN %s",(set(menu_items_time)))        
    for row in cur:
        menu_items_timeD.append(row[0])        
    # For scenario    
    menu_items_scenario  =  []
    menu_items_scenarioD =  []
    cur.execute("SELECT DISTINCT aspect8 FROM data WHERE dataset_id = %s",(this_id))  
    for row in cur:
        menu_items_scenario.append(row[0])
    cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_items.id IN %s",(set(menu_items_scenario)))        
    for row in cur:
        menu_items_scenarioD.append(row[0])        
                
'''
If there is no SankeyLink: Do nothing (no warning etc.)
If there is a SankeyLink: Continue as follows:
    
AFTER: "System definition of corresponding datagroup (if applicable):"
and
BEFORE: "Dataset Preview (may take a few moments to refresh):"

1. Display: "For this dataset, a floweaver Sankey is available:"

2. Place five dropdown menus on one line, populated with the labels above:
    region / year / material / layer / scenario 
    PLUS a button on the right side: "Draw Sankey"
    
3. Pre-select the first item in each dropdown and draw the first Sankey, Details below

4. Allow the user to select different entries from the dropdown lists and redraw the Sankey if the "Draw Sankey" button is hit.
'''
# simulate the chosen dropdown parameters for the Sankey:
this_materialD   = menu_items_materialD[0] # Label, used for filename
this_material    = menu_items_material[menu_items_materialD.index(this_materialD)]
this_layerD      = menu_items_layerD[0] # Label, used for filename
this_layer       = menu_items_layer[menu_items_layerD.index(this_layerD)]
this_regionD     = menu_items_regionD[13] # Label, used for filename
this_region      = menu_items_region[menu_items_regionD.index(this_regionD)]
this_timeD       = menu_items_timeD[8] # Label, used for filename
this_time        = menu_items_time[menu_items_timeD.index(this_timeD)]
this_scenarioD   = menu_items_scenarioD[0] # Label, used for filename
this_scenario    = menu_items_scenario[menu_items_scenarioD.index(this_scenarioD)]

# With these parameters, the Sankey flow data can be queried for
# source (aspect 6), target (aspect 7), type (aspect 1), and value
# raw query with IDs, not labels, no JOIN:
SQL = "SELECT aspect6, aspect7, aspect1, value from data WHERE dataset_id = %s AND data.aspect2 = %s  AND data.aspect3 = %s AND data.aspect4 = %s AND data.aspect5 = %s AND data.aspect8 = %s"
cur.execute(SQL,(this_id,this_material,this_layer,this_region,this_time,this_scenario))       
for row in cur:
    print(row[0],row[1],row[2],row[3])
# final query with labels instead of IDs via JOIN statement:    
SQL = "SELECT ci1.attribute1_oto, ci2.attribute1_oto, ci3.attribute1_oto, d.value from data d INNER JOIN classification_items ci1 ON d.aspect6 = ci1.id INNER JOIN classification_items ci2 ON d.aspect7 = ci2.id INNER JOIN classification_items ci3 ON d.aspect1 = ci3.id WHERE dataset_id = %s AND aspect2 = %s  AND aspect3 = %s AND aspect4 = %s AND aspect5 = %s AND aspect8 = %s"
cur.execute(SQL,(this_id,this_material,this_layer,this_region,this_time,this_scenario))       
for row in cur:
    print(row[0],row[1],row[2],row[3]) # the four entries for each row of the .csv

# Extract data and save to csv:
# --> Language-specific implementation, very basic csv, no example provided here, see 
# https://floweaver.readthedocs.io/en/latest/tutorials/quickstart.html for an example    

'''
4. Link the chosen dataset and material to the right Sankey Config as specified here:
https://github.com/IndEcol/IEDC_floweaver_integration/blob/main/floweaver_IEDC_Sankey_configs/floweaver_IEDC_Sankey_configs.config 
(A local copy will be available on the vm in a suitable folder)
Draw the Sankey with D3.js, by combining the Sankey config as indicated in the config file and the dataset (.csv) generated above, as shown here:
    https://floweaver.readthedocs.io/en/latest/execute-spec-demo/
    
5. Enable the export buttons "export to .png" and "export to .svg"

6. Display the text: The floweaver Sankey configuration for this dataset is available via https://github.com/IndEcol/IEDC_floweaver_integration/

7. Display the floweaver logo
'''




# Other code, just for experimenting:
# cur.execute("SELECT DISTINCT attribute1_oto FROM classification_items JOIN data ON classification_items.id = data.aspect2 WHERE dataset_id = %s",(this_id))


#        