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

## 29.1.
### New data type
#SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES ('Characterisation factor','Environmental or social midpoint or endpoint indicator per unit of substance listed in life cycle inventory',3,'CF')"
#cur.execute(SQL)

# 5.2. Change data category
#SQL = "UPDATE types SET reference_data_category = 4 WHERE symbol = 'PAR'"
#cur.execute(SQL)
#
#SQL = "UPDATE types SET reference_data_category = 4 WHERE symbol = 'UPI'"
#cur.execute(SQL)

#8.3.2019
## New layers
#SQL = "INSERT INTO layers (name,description) VALUES ('Area','area measure of stocks or flows of products like buildings')"
#cur.execute(SQL)
#SQL = "INSERT INTO layers (name,description) VALUES ('Misc_share','share of a quantity in another total quantity, miscellaneous units')"
#cur.execute(SQL)

## add new aspect
#SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('economic_indicator','various intensive economic indicators',10,'E','Economic indicator')"
#cur.execute(SQL)


## New user
#SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (8,'qingshitu','Qingshi Tu','Yale','2019-01-01 12:00:00','2050-06-09 12:00:00')"
#cur.execute(SQL)

###10.3.2019
## add dimension 'object' for general objects of interest, comprises material, commodity, population, and other objects in the system, where the 'material' and 'commodity' dimensions don't fit.
#SQL = "INSERT INTO dimensions (id,name,description) VALUES (14,'object','general objects of interest, comprises material, commodity, population, and other objects in the system, where the material and commodity dimensions dont fit')"
#cur.execute(SQL)
## add new aspect	s
#SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('model','quantification by different models, model alternatives',9,'R','model veRsion')"
#cur.execute(SQL)
#SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('focus_object','object in focus of e.g., indicators',14,'i','none')"
#cur.execute(SQL)
#SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('reference_object','object or object group that serves as reference, e.g., for indicators',14,'j','none')"
#cur.execute(SQL)
## add SSP_Database_license:
#SQL = "INSERT INTO licences (id,name,description) VALUES (9,'SSP database license','license for using data from the SSP database at IIASA, copyright notice. For full text, cf. https://tntcat.iiasa.ac.at/SspDb/dsd?Action=htmlpage&page=about#termsofuse')"
#cur.execute(SQL)
## Add new units
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (8,'BnUS$2005','billion US Dollar of 2005',1000000000)"
#cur.execute(SQL)
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (2,'kg CO2 eq.','kg of CO2-equivalent (GWP)',1)"
#cur.execute(SQL)
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (6,'km2','square kilometer',1000000)"
#cur.execute(SQL)
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (5,'Mm3','million cubig meters',1000000)"
#cur.execute(SQL)

###30.5.2019
## Add new units
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (4,'toe','ton of oil equivalent',4.1868e10)"
#cur.execute(SQL)
#SQL = "INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (4,'Mtoe','million ton of oil equivalent',4.1868e16)"
#cur.execute(SQL)
## add layer
#SQL = "INSERT INTO layers (name,description) VALUES ('Energy','Energy layer')"
#cur.execute(SQL)
## add licences
#SQL = "INSERT INTO licences (id,name,description) VALUES (10,'© OECD/IEA 2016','OECD/IEA license, for full text, cf. https://www.iea.org/media/copyright/TermsandconditionsFinal11Jan2017.pdf')"
#cur.execute(SQL)
#SQL = "INSERT INTO licences (id,name,description) VALUES (11,'© OECD/IEA 2018','OECD/IEA license, for full text, cf. https://www.iea.org/media/copyright/TermsandconditionsFinal11Jan2017.pdf')"
#cur.execute(SQL)
### add new aspect
#SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('time_frame','indicates time periods or time frames, quantitative and qualitative, for data and indicators',1,'P','Period')"
#cur.execute(SQL)


## close connection
cur.close()
conn.close()
#
#    
#    
# The End
