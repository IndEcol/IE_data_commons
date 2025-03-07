# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:01:15 2018

@author: spauliuk
"""

import pymysql
import datetime
import IEDC_PW


#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

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
cur.execute("SELECT * FROM licences")
for row in cur:
    print(row)

cur.execute("SELECT * FROM users")
for row in cur:
    print(row)
    
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
## add new aspects	
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

### 12./13.11.2019
## Add new uncertainty options to stats_array
#cur.execute("INSERT INTO stats_array (name, description, loc) VALUES ('ca. value','data point flagged as ca. value without quantitative uncertainty estimate','ca. value')") 
## New data types
#SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES ('Stock change','change in stock (net addition, withdrawal, disposal, …)',2,'DS')"
#cur.execute(SQL)
#SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES ('Urban metabolism indicators','various indicators of urban metabolism, extensive, intensive.',6,'URB')"
#cur.execute(SQL)
## Fix typo in unit table:
#cur.execute("UPDATE units SET unit_name = 'million cubic meters' WHERE id = 94")
## add licence
#SQL = "INSERT INTO licences (id,name,description) VALUES (13,'Copyright CSIRO','Copyright CSIRO	License information provided for datasets made available by CSIRO')"
#cur.execute(SQL)
## Add new units
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (4,'PJ','Petajoule',1000000000000000000)")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (9,'mm','millimeter',0.001)")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (3,'CDD','cooling degree days',86400)")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'MEUR1995','million Euro 1995')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (6,'ha','hectare',10000)")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (3,'person*day','person-day',86400)")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'Chinese yuan','Chinese yuan')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'US dollars, 2010','US dollars, 2010')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'MUSD','million US dollars')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'Argentinian pesos','Argentinian pesos')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'Indian rupee','Indian rupee')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'USD','US Dollars')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'Nigerian naira','Nigerian naira')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'GBP pounds, 2010','British pounds, 2010')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'Philippine pesos','Philippine pesos')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'Mexican pesos','Mexican pesos')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'EUR','Euro')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'Korean won','Korean won')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'Iranian rial','Iranian rial')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (2,'t_CO2-eq','tonnes of CO2-equivalents',1000)")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (3,'Ml','Million litres',1000)")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (2,'kt BOD','kiloton of biochemical oxygen demand (wastewater indicator)')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (2,'kt COD','kiloton of chemical oxygen demand (wastewater indicator)')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (3,'person*yr','person-year')")
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (13,'GBq','gigabequerel',1000000000)")

## 4.12.19
## Add new layer
#SQL = "INSERT INTO layers (name,description) VALUES ('Radioactivity','activity of a quantity of radioactive material')"
#cur.execute(SQL)
#cur.execute("INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (3,'HDD','heating degree days',86400)")

## 25.11.2022
# add SSP_Database_license:
# SQL = "INSERT INTO licences (id,name,description) VALUES (14,'© by the International Society for Industrial Ecology','default license for material published in the Journal of Industrial Ecology (if not overridden by open access agreement)')"
# cur.execute(SQL)

## New category
#SQL = "INSERT INTO categories (id,name,description) VALUES (8,'Non-numerical','Non-numeric data such as boolean values or flags')"

## Add new layers
# SQL = "INSERT INTO layers (name,description) VALUES ('Constructed floor area','Total constructed floor area of buildings')"
# SQL = "INSERT INTO layers (name,description) VALUES ('Gross floor area','Gross floor area of buildings')"
# SQL = "INSERT INTO layers (name,description) VALUES ('Gross internal area','Gross internal area of buildings')"
# SQL = "INSERT INTO layers (name,description) VALUES ('Net internal area','Net internal area of buildings')"
# SQL = "INSERT INTO layers (name,description) VALUES ('Heated area','Heated area of buildings')"
# SQL = "INSERT INTO layers (name,description) VALUES ('Cooled area','Cooled area of buildings')"

## Add new aspects
# SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('end-use sector','sector of final consumption, where service is provided to households and public institutions',7,'U','end-Use sector')"
# SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('strategy','scenario alternative that involves a certain strategy or a combination thereof',9,'v','scenario alternati_v_e')"

## Add new units
# SQL = "UPDATE units SET refunit_id = 2, unitcode = 'MtC', unit_name = 'megatons of carbon-equivalents', factor = 1000000000 WHERE id = 14" 
# SQL = "UPDATE units SET refunit_id = 2, unitcode = 'Mt CO2-eq', unit_name = 'megatons of CO2-equivalents', factor = 1000000000 WHERE id = 15" 

### 25.4.23
## add dimension 'strategy_option', (ID: 15), to describe options for change in a system. The new strategy dimension is more appropriate to describe potential for change than the already existing scenario dimension, which links a certain system variable to a given set of exogenous assumptions. Here, however, the potential for change lies more within the process/material/product itself rather than in the exogenous assumptions made. In a scenario analysis, the strategy potentials (scenario-independent) will materialize to a certain scenario-dependent degree.
# SQL = "INSERT INTO dimensions (id,name,description) VALUES (15,'strategy_option','describe options for change in individual system elements. The strategy/option pertains to a possible change for a small unit in the system, whereas a scenario describes a possible future for the system as a whole, and needs a system-wide narrative.')"
# cur.execute(SQL)
## Update aspect and classificaitons linking to the new strategy dimension:
# cur.execute("SELECT id, aspect_8, aspect_8_classification FROM datasets")
# for row in cur:
#     if row[1] == 41:
#         print(row)    
# --> Only aspect 41 and classification 78 is affacted!
#Change dimension of aspect 41:
#cur.execute("UPDATE aspects SET dimension = 15 WHERE id = 41")
#cur.execute("UPDATE aspects SET index_letter_crib = 'alternati_v_e strategy or option' WHERE id = 41")
#cur.execute("UPDATE classification_definition SET dimension = 15 WHERE id = 78")

## New layers
#SQL = "INSERT INTO layers (name,description) VALUES ('TRL','technology readiness level')"
#cur.execute(SQL)

### 25.4.23
# SQL = "INSERT INTO layers (name,description) VALUES ('Volume','volume of a flow, e.g., for water')"
# cur.execute(SQL)
# SQL = "INSERT INTO layers (name,description) VALUES ('Production capacity','production capacity of plants, in e.g., Mt/yr')"
# cur.execute(SQL)

#SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('input_category','general category of an input to a process, used for process inventories',14,'q','none')"
#cur.execute(SQL)
#SQL = "INSERT INTO aspects (aspect,description,dimension,index_letter,index_letter_crib) VALUES ('output_category','general category of an output of a process, used for process inventories',14,'Q','none')"
#cur.execute(SQL)

# Nov. 2023 update
## New layers
# SQL = "INSERT INTO layers (name,description) VALUES ('primary energy','primary energy, as extracted from nature')"
# cur.execute(SQL)
# SQL = "INSERT INTO layers (name,description) VALUES ('secondary energy','secondary energy, after conversion from primary energy')"
# cur.execute(SQL)
# SQL = "INSERT INTO layers (name,description) VALUES ('final energy','final energy, at the point of final energy conversion for use')"
# cur.execute(SQL)
# SQL = "INSERT INTO layers (name,description) VALUES ('useful energy','useful energy, energy delivered for/as service')"
# cur.execute(SQL)
# SQL = "INSERT INTO layers (name,description) VALUES ('General ratio','General ratio of two quantities')"
# cur.execute(SQL)

# add new licenses
# SQL = "INSERT INTO licences (id,name,description,link) VALUES (15,'© European Union','Used for Eurostat data. Reuse is authorised provided the source is acknowledged.','https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Copyright/licence_policy')"
# cur.execute(SQL)
# SQL = "INSERT INTO licences (id,name,description) VALUES (16,'GNU General Public License v3.0','GNU General Public License v3.0')"
# cur.execute(SQL)

## Add new data types:
# NewTypes  = ['Process parameters']
# NewTypesD = ['general parameters that describe processes, extensive']
# NewTypesG = [5]
# NewTypesS = ['PP']

# for m in range(0,len(NewTypes)):
#     SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES (%s,%s,%s,%s)"
#     cur.execute(SQL,(NewTypes[m],NewTypesD[m],NewTypesG[m],NewTypesS[m]))

## Add new units
# SQL = "INSERT INTO units (refunit_id,unitcode,unit_name,factor) VALUES (2,'g CO2 eq.','g of CO2-equivalent (GWP)',0.001)"
# cur.execute(SQL)

# July. 2023 update
# Add new uncertainty options to stats_array
#cur.execute("INSERT INTO stats_array (name, description, loc, scale) VALUES ('25th and 75th percentile','25th and 75th percentile, some unit as value','25th percentile','75th percentile')") 
#cur.execute("INSERT INTO stats_array (name, description, loc, scale, shape) VALUES ('min-25th and 75th percentile-max','min-25th and 75th percentile-max, some unit as value','min','25th percentile','75th percentile;max')") 

## New user
# SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (9,'hmli','Huimei Li','IEF','2024-06-18 12:00:00','2050-06-09 12:00:00')"
# cur.execute(SQL)

# Nov. 2024 update:
#SQL = "INSERT INTO layers (name,description) VALUES ('Energy per product operation','Energy per unit of operation of product, like MJ/km driven')"
#cur.execute(SQL)
# SQL = "UPDATE types SET symbol = 'EI' WHERE symbol = 'EIP'"
# cur.execute(SQL)
# SQL = "INSERT INTO licences (id,name,description) VALUES (17,'© IIASA and contributing modeling teams 2024','license for using data from SSP database at IIASA, version 3.0 and 3.1 of 2024, see https://data.ece.iiasa.ac.at/ssp/#/license')"
# cur.execute(SQL)
# SQL = "INSERT INTO licences (id,name,description) VALUES (18,'© The authors','copyright lies with the authors')"
# cur.execute(SQL)
# SQL = "INSERT INTO licences (id,name,description) VALUES (19,'miscellaneous licenses, see the comments in the dataset','miscellaneous licenses, see the comments in the dataset')"
# cur.execute(SQL)
# SQL = "INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (8,'EUR2020','Euros of 2020')"
# cur.execute(SQL)
# SQL = "INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (5,'Nm3','standard cubic metre (Sm3), Normkubikmeter')"
# cur.execute(SQL)
# SQL = "INSERT INTO units (refunit_id,unitcode,unit_name) VALUES (2,'kt_F_gases_eq','kilotonnes of F-gases equivalents')"
# cur.execute(SQL)

## New user
#SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (10,'ilhch','Ilham Checkrad','IEF','2024-11-22 12:00:00','2050-06-09 12:00:00')"
#SQL = "UPDATE users SET name = 'Ilham Chekrad' WHERE id = 10" 
#cur.execute(SQL)
		
### IEDC March 2025 update
#cur.execute("INSERT INTO stats_array (name, description, loc, scale) VALUES ('2.5th and 97.5th percentile','2.5th and 97.5th percentile, of a given quantity, some unit as value','2.5th percentile','97.5th percentile')") 
#cur.execute("INSERT INTO stats_array (name, description, loc, scale) VALUES ('RSD','relative standard deviation (RSD) as share of mean (1) or % of mean (%)','RSD (unit: 1)','RSD (unit: %')") 
#cur.execute("INSERT INTO stats_array (name, description, loc, scale) VALUES ('5th and 95th percentile','5th and 95th percentile, of a given quantity, some unit as value','5th percentile','95th percentile')") 

#SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES ('Lorenz curve, normalized','normalized Lorenz curve (values from 0-1) of the cumulative ranked distribution of an indicator across a population',3,'LC')"
#SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES ('Lorenz curve, non-normalized, flow','non-normalized Lorenz curve of the cumulative ranked distribution of a flow across a population',1,'LCF')"
#SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES ('Lorenz curve, non-normalized, stock','non-normalized Lorenz curve of the cumulative ranked distribution of a stock across a population',2,'LCS')"
#SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES ('general ratio of flows linked to a process','general ratio of flows linked to a process - determined by the same process they are all connected to',4,'SHR')"
#SQL = "INSERT INTO types (name,description,reference_data_category,symbol) VALUES ('Boolean data type (flag)','Boolean data type (flag) to indicate whether a certain property is true for a given set of aspects or not',8,'FLG')"
#cur.execute(SQL)
#cur.execute("UPDATE types SET description = 'flows of all kind' WHERE id = 1") 
#cur.execute("UPDATE types SET description = 'material composition of products, alloys, waste/scrap, etc.' WHERE id = 6") 

#SQL = "INSERT INTO provenance (name,description) VALUES ('Representative values based on compilation from scientific literature and expert estimates','')"
#SQL = "INSERT INTO provenance (name,description) VALUES ('Representative (synthetic) sample, aggregated from survey results','Representative (including synthetic) sample, aggregated from survey results')"
#SQL = "INSERT INTO provenance (name,description) VALUES ('Measurements','Data derived directly from measurements')"
#cur.execute(SQL)


#SQL = "INSERT INTO layers (name,description) VALUES ('material volume per area','used to indicate material composition of buildings, where the values are given as m³ per building area')"
#cur.execute(SQL)

## New users
# SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (11,'almcs','Alexander McShane','IEF','2025-01-01 12:00:00','2050-06-09 12:00:00')"
# SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (12,'chrhs','Christian Hauenstein','IEF','2025-01-01 12:00:00','2050-06-09 12:00:00')"
# SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (13,'magel','Marcel Geller','IEF','2025-01-01 12:00:00','2050-06-09 12:00:00')"
# SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (14,'jnasr','Jad Nasr','IEF','2025-01-01 12:00:00','2050-06-09 12:00:00')"
# SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (15,'Jovel','Johan Vélez','IEF','2025-01-01 12:00:00','2050-06-09 12:00:00')"
# SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (16,'mjiang','Meng Jiang','Indecol-NTNU','2025-01-01 12:00:00','2050-06-09 12:00:00')"
# SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (17,'mveng','Martijn van Engelenburg','CML','2025-01-01 12:00:00','2050-06-09 12:00:00')"
# SQL = "INSERT INTO users (id,username,name,institution,start_date,end_date) VALUES (18,'arcast','Arias Castillo','INEC HS Pforzheim','2025-01-01 12:00:00','2050-06-09 12:00:00')"
#cur.execute(SQL)
# cur.execute("UPDATE users SET username = 'jovel' WHERE id = 15") 

# fix aspect table entry
#cur.execute("UPDATE aspects SET description = 'dimensionless aspect (with unit 1)' WHERE id = 4") 

#SQL = "INSERT INTO licences (id,name,description) VALUES (20,'CC BY NC 4.0','https://creativecommons.org/share-your-work/cclicenses/')"
#SQL = "INSERT INTO licences (id,name,description) VALUES (21,'CC BY ND 4.0','https://creativecommons.org/share-your-work/cclicenses/')"
#SQL = "INSERT INTO licences (id,name,description) VALUES (22,'CC BY NC ND 4.0','https://creativecommons.org/share-your-work/cclicenses/')"
#cur.execute(SQL)

# Add units:
# SQL = "UPDATE units SET refunit_id = 6, unitcode = 'cm2', unit_name = 'square centimeter', factor = 1E-4 WHERE id = 16"
# SQL = "UPDATE units SET refunit_id = 8, unitcode = 'MY', unit_name = 'million yen' WHERE id = 17"
# SQL = "UPDATE units SET refunit_id = 1, unitcode = 'household', unit_name = 'household', factor = 1 WHERE id = 18"
#SQL = "UPDATE units SET refunit_id = 7, unitcode = 'kVA', unit_name = 'kilo volt-ampere', factor = 1000 WHERE id = 19"
#cur.execute(SQL)
#cur.execute("UPDATE units SET factor = NULL WHERE id = 17") 

## New layer
SQL = "INSERT INTO layers (name,description) VALUES ('Energy per unit of output','specific energy requirement of a process per unit of output, e.g., in kWh/item')"
cur.execute(SQL)			


## close connection
cur.close()
conn.close()




#
#    
#    
# The End
