# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:57:29 2017

@author: spauliuk
"""

import pymysql
import datetime
import numpy as np
from os import walk, path
import xlrd
from datetime import date, timedelta
import csv

import IEDC_PW
import IEDC_Paths

def from_excel_ordinal(ordinal, _epoch=date(1900, 1, 1)):
    if ordinal > 59:
        ordinal -= 1  # Excel leap year bug, 1900 is not a leap year!
    return _epoch + timedelta(days=ordinal - 1)  # epoch is day 1



#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()


# Check
#cur.execute("SELECT COUNT(*) FROM classification_items")
#for row in cur:
#    print(row)    

#Modify classification items for Global_Material_Stocks_Assessment_Krausmann_2017
#cur.execute("UPDATE classification_items SET attribute1_oto = 'material extraction' WHERE attribute1_oto = 'reserved_1' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'technosphere'        WHERE attribute1_oto = 'reserved_2' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'other metals and minerals' WHERE attribute1_oto = 'reserved_33' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'sand and gravel'           WHERE attribute1_oto = 'reserved_34' AND classification_id = 4")

#Modify classification items for Global_Material_Stock_Flow_Wiedenhofer_2019    
#cur.execute("UPDATE classification_items SET attribute1_oto = 'aggregate, downcycled'                              WHERE attribute1_oto = 'reserved_35' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'aggregate, virgin'                                  WHERE attribute1_oto = 'reserved_36' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'glass, flat glass'                                  WHERE attribute1_oto = 'reserved_37' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'glass, container glass'                             WHERE attribute1_oto = 'reserved_38' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'all stock-building materials, primary production'   WHERE attribute1_oto = 'reserved_39' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'all stock-building materials, secondary production' WHERE attribute1_oto = 'reserved_40' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'all stock-building materials'                       WHERE attribute1_oto = 'reserved_41' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Global Stabilization Scenario', description = 'All model parameters and the primary material inputs are held constant at their levels of 2014; please note that primary sand and gravel quantities are partially estimated as the gap betwen downcycled aggregates and the demand for primary sand and gravel, therefore this quantity increases slightly because secondary recycling flows from concrete, asphalt and bricks lead to higher demand for primary sand and gravel' WHERE attribute1_oto = 'reserved_3' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Sustainable Circularity Scenario', description = 'All model parameters are held constant at their levels of 2014; while primary material inputs are reduced by -90% between 2014 and 2030, while all recycling rates are increased from their 2014 levels to 90% in 2030' WHERE attribute1_oto = 'reserved_4' AND classification_id = 8")

#Modify classification items for Global_Steel_Cycle_Milford_Pauliuk_2013
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Business as usual (BAU)'                                                     WHERE attribute1_oto = 'reserved_1' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Energy efficiency and material efficiency fully applied by 2100 (EEME2100)'  WHERE attribute1_oto = 'reserved_2' AND classification_id = 8")


##Classification 4:  add "wood, dry mass"
#cur.execute("UPDATE classification_items SET attribute1_oto = 'wood, dry mass' WHERE attribute1_oto = 'reserved_42' AND classification_id = 4")
#
##Classification 8:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'SSP1' WHERE attribute1_oto = 'reserved_5' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'SSP2' WHERE attribute1_oto = 'reserved_6' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'SSP2_450ppm' WHERE attribute1_oto = 'reserved_7' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'SSP2_sensitivity_cars' WHERE attribute1_oto = 'reserved_8' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'SSP3' WHERE attribute1_oto = 'reserved_9' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'SSP4' WHERE attribute1_oto = 'reserved_10' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'SSP5' WHERE attribute1_oto = 'reserved_11' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'RCP2.6' WHERE attribute1_oto = 'reserved_12' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'RCP3.4' WHERE attribute1_oto = 'reserved_13' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'RCP4.5' WHERE attribute1_oto = 'reserved_14' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'RCP6.0' WHERE attribute1_oto = 'reserved_15' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'RCP8.5' WHERE attribute1_oto = 'reserved_16' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'RCP_Baseline_(unmitigated)' WHERE attribute1_oto = 'reserved_17' AND classification_id = 8")
#
##Classification 6:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'EAF' WHERE attribute1_oto = 'reserved_3' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'BOF' WHERE attribute1_oto = 'reserved_4' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'foundries' WHERE attribute1_oto = 'reserved_5' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'forming' WHERE attribute1_oto = 'reserved_6' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'liquid metal cross section' WHERE attribute1_oto = 'reserved_7' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'scrap market' WHERE attribute1_oto = 'reserved_8' AND classification_id = 6")
#
##Classification 20:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Occupational health', description = 'measured in lost work-days' WHERE attribute1_oto = 'reserved_1' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Missing education', description = 'measured in no. of school-hours lost (or gained)' WHERE attribute1_oto = 'reserved_2' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Productivity loss from corruption', description = 'measured in monetary value of additional prod. costs' WHERE attribute1_oto = 'reserved_3' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Effect of trade barriers', description = 'measured in monetary value of subsidies' WHERE attribute1_oto = 'reserved_4' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Excessive work', description = 'measured in no. of work-hours in excess of 48/person/week' WHERE attribute1_oto = 'reserved_5' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Labour rights violations', description = 'measured in no. of work-hours of unorganised labour + reported violations' WHERE attribute1_oto = 'reserved_6' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Productivity loss from lacking physical infrastructure', description = 'measured in monetary contribution (in PPS) to local infrastructure development' WHERE attribute1_oto = 'reserved_7' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Unequal employment opportunities', description = 'measured in sum of wages in excess of balanced composition relative to recruitment base' WHERE attribute1_oto = 'reserved_8' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Poverty', description = 'measured in monetary value of specific, more than industry-average, efforts to provide: flexible jobs with low demands on skills, parent-friendly employment opportunities, fair transactions and payment options for the poor, and delivery and personal services for the disabled' WHERE attribute1_oto = 'reserved_9' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Inadequate access to health care', description = 'measured in no. of workers without adequate access to health care (defined as >1000 capita / doctor) for themselves and their family' WHERE attribute1_oto = 'reserved_10' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Unemployment and underemployment', description = 'measured as: Positive: No. of work-hours by workers recruited from long-term unemployment. Support to terminated workers.' WHERE attribute1_oto = 'reserved_11' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Inadequate access to pensions or social security', description = 'measured in no. of workers without adequate pension scheme and/or social security access' WHERE attribute1_oto = 'reserved_12' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Stressful working conditions', description = 'measured in no. of work-hours * relative stress measure above threshold' WHERE attribute1_oto = 'reserved_13' AND classification_id = 20")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Appropriation of indigenous resources', description = 'measured in assessed market value of resources with property rights assigned to indigenous people' WHERE attribute1_oto = 'reserved_14' AND classification_id = 20")
#	 
##Classification 18:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Materials/Fuels', attribute5_anc = 'ecospoldv2 Id 1', attribute6_anc = 'ecospoldv2 type = Input flow' WHERE attribute1_oto = 'reserved_1' AND classification_id = 18")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Electricity/Heat', attribute5_anc = 'ecospoldv2 Id 2', attribute6_anc = 'ecospoldv2 type = Input flow' WHERE attribute1_oto = 'reserved_2' AND classification_id = 18")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Services', attribute5_anc = 'ecospoldv2 Id 3', attribute6_anc = 'ecospoldv2 type = Input flow' WHERE attribute1_oto = 'reserved_3' AND classification_id = 18")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'From Technosphere (unspecified)', attribute5_anc = 'ecospoldv2 Id 5', attribute6_anc = 'ecospoldv2 type = Input flow' WHERE attribute1_oto = 'reserved_4' AND classification_id = 18")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'ReferenceProduct', attribute5_anc = 'ecospoldv2 Id 0', attribute6_anc = 'ecospoldv2 type = Output flow' WHERE attribute1_oto = 'reserved_5' AND classification_id = 18")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'By-product', attribute5_anc = 'ecospoldv2 Id 2', attribute6_anc = 'ecospoldv2 type = Output flow' WHERE attribute1_oto = 'reserved_6' AND classification_id = 18")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Material for Treatment', attribute5_anc = 'ecospoldv2 Id 3', attribute6_anc = 'ecospoldv2 type = Output flow' WHERE attribute1_oto = 'reserved_7' AND classification_id = 18")
#
#cur.execute("INSERT into classification_items (classification_id, attribute1_oto, attribute5_anc, attribute6_anc) VALUES (18,'Stock Additions','ecospoldv2 Id 5','ecospoldv2 type = Output flow')")
#cur.execute("INSERT into classification_items (classification_id, attribute1_oto, attribute5_anc, attribute6_anc) VALUES (18,'From Environment','ecospoldv2 Id 4','ecospoldv2 type = Elementary exchange')")
#cur.execute("INSERT into classification_items (classification_id, attribute1_oto, attribute5_anc, attribute6_anc) VALUES (18,'ToEnvironment','ecospoldv2 Id 4','ecospoldv2 type = Elementary exchange')")


# ISO region classification 2 update:
# Correct description:
#cur.execute("UPDATE classification_definition SET description = 'ISO 3166 classification of states and regions, with custom extensions. Numbers > 10000 are self-defined.'WHERE id = 2")    
#
## Add regions
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute4_oto) VALUES (%s,%s,%s)",(2,'America','10010'))
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute4_oto) VALUES (%s,%s,%s)",(2,'Switzerland and Liechtenstein','10011'))
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute4_oto) VALUES (%s,%s,%s)",(2,'Middle East','10012'))
#
## Fix spelling and other mistakes
#cur.execute("UPDATE classification_items SET attribute1_oto = 'French Guiana' WHERE attribute1_oto = 'French guiana' AND classification_id = 2")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Åland Islands' WHERE attribute1_oto = 'land Islands' AND classification_id = 2")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Curacao' WHERE attribute1_oto = 'Cura‡ao' AND classification_id = 2")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'South Georgia and the South Sandwich Islands' WHERE attribute1_oto = 'South georgia and the south sandwich is' AND classification_id = 2")
#cur.execute("UPDATE classification_items SET attribute1_oto = %s WHERE id = 5926 AND classification_id = 2",("Cote d'Ivoire"))
#cur.execute("UPDATE classification_items SET attribute1_oto = %s WHERE id = 5986 AND classification_id = 2",("Korea, democratic people's republic of"))

# 5.2. add 'unspecified'
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute4_oto) VALUES (%s,%s,%s)",(2,'unspecified','10013'))

# 8.3.2019 new materials and building types
##Classification 4:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'gravel' WHERE attribute1_oto = 'reserved_43' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'lime'   WHERE attribute1_oto = 'reserved_44' AND classification_id = 4")

##Classification 13:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'plants and warehouses'           WHERE attribute1_oto = 'reserved_1' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'office buildings'                WHERE attribute1_oto = 'reserved_2' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'commercial buildings'            WHERE attribute1_oto = 'reserved_3' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'education and culture buildings' WHERE attribute1_oto = 'reserved_4' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'other non-residential buildings' WHERE attribute1_oto = 'reserved_5' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'healthcare buildings'            WHERE attribute1_oto = 'reserved_6' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'research buildings'              WHERE attribute1_oto = 'reserved_7' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'other buildings'                 WHERE attribute1_oto = 'reserved_8' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'single family terraced houses'   WHERE attribute1_oto = 'reserved_9' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'apartment blocks'                WHERE attribute1_oto = 'reserved_10' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'education buildings'             WHERE attribute1_oto = 'reserved_11' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'hotels and restaurants'          WHERE attribute1_oto = 'reserved_12' AND classification_id = 13")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'recreational buildings'          WHERE attribute1_oto = 'reserved_13' AND classification_id = 13")

## 8.3.2019: Add regions
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute3_oto,attribute4_oto) VALUES (%s,%s,%s,%s)",(2,'Arab World','ARB','10014'))
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute2_oto, attribute3_oto, attribute4_oto) VALUES (%s,%s,%s,%s,%s)",(2,'European Union','EU','EUU','10015'))
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute3_oto,attribute4_oto) VALUES (%s,%s,%s,%s)",(2,'West Bank and Gaza','PSE','10016'))

## 10.3.2019
#cur.execute("UPDATE classification_items SET attribute1_oto = 'History'          WHERE attribute1_oto = 'reserved_18' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'PPP-GDP', description = 'gross domestic product based on purchasing power parity'          WHERE attribute1_oto = 'reserved_1' AND classification_id = 28")

### 27. April 2019, change process names in 200R steel cycle dataset
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Market for final products'          WHERE attribute2_oto = 11 AND classification_id = 16")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Market for parts of final products' WHERE attribute2_oto = 10 AND classification_id = 16")





# Close connection
cur.close()
conn.close()


#
#
#
#
#


