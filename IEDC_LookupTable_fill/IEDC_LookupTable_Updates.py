# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:01:15 2018

@author: spauliuk
"""

import pymysql
import datetime
import IEDC_PW


conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

## Add 'Mt' to 'Gg' unit:
#cur.execute("UPDATE units SET alt_unitcode = 'Mt' WHERE unitcode = 'Tg'") 
#
## fix misspelled æ:
#cur.execute("UPDATE units SET unitcode = 'µs' WHERE unitcode = 'æs'") 
#cur.execute("UPDATE units SET unitcode = 'µg' WHERE unitcode = 'æg'") 
#cur.execute("UPDATE units SET unitcode = 'µWs' WHERE unitcode = 'æWs'") 
#cur.execute("UPDATE units SET unitcode = 'µJ' WHERE unitcode = 'æJ'") 
#
#cur.execute("SELECT * FROM units")
#for row in cur:
#    print(row)


#cur.execute("SELECT * FROM stats_array")
#for row in cur:
#    print(row)
    
# Add litre:
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (5,'l','litre',0.001)"
#cur.execute(SQL)

# Add new uncertainty options to stats_array
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('1stddev','symmetric uncertainty range, +/-1 standard deviation, same unit as value','standard deviation (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('2stddevs','symmetric uncertainty range, +/-2 standard deviations, same unit as value','2 standard deviations (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('3stddevs','symmetric uncertainty range, +/-3 standard deviations, same unit as value','3 standard deviations (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('1stddev%','symmetric uncertainty range, +/-1 standard deviation, in % of value','standard deviation in % (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('2stddevs%','symmetric uncertainty range, +/-2 standard deviations, in % of value','2 standard deviations in % (half the uncertainty range)')") 
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('3stddevs%','symmetric uncertainty range, +/-3 standard deviations, in % of value','3 standard deviations in % (half the uncertainty range)')") 

### Add 'Mt' to 'Gg' unit:
#cur.execute("UPDATE units SET alt_unitcode = 'kt' WHERE unitcode = 'Gg'") 
#
## Add BYen:
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'BYen','billion Yen')"
#cur.execute(SQL)
#
## Add million GBP_2010:
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'million GBP_2010','million British Pounds_2010')"
#cur.execute(SQL)


## Add new layers:
#NewLayers = ['Dry mass','Wet mass','Lower heating value','Higher heating value','monetary (basic prices)','monetary (purchaser prices)','monetary (constant prices)']
#NewLayerD = ['Dry mass only','Wet mass (water content included)','Net Calorific Value (NCV)','Gross Calorific Value (GCV)','monetary value as basic price','monetary value as purchaser price','monetary value as constant price']
#for m in range(0,len(NewLayers)):
#    SQL = "INSERT INTO layers (name,description) VALUES (%s,%s)"
#    cur.execute(SQL,(NewLayers[m],NewLayerD[m]))


## Add new data types:
#NewTypes  = ['Misc_intensive','Activity parameters','Transfer coefficients','Criticality','Impact indicators','Flow_prices']
#NewTypesD = ['miscellaneous intensive properties, e.g., those used in ecoinvent','parameters, e.g., those used in ecoinvent','transfer coefficients, e.g., those used in ecoinvent','criticality indicators','impact indicators, e.g., from LC impact assessment','price information for flows (not products: 3_PR)']
#NewTypesG = [6,6,6,6,6,6]
#NewTypesS = ['MIP','PAR','TC','CR','IMI','FPR']
#
#for m in range(0,len(NewTypes)):
#    SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES (%s,%s,%s,%s)"
#    cur.execute(SQL,(NewTypes[m],NewTypesD[m],NewTypesG[m],NewTypesS[m]))

## Add new aspects
#NewAspects  = ['layer_in','layer_out','impact_indicator']
#NewAspectsD = ['Layer of quantification for incoming flow','Layer of quantification for outgoing flow','Impact indicator of flow']
#NewAspectsM = [12,12,10]
#NewAspectsL = ['a','A','I']
#NewAspectsC = ['L_a_yer_in','L_A_yer_out','Impact indicator']
# 
#for m in range(0,len(NewAspects)):
#    SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES (%s,%s,%s,%s,%s)"
#    cur.execute(SQL,(NewAspects[m],NewAspectsD[m],NewAspectsM[m],NewAspectsL[m],NewAspectsC[m]))

# Add explanations to lookup tables
#cur.execute("UPDATE aspects SET description = 'technology class of product or commodity in the sense of product type' WHERE aspect = 'technology'")
#cur.execute("UPDATE aspects SET description = 'layer of qantification: mass, volume, energy, radioactivity, monetary, ...' WHERE aspect = 'layer'")
#cur.execute("UPDATE aspects SET index_letter_crib = 's_ubstituting' WHERE aspect = 'substituting_material'")	
#cur.execute("UPDATE aspects SET description = 'refers to the material that substitutes another one' WHERE aspect = 'substituting_material'")	

#23.1.19 Add data category 7 (correspondence tables)
## New category
#SQL = "INSERT INTO categories (id,name,description) VALUES (7,'Correspondence','Correspondence between two classifications')"
#cur.execute(SQL)
#
## New data type
#SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES ('correspondence_table','Correspondence between two classifications',7,'CT')"
#cur.execute(SQL)
#
## New layer
#SQL = "INSERT INTO layers (name,description) VALUES ('Correspondence','Correspondence between two classifications')"
#cur.execute(SQL)
#
## add component aspect
#SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('component','component of product or other object',6,'k','k(c)omponent')"
#cur.execute(SQL)


## close connection
cur.close()
conn.close()
#
#    
#    
# The End
