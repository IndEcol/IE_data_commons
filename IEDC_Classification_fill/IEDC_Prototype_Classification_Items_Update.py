﻿# -*- coding: utf-8 -*-
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

## 30.5.2019
#cur.execute("UPDATE classification_items SET attribute1_oto = 'all (unspecified)'          WHERE attribute1_oto = 'reserved_1' AND classification_id = 10")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity'                WHERE attribute1_oto = 'reserved_2' AND classification_id = 10")
#
#cur.execute("UPDATE classification_items SET attribute1_oto = 'ferronickel'                WHERE attribute1_oto = 'reserved_45' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'cement clinker'             WHERE attribute1_oto = 'reserved_46' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'sinter (iron ore)'          WHERE attribute1_oto = 'reserved_47' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'silicon (metallurgical grade)'   WHERE attribute1_oto = 'reserved_48' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'metal other than steel, Cu, Al'  WHERE attribute1_oto = 'reserved_49' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'straw'                      WHERE attribute1_oto = 'reserved_50' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'concrete aggregates'        WHERE attribute1_oto = 'reserved_51' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'mineral fill'               WHERE attribute1_oto = 'reserved_52' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'adobe'                      WHERE attribute1_oto = 'reserved_53' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'bitumen'                    WHERE attribute1_oto = 'reserved_54' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'clay'                       WHERE attribute1_oto = 'reserved_55' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'siding unspecified'         WHERE attribute1_oto = 'reserved_56' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'linoleum'                   WHERE attribute1_oto = 'reserved_57' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'carpet'                     WHERE attribute1_oto = 'reserved_58' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'heraklith'                  WHERE attribute1_oto = 'reserved_59' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'insulation unspecified'     WHERE attribute1_oto = 'reserved_60' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'other unspecified material' WHERE attribute1_oto = 'reserved_61' AND classification_id = 4")
#
#cur.execute("UPDATE classification_items SET attribute1_oto = 'polystyrene'                WHERE attribute1_oto = 'polystyrene ' AND classification_id = 4")
#
#cur.execute("UPDATE classification_items SET attribute1_oto = 'OECD', attribute4_oto = 10017  WHERE attribute1_oto = 'reserved_1' AND classification_id = 2")
#
#cur.execute("UPDATE classification_items SET attribute1_oto = '2000-2005' WHERE attribute1_oto = 'reserved_1' AND classification_id = 14")
#cur.execute("UPDATE classification_items SET attribute1_oto = '2010-2012' WHERE attribute1_oto = 'reserved_2' AND classification_id = 14")
#
#cur.execute("UPDATE classification_items SET attribute1_oto = 'collected EoL (end-of-life) products' WHERE attribute1_oto = 'reserved_1' AND classification_id = 7")
#
#cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity market' WHERE attribute1_oto = 'reserved_9' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity generation from fossil fuels' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity generation from nuclear reactors' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity generation from renewable sources' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity generation, total' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'industry' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'transport' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'other (commercial and public services, agriculture/forestry, fishing and non-specified)' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'non-energy use' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'energy markets' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'markets for final products and commodities' WHERE attribute1_oto = 'reserved_10' AND classification_id = 6")
#
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Bangkok' WHERE attribute1_oto = 'reserved_1' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Vienna' WHERE attribute1_oto = 'reserved_2' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Rio de Janeiro' WHERE attribute1_oto = 'reserved_3' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'not specified' WHERE attribute1_oto = 'reserved_4' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Turin' WHERE attribute1_oto = 'reserved_5' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Esch-sur-Alzette' WHERE attribute1_oto = 'reserved_6' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Macao SAR, China' WHERE attribute1_oto = 'reserved_7' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Chiclayo' WHERE attribute1_oto = 'reserved_8' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Philadelphia' WHERE attribute1_oto = 'reserved_9' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Los Angeles' WHERE attribute1_oto = 'reserved_10' AND classification_id = 11")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Taipei' WHERE attribute1_oto = 'reserved_11' AND classification_id = 11")
#	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings, urban, SFH' WHERE attribute1_oto = 'reserved_14' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings, urban, MFH' WHERE attribute1_oto = 'reserved_15' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings, rural, SFH' WHERE attribute1_oto = 'reserved_16' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings, rural, MFH' WHERE attribute1_oto = 'reserved_17' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings, urban' WHERE attribute1_oto = 'reserved_18' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings, rural' WHERE attribute1_oto = 'reserved_19' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'commercial buildings, urban' WHERE attribute1_oto = 'reserved_20' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'industrial buildings, urban' WHERE attribute1_oto = 'reserved_21' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings,  SFH' WHERE attribute1_oto = 'reserved_22' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings, MFH' WHERE attribute1_oto = 'reserved_23' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'industrial buildings' WHERE attribute1_oto = 'reserved_24' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'rural buildings' WHERE attribute1_oto = 'reserved_25' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'non-residential buildings, urban' WHERE attribute1_oto = 'reserved_26' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential and commercial buildings' WHERE attribute1_oto = 'reserved_27' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'diverse building types' WHERE attribute1_oto = 'reserved_28' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'unspecified' WHERE attribute1_oto = 'reserved_29' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'public buildings' WHERE attribute1_oto = 'reserved_30' AND classification_id = 13")	
#cur.execute("UPDATE classification_items SET attribute1_oto = 'urban buildings' WHERE attribute1_oto = 'reserved_31' AND classification_id = 13")	

###13.11.2019
# add unspecific year:
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(3,'unspecified'))
## Classfs. 7 and 8:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'wood and wood products' WHERE attribute1_oto = 'reserved_2' AND classification_id = 7")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'short' WHERE attribute1_oto = 'reserved_19' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'baseline' WHERE attribute1_oto = 'reserved_20' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'long' WHERE attribute1_oto = 'reserved_21' AND classification_id = 8")
## Classfs. 2, 14, and 28:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Asia-Pacific', attribute4_oto = 10018  WHERE attribute1_oto = 'reserved_2' AND classification_id = 2")
#cur.execute("UPDATE classification_items SET attribute1_oto = '2008' WHERE attribute1_oto = 'reserved_3' AND classification_id = 14")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'domestic extraction (DE)' WHERE attribute1_oto = 'reserved_2' AND classification_id = 28")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'domestic material consumption (DMC)' WHERE attribute1_oto = 'reserved_3' AND classification_id = 28")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'direct material input (DMI)' WHERE attribute1_oto = 'reserved_4' AND classification_id = 28")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'physical exports' WHERE attribute1_oto = 'reserved_5' AND classification_id = 28")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'physical imports' WHERE attribute1_oto = 'reserved_6' AND classification_id = 28")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'physical trade balance (PTB, net imports)' WHERE attribute1_oto = 'reserved_7' AND classification_id = 28")
## Classf. 6:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'markets for final products and commodities' WHERE attribute1_oto = 'reserved_11' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity generation, total' WHERE attribute1_oto = 'reserved_12' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity generation from nuclear reactors' WHERE attribute1_oto = 'reserved_13' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity generation from renewable sources' WHERE attribute1_oto = 'reserved_14' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'energy markets' WHERE attribute1_oto = 'reserved_15' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'industry' WHERE attribute1_oto = 'reserved_16' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'transport' WHERE attribute1_oto = 'reserved_17' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'residential' WHERE attribute1_oto = 'reserved_18' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'other (commercial and public services, agriculture/forestry, fishing and non-specified)' WHERE attribute1_oto = 'reserved_19' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'non-energy use' WHERE attribute1_oto = 'reserved_20' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'natural resources' WHERE attribute1_oto = 'reserved_21' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'market for extracted resources' WHERE attribute1_oto = 'reserved_22' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'processing industries' WHERE attribute1_oto = 'reserved_23' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'use phase - paper and packaging' WHERE attribute1_oto = 'reserved_24' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'use phase - furniture' WHERE attribute1_oto = 'reserved_25' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'use phase - buildings' WHERE attribute1_oto = 'reserved_26' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'use phase - infrastructure' WHERE attribute1_oto = 'reserved_27' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'use phase - agriculture' WHERE attribute1_oto = 'reserved_28' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'use phase - others' WHERE attribute1_oto = 'reserved_29' AND classification_id = 6")
## Classf. 4
#cur.execute("UPDATE classification_items SET attribute1_oto = 'coal' WHERE attribute1_oto = 'reserved_62' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'crop residues' WHERE attribute1_oto = 'reserved_63' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'crops' WHERE attribute1_oto = 'reserved_64' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'ferrous ores' WHERE attribute1_oto = 'reserved_65' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'grazed biomass and fodder crops' WHERE attribute1_oto = 'reserved_66' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'natural gas' WHERE attribute1_oto = 'reserved_67' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'non-ferrous ores' WHERE attribute1_oto = 'reserved_68' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'non-metallic minerals - construction dominant' WHERE attribute1_oto = 'reserved_69' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'non-metallic minerals - industrial or agricultural dominant' WHERE attribute1_oto = 'reserved_70' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'oil shale and tar sands' WHERE attribute1_oto = 'reserved_71' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'petroleum' WHERE attribute1_oto = 'reserved_72' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'wild catch and harvest' WHERE attribute1_oto = 'reserved_73' AND classification_id = 4")

###3.8.21
## Classfs. 2: Fix duplicate and incorrect entry for Kosovo 3digit code: from 780 to 10018
#cur.execute("UPDATE classification_items SET attribute4_oto = 10018 WHERE id = 5987")

### 25.11.22
#cur.execute("UPDATE classification_items SET attribute1_oto = 'coal' WHERE attribute1_oto = 'reserved_62' AND classification_id = 4")
# id: 14	time_ranges
# cur.execute("UPDATE classification_items SET attribute1_oto = 'before 1980' WHERE attribute1_oto = 'reserved_10' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = '1980-1989' WHERE attribute1_oto = 'reserved_11' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = '1990-1999' WHERE attribute1_oto = 'reserved_12' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'after 2000' WHERE attribute1_oto = 'reserved_13' AND classification_id = 14")

# id: 2	regions-iso
# cur.execute("UPDATE classification_items SET attribute1_oto = 'Non-OECD', attribute4_oto = 10018 WHERE attribute1_oto = 'reserved_10' AND classification_id = 2")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'EU27', attribute4_oto = 10019, attribute5_anc = 'Europe' WHERE attribute1_oto = 'reserved_11' AND classification_id = 2")

# id: 8	scenario alternatives
#cur.execute("UPDATE classification_items SET attribute1_oto = 'LED' WHERE attribute1_oto = 'reserved_22' AND classification_id = 8")

# id: 7	general_product_categores
# cur.execute("UPDATE classification_items SET attribute1_oto = 'fabrication scrap' WHERE attribute1_oto = 'reserved_10' AND classification_id = 7")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'products for re-use' WHERE attribute1_oto = 'reserved_100' AND classification_id = 7")


# id: 6	broad industry groups
#cur.execute("UPDATE classification_items SET attribute5_anc = 'scope 1' WHERE attribute1_oto = 'use phase' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'primary production', attribute5_anc = 'production from natural resources, like metal ores or other minerals' WHERE attribute1_oto = 'reserved_30' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'secondary production', attribute5_anc = 'production from waste and scrap' WHERE attribute1_oto = 'reserved_31' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'natural environment', attribute5_anc = 'complement of >all (entire economy)<' WHERE attribute1_oto = 'reserved_32' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'scope 2', attribute5_anc = 'indirect (GHG) emissions associated with the purchase of electricity, steam, heat, or cooling' WHERE attribute1_oto = 'reserved_33' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'scope 3', attribute5_anc = 'all indirect (GHG) emissions of an activity that are not part of scope 2' WHERE attribute1_oto = 'reserved_34' AND classification_id = 6")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'system-wide', attribute2_oto = 'entire system', attribute5_anc = 'Definition is relative to the system definition for this dataset' WHERE attribute1_oto = 'reserved_35' AND classification_id = 6")

# Nov. 2023 update
# cities = ['Dhaka',
# 'London',
# 'Paris',
# 'Moscow',
# 'Lagos',
# 'Cairo',
# 'Tehran',
# 'Istanbul',
# 'Manila',
# 'Karachi',
# 'Seoul',
# 'Tokyo',
# 'Osaka',
# 'Guangzhou',
# 'Shanghai']

# resv = ['reserved_12',
# 'reserved_13',
# 'reserved_14',
# 'reserved_15',
# 'reserved_16',
# 'reserved_17',
# 'reserved_18',
# 'reserved_19',
# 'reserved_20',
# 'reserved_21',
# 'reserved_22',
# 'reserved_23',
# 'reserved_24',
# 'reserved_25',
# 'reserved_26']


# for m in range(0,len(cities)):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =11"
#     cur.execute(SQL,(cities[m],resv[m]))
    
# cur.execute("UPDATE classification_items SET attribute1_oto = 'service buildings' WHERE attribute1_oto = 'reserved_32' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'mixed-use buildings' WHERE attribute1_oto = 'reserved_33' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings, row houses' WHERE attribute1_oto = 'reserved_34' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'residential buildings, high rise' WHERE attribute1_oto = 'reserved_35' AND classification_id = 13")

# cur.execute("UPDATE classification_items SET attribute1_oto = 'Material footprint (MF), raw material input (RMI), or raw material equivalent (RME) (synonyms)' WHERE attribute1_oto = 'reserved_10' AND classification_id = 79")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'Raw material equivalents of imports (RME_IM)' WHERE attribute1_oto = 'aw material equivalents of imports (RME_IM)' AND classification_id = 79")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'Raw material equivalents of exports (RME_EX)' WHERE attribute1_oto = 'reserved_12' AND classification_id = 79")

# gpc = ['roads',
# 'bridges',
# 'tunnels',
# 'airports',
# 'railways',
# 'wind turbines',
# 'solar PV generation units of all sizes',
# 'geothermal power stations']

# resv =['reserved_3',
# 'reserved_4',
# 'reserved_5',
# 'reserved_6',
# 'reserved_7',
# 'reserved_8',
# 'reserved_9',
# 'reserved_11']

# for m in range(0,len(gpc)):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =7"
#     cur.execute(SQL,(gpc[m],cities[m]))

#cur.execute("UPDATE classification_items SET attribute1_oto = 'palladium' WHERE attribute1_oto = 'paladium' AND classification_id = 4")

# matss = ['other metals (other than Fe, Al, Cu)',
# 'aggregates (other than in concrete)',
# 'other biomass-based materials (other than timber)',
# 'all metals',
# 'all non-metallic minerals',
# 'timber',
# 'total biomass',
# 'other fossil-based materials (other than bitumen, including plastics)',
# 'other minerals (other than concrete, bricks, glass, other aggregates)',
# 'all fossil fuel based materials',
# 'gravel (roof)',
# 'glass wool',
# 'raw material',
# 'refined material',
# 'manufactured goods',
# 'manufacturing scrap',
# 'manufacturing scrap for recycling',
# 'scrap',
# 'recycled material',
# 'packaging waste',
# 'plastic packaging waste',
# 'solid waste (all types)',
# 'waste paper and cardboard',
# 'waste rubber',
# 'waste textiles',
# 'waste, organic',
# 'mineralic waste',
# 'ferrous metal waste',
# 'non-ferrous metal waste',
# 'non-ferrous metal waste, precious metals only',
# 'non-ferrous metal waste, Cu, Al, and Ni only',
# 'non-ferrous metal waste, other than prec. metals and Cu/Al/Ni',
# 'waste, not specified',
# 'yttrium',
# 'tantalum',
# 'tellurium',
# 'titanium',
# 'sapele wood',
# 'praseodymium',
# 'natural rubber',
# 'limestone',
# 'indium',
# 'beryllium',
# 'bismuth',
# 'dysprosium',
# 'gallium',
# 'germanium',
# 'all waste excluding major mineral waste',
# 'waste electrical and electronic equipment (WEEE)',
# 'paper and cardboard packaging waste',
# 'wooden packaging waste',
# 'metallic packaging waste',
# 'glass packaging waste',
# 'waste for recycling']


# resv =['reserved_74',
# 'reserved_75',
# 'reserved_76',
# 'reserved_77',
# 'reserved_78',
# 'reserved_79',
# 'reserved_80',
# 'reserved_81',
# 'reserved_82',
# 'reserved_83',
# 'reserved_84',
# 'reserved_85',
# 'reserved_86',
# 'reserved_87',
# 'reserved_88',
# 'reserved_89',
# 'reserved_90',
# 'reserved_91',
# 'reserved_92',
# 'reserved_93',
# 'reserved_94',
# 'reserved_95',
# 'reserved_96',
# 'reserved_97',
# 'reserved_98',
# 'reserved_99',
# 'reserved_100',
# 'reserved_101',
# 'reserved_102',
# 'reserved_103',
# 'reserved_104',
# 'reserved_105',
# 'reserved_106',
# 'reserved_107',
# 'reserved_108',
# 'reserved_109',
# 'reserved_110',
# 'reserved_111',
# 'reserved_112',
# 'reserved_113',
# 'reserved_114',
# 'reserved_115',
# 'reserved_116',
# 'reserved_117',
# 'reserved_118',
# 'reserved_119',
# 'reserved_120',
# 'reserved_121',
# 'reserved_122',
# 'reserved_123',
# 'reserved_124',
# 'reserved_125',
# 'reserved_126',
# 'reserved_127']

    
# for m in range(0,len(matss)):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =4"
#     cur.execute(SQL,(matss[m],resv[m]))    


# yrs = ['before 1945',
# '1945-1970',
# '1971-2000',
# 'all years',
# '2010-2020',
# '2020-2080']

# resv =['reserved_4',
# 'reserved_5',
# 'reserved_6',
# 'reserved_7',
# 'reserved_8',
# 'reserved_9']

# for m in range(0,len(yrs)):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =14"
#     cur.execute(SQL,(yrs[m],resv[m]))

# bigs = ['remelting',
# 'electricity generation from wind turbines',
# 'electricity generation from hydropower station',
# 'electricity generation from solar PV',
# 'electricity generation from other modern renewables, including biomass and geothermal power',
# 'households',
# 'housholds, commerce, and other sources of MSW',
# 'all (entire economy including households and other end-use sectors)',
# 'market for waste']

# resv =['reserved_36',
# 'reserved_37',
# 'reserved_38',
# 'reserved_39',
# 'reserved_40',
# 'reserved_41',
# 'reserved_42',
# 'reserved_43',
# 'reserved_44']

# for m in range(0,len(bigs)):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =6"
#     cur.execute(SQL,(bigs[m],resv[m]))

# cur.execute("UPDATE classification_items SET attribute1_oto = 'electricity, from renewable sources' WHERE attribute1_oto = 'reserved_3' AND classification_id = 10")

# cur.execute("UPDATE classification_items SET attribute1_oto = 'Production capacity' WHERE attribute1_oto = 'reserved_15' AND classification_id = 20")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'Lifetime' WHERE attribute1_oto = 'reserved_16' AND classification_id = 20")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'Monetary' WHERE attribute1_oto = 'reserved_17' AND classification_id = 20")

# cur.execute("INSERT into classification_items (classification_id, attribute1_oto) VALUES (72,'all materials')")

# cnts = ['G7',
# 'G20',
# 'ASEAN',
# 'South and Central America',
# 'Other EU27 (2020) countries',
# 'Non EU27 (2020) countries',
# 'EU28']

# resv =['reserved_3',
# 'reserved_4',
# 'reserved_5',
# 'reserved_6',
# 'reserved_7',
# 'reserved_8',
# 'reserved_9']

# attr4 = [10020,10021,10022,10023,100001,100002,10024]


# for m in range(0,len(cnts)):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s, attribute4_oto = %s WHERE attribute1_oto = %s AND classification_id =2"
#     cur.execute(SQL,(cnts[m],attr4[m],resv[m]))

# SQL = "UPDATE classification_items SET attribute3_oto = %s WHERE attribute1_oto = %s AND classification_id =2"
# cur.execute(SQL,('GLO','Global'))

#cur.execute("UPDATE classification_items SET attribute1_oto = 'Western Sahara' WHERE attribute1_oto = 'Western sahara' AND classification_id = 2")

# July. 2023 update
#cur.execute("UPDATE classification_items SET attribute1_oto = 'structural wood' WHERE attribute1_oto = 'reserved_128' AND classification_id = 4")
# cur.execute("UPDATE classification_items SET attribute1_oto = '1990-2030' WHERE attribute1_oto = 'reserved_14' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = '2010-2018' WHERE attribute1_oto = 'reserved_15' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = '2010-2050' WHERE attribute1_oto = 'reserved_16' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = '2015-2050' WHERE attribute1_oto = 'reserved_17' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'n.a.' WHERE attribute1_oto = 'reserved_18' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = '1980-2004' WHERE attribute1_oto = 'reserved_19' AND classification_id = 14")
# cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute4_oto) VALUES (%s,%s,%s)",(2,'OECD Europe','10024'))
# cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute4_oto) VALUES (%s,%s,%s)",(2,'OECD North America','10025'))
# cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute4_oto) VALUES (%s,%s,%s)",(2,'OECD Pacific','10026'))
# cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute4_oto) VALUES (%s,%s,%s)",(2,'Economies in Transition (EIT)','10027'))
# cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto, attribute4_oto) VALUES (%s,%s,%s)",(2,'Africa and the Middle East','10028'))
# cur.execute("UPDATE classification_items SET attribute1_oto = 'non-residential buildings, concrete structure' WHERE attribute1_oto = 'reserved_36' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'non-residential buildings, masonry' WHERE attribute1_oto = 'reserved_37' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'non-residential buildings, steel structure' WHERE attribute1_oto = 'reserved_38' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'non-residential buildings, timber structure' WHERE attribute1_oto = 'reserved_39' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'multi-family houses, masonry' WHERE attribute1_oto = 'reserved_40' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'multi-family houses, steel structure' WHERE attribute1_oto = 'reserved_41' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'multi-family houses, timber structure' WHERE attribute1_oto = 'reserved_42' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'single-family house, concrete structure' WHERE attribute1_oto = 'reserved_43' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'single-family house, masonry' WHERE attribute1_oto = 'reserved_44' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'single-family house, steel structure' WHERE attribute1_oto = 'reserved_45' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'single-family house, timber structure' WHERE attribute1_oto = 'reserved_46' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'single-family house with concrete structure' WHERE attribute1_oto = 'reserved_47' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'single-family house with wooden structure' WHERE attribute1_oto = 'reserved_48' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'semi-detached house with concrete structure' WHERE attribute1_oto = 'reserved_49' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'semi-detached house with wooden structure' WHERE attribute1_oto = 'reserved_50' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'medium apartment building' WHERE attribute1_oto = 'reserved_51' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'large apartment building developed horizontally' WHERE attribute1_oto = 'reserved_52' AND classification_id = 13")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'large apartment building developed vertically' WHERE attribute1_oto = 'reserved_53' AND classification_id = 13")

# NewProds = ['motorcycle, engine power 4kW',
# 'motorcycle, engine power 11kW',
# 'motorcycle, engine power 25kW',
# 'motorcycle, engine power 50kW',
# 'intercity bus',
# 'city bus',
# 'bicycle',
# 'private car',
# 'SUV',
# 'electric bicycle',
# 'subway car',
# 'tram car',
# 'local train',
# 'passenger car, gasoline',
# 'passenger car, diesel',
# 'passenger car, battery electric',
# 'plug-in battery electric vehicle',
# 'diesel-powered bus',
# 'diesel-powered passenger rail',
# 'electric-powered passenger rail',
# 'electric-powered high-speed rail',
# 'jet fuel-powered aircraft',
# 'diesel-powered medium heavy-duty truck',
# 'diesel-powered heavy heavy-duty truck',
# 'diesel-powered freight rail',
# 'heavy fuel oil-powered containerships',
# 'heavy fuel oil-powered crude tanker',
# 'light duty vehicle',
# '2/3-wheeler',
# 'bus',
# 'medium duty vehicle',
# 'heavy-duty vehicle',
# 'truck',
# 'motorcycle',
# 'compact vehicle (660ml-2000ml) for freight',
# 'compact vehicle (660ml-2000ml) for own use',
# 'light-duty vehicle (less 660ml) for freight',
# 'light-duty vehicle (less 660ml) for own use',
# 'motor coache for own use',
# 'motor coache for passengers',
# 'ordinary passenger car (over 2000ml) for freight',
# 'ordinary passenger car (over 2000ml) for own use',
# 'other industrial truck',
# 'other vehicle for own use',
# 'small-size bus for own use',
# 'small-size bus for passengers',
# 'special-use car and auxiliary car',
# 'taxi',
# 'truck (light-duty cars) for own use',
# 'truck (light-duty) for freight',
# 'truck (ordinary vehicle) for own use',
# 'truck (ordinary, diesel-powered) for freight',
# 'truck (ordinary, gas-powered) for freight',
# 'trucks (small cars) for own use',
# 'truck (small, diesel-powered) for freight',
# 'truck (small, gas-powered) for freight',
# 'truck (tractor) for freight',
# 'industrial trailer, including agricultural trailer',
# 'platform truck, including trailers',
# 'rail car',
# 'aircrafts and helicopters',
# 'cargo ship',
# 'other vessel',
# 'ship',
# 'steel vessel',
# 'subway train',
# 'rigid bus',
# 'articulated bus',
# 'battery electric bus',
# 'service motor vehicle (road)',
# 'service motor vehicle (rail)',
# 'motorcycle (4-cylinder)',
# 'motorcycle (2-cylinder)',
# 'motorcycle (sport bike)',
# 'school bus',
# 'diesel-powered city bus',
# 'light rail trains',
# 'light rail trains, electric',
# 'pickup',
# 'sedan',
# 'heavy rail, passenger',
# 'heavy rail, passenger, diesel-powered',
# 'high speed rail',
# 'pedelec',
# 'passenger car, LPG',
# 'passenger car, bifuel CNG/petrol',
# 'passenger car, PHEV gasoline',
# 'passenger car, PHEV diesel',
# 'diesel-powered coach',
# 'aircraft, national kerosene',
# 'aircraft, international kerosene',
# 'trams and subway trains',
# 'long-distance train',
# 'motorcycle, 2-stroke gasoline engine',
# 'motorcycle, 4-stroke gasoline engine',
# 'motorcycle, battery-electric',
# 'medium duty truck',
# 'heavy-duty truck',
# 'non-operating vehicles',
# 'bus, government or business',
# 'bus, LNG',
# 'bus, CNG',
# 'bus, hybrid eletric',
# 'bus, H2, fuel cell',
# 'locomotive, diesel',
# 'locomotive, electric',
# 'locomotive, highspeed',
# 'aircraft, jetfuel',
# 'aircraft, biofuel',
# 'ship, fuel oil',
# 'ship, dual fuel',
# 'ship, LNG',
# 'ship, modifiel fuel oil',
# 'passenger car, hybrid electric',
# 'passenger car, fuel cell']

# for m in range(0,12):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =7"
#     cur.execute(SQL,(NewProds[m],'reserved_'+str(m+115)))

#cur.execute("UPDATE classification_items SET attribute1_oto = 'bus, LNG' WHERE attribute1_oto = 'reserved_127' AND classification_id = 7")
#cur.execute("UPDATE classification_items SET attribute1_oto = '2004' WHERE attribute1_oto = 'reserved_20' AND classification_id = 14")
#cur.execute("UPDATE classification_items SET attribute1_oto = '2005' WHERE attribute1_oto = 'reserved_21' AND classification_id = 14")
#cur.execute("UPDATE classification_items SET attribute1_oto = '2006' WHERE attribute1_oto = 'reserved_22' AND classification_id = 14")

#November 2024 update
#cur.execute("UPDATE classification_items SET attribute1_oto = 'bus, hybrid electric' WHERE attribute1_oto = 'bus, hybrid eletric' AND classification_id = 7")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'IIASA-WiC POP 2023' WHERE attribute1_oto = 'reserved_1' AND classification_id = 29")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'OECD ENV-Growth 2023' WHERE attribute1_oto = 'reserved_2' AND classification_id = 29")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'muscle power' WHERE attribute1_oto = 'reserved_4' AND classification_id = 10")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'compressed natural gas (CNG)' WHERE attribute1_oto = 'reserved_5' AND classification_id = 10")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'liquefied petroleum gas (LPG)' WHERE attribute1_oto = 'reserved_6' AND classification_id = 10")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'copper, electric grade' WHERE attribute1_oto = 'reserved_129' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'steel, automotive' WHERE attribute1_oto = 'reserved_130' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'pitch' WHERE attribute1_oto = 'reserved_131' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'bricks and tiles' WHERE attribute1_oto = 'reserved_132' AND classification_id = 4")

# NewTR = ['2020-2030',
# '2010',
# '2020',
# '2017',
# '2025',
# '2030',
# '2040',
# '2050',
# '2018',
# '2027',
# '2023',
# '2019',
# '2021',
# '2011',
# '2016',
# '2007',
# '2013',
# '2015',
# '1949',
# '1950',
# '1954',
# '1955',
# '1956',
# '1957',
# '1958',
# '1960-1979',
# '2000-2006']

# for m in range(0,27):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =14"
#     cur.execute(SQL,(NewTR[m],'reserved_'+str(m+23)))

# NewLayer = ['technology readiness level (TRL)',
# 'time',
# 'misc_share',
# 'monetary value (constant prices)',
# 'dry mass',
# 'service',
# 'electricity',
# 'mass ratio']

# for m in range(0,8):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =20"
#     cur.execute(SQL,(NewLayer[m],'reserved_'+str(m+18)))

# NewVehs = ['ICEV-g_Passenger car_Conventional design',
# 'ICEV-g_Light truck_Conventional design',
# 'ICEV-g_Microcar_Conventional design',
# 'ICEV-g_Minivan/SUV_Conventional design',
# 'ICEV-d_Passenger car_Conventional design',
# 'ICEV-d_Light truck_Conventional design',
# 'ICEV-d_Microcar_Conventional design',
# 'ICEV-d_Minivan/SUV_Conventional design',
# 'HEV_Passenger car_Conventional design',
# 'HEV_Light truck_Conventional design',
# 'HEV_Microcar_Conventional design',
# 'HEV_Minivan/SUV_Conventional design',
# 'PHEV_Passenger car_Conventional design',
# 'PHEV_Light truck_Conventional design',
# 'PHEV_Microcar_Conventional design',
# 'PHEV_Minivan/SUV_Conventional design',
# 'BEV_Passenger car_Conventional design',
# 'BEV_Light truck_Conventional design',
# 'BEV_Microcar_Conventional design',
# 'BEV_Minivan/SUV_Conventional design',
# 'HFCEV_Passenger car_Conventional design',
# 'HFCEV_Light truck_Conventional design',
# 'HFCEV_Microcar_Conventional design',
# 'HFCEV_Minivan/SUV_Conventional design',
# 'ICEV-g_Passenger car_Lightweight design',
# 'ICEV-g_Light truck_Lightweight design',
# 'ICEV-g_Microcar_Lightweight design',
# 'ICEV-g_Minivan/SUV_Lightweight design',
# 'ICEV-d_Passenger car_Lightweight design',
# 'ICEV-d_Light truck_Lightweight design',
# 'ICEV-d_Microcar_Lightweight design',
# 'ICEV-d_Minivan/SUV_Lightweight design',
# 'HEV_Passenger car_Lightweight design',
# 'HEV_Light truck_Lightweight design',
# 'HEV_Microcar_Lightweight design',
# 'HEV_Minivan/SUV_Lightweight design',
# 'PHEV_Passenger car_Lightweight design',
# 'PHEV_Light truck_Lightweight design',
# 'PHEV_Microcar_Lightweight design',
# 'PHEV_Minivan/SUV_Lightweight design',
# 'BEV_Passenger car_Lightweight design',
# 'BEV_Light truck_Lightweight design',
# 'BEV_Microcar_Lightweight design',
# 'BEV_Minivan/SUV_Lightweight design',
# 'HFCEV_Passenger car_Lightweight design',
# 'HFCEV_Light truck_Lightweight design',
# 'HFCEV_Microcar_Lightweight design',
# 'HFCEV_Minivan/SUV_Lightweight design']

# NewVehsD = ['ICEV: internal combustion engine vehicle, gasoline',
# 'ICEV: internal combustion engine vehicle, gasoline',
# 'ICEV: internal combustion engine vehicle, gasoline',
# 'ICEV: internal combustion engine vehicle, gasoline',
# 'ICEV: internal combustion engine vehicle, diesel',
# 'ICEV: internal combustion engine vehicle, diesel',
# 'ICEV: internal combustion engine vehicle, diesel',
# 'ICEV: internal combustion engine vehicle, diesel',
# 'HEV: hybrid electric vehicle',
# 'HEV: hybrid electric vehicle',
# 'HEV: hybrid electric vehicle',
# 'HEV: hybrid electric vehicle',
# 'PHEV: plugin hybrid electric vehicle',
# 'PHEV: plugin hybrid electric vehicle',
# 'PHEV: plugin hybrid electric vehicle',
# 'PHEV: plugin hybrid electric vehicle',
# 'BEV: battery electric vehicle',
# 'BEV: battery electric vehicle',
# 'BEV: battery electric vehicle',
# 'BEV: battery electric vehicle',
# 'HFCEV: hydrogen fuell cell electric vehicle',
# 'HFCEV: hydrogen fuell cell electric vehicle',
# 'HFCEV: hydrogen fuell cell electric vehicle',
# 'HFCEV: hydrogen fuell cell electric vehicle',
# 'ICEV: internal combustion engine vehicle, gasoline',
# 'ICEV: internal combustion engine vehicle, gasoline',
# 'ICEV: internal combustion engine vehicle, gasoline',
# 'ICEV: internal combustion engine vehicle, gasoline',
# 'ICEV: internal combustion engine vehicle, diesel',
# 'ICEV: internal combustion engine vehicle, diesel',
# 'ICEV: internal combustion engine vehicle, diesel',
# 'ICEV: internal combustion engine vehicle, diesel',
# 'HEV: hybrid electric vehicle',
# 'HEV: hybrid electric vehicle',
# 'HEV: hybrid electric vehicle',
# 'HEV: hybrid electric vehicle',
# 'PHEV: plugin hybrid electric vehicle',
# 'PHEV: plugin hybrid electric vehicle',
# 'PHEV: plugin hybrid electric vehicle',
# 'PHEV: plugin hybrid electric vehicle',
# 'BEV: battery electric vehicle',
# 'BEV: battery electric vehicle',
# 'BEV: battery electric vehicle',
# 'BEV: battery electric vehicle',
# 'HFCEV: hydrogen fuell cell electric vehicle',
# 'HFCEV: hydrogen fuell cell electric vehicle',
# 'HFCEV: hydrogen fuell cell electric vehicle',
# 'HFCEV: hydrogen fuell cell electric vehicle']

# for m in range(0,48):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s, description = %s WHERE attribute1_oto = %s AND classification_id =7"
#     cur.execute(SQL,(NewVehs[m],NewVehsD[m],'reserved_'+str(m+128)))

# NewLy = ['technical lifetime',
# 'investment cost per capacity',
# 'fixed O&M costs per capacity',
# 'technology readiness level (TRL)',
# 'energy efficiency improvement',
# 'expected technology availability year',
# 'variable O&M costs per production',
# 'typical plant capacity',
# 'investment cost per capacity refurbishment',
# 'annualized fixed costs (CAPEX and O&M)',
# 'variable O&M costs per activity',
# 'CAPEX, greenfield',
# 'CAPEX, brownfield',
# 'OPEX, total',
# 'OPEX, alumina',
# 'OPEX, electricity',
# 'OPEX, anode',
# 'OPEX, labour',
# 'OPEX, other costs',
# 'OPEX, CCS plant O&M costs',
# 'OPEX, CCS plant fuel costs',
# 'retrofit CAPEX',
# 'variable O&M costs per capacity',
# 'assumed plant capacity',
# 'CAPEX - new build brownfield, Steam cracker',
# 'CAPEX - new build brownfield, General',
# 'O&M as % of CAPEX',
# 'O&M',
# 'CAPEX - new build brownfield, CCS',
# 'CAPEX - retrofit',
# 'CAPEX - new build brownfield, Electric steam cracker',
# 'CAPEX - new build brownfield, POX unit',
# 'CAPEX - new build brownfield, Methanol synthesis unit',
# 'CAPEX - new build brownfield, MTO unit',
# 'CAPEX - new build brownfield, Hydrogen burners',
# 'CAPEX - new build brownfield, NOx abatement unit',
# 'CAPEX - new build brownfield, Pyrolysis unit',
# 'CAPEX - new build brownfield, Hydrotreater',
# 'CAPEX - retrofit, Electric steam cracker',
# 'CAPEX - new build brownfield',
# 'CAPEX - new build brownfield, CCS unit',
# 'CAPEX - new build brownfield, all units',
# 'CAPEX - retrofit, all units']

# for m in range(0,43):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =28"
#     cur.execute(SQL,(NewLy[m],'reserved_'+str(m+8)))

# NewBld = ['industrial building, wood',
# 'civil building, wood',
# 'civil building, steel-concrete',
# 'industrial building, brick-wood',
# 'civil building, brick-wood',
# 'industrial building, brick-concrete',
# 'civil building, brick-concrete',
# 'industrial building, steel-concrete',
# 'civil building, steel',
# 'industrial building, steel',
# 'working shop',
# 'storehouse',
# 'energy station',
# 'teaching building',
# 'library',
# 'hall',
# 'hotel',
# 'shower room',
# 'meeting room',
# 'washing room',
# 'toilet',
# 'forging shop',
# 'heat-treatment shop',
# 'electronic shop',
# 'paper machine room',
# 'chemical shop',
# 'paper making shop',
# 'machine shop']

# for m in range(0,28):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =13"
#     cur.execute(SQL,(NewLy[m],'reserved_'+str(m+54))) ###  ERROR: Wrong labels uploaded! Fix below.

# InsLy =['CAPEX - new build brownfield, PDH',
# 'CAPEX - retrofit, Feedstock switch',
# 'CAPEX - new build brownfield, C3 splitter',
# 'specific capital costs',
# 'operating costs, use of green hydrogen',
# 'operating costs, electricity use',
# 'operating costs, other',
# 'compensation, lost metallurgical gases',
# 'operating costs, carbon capture, transport, storage',
# 'operating costs, materials',
# 'specific capital costs, CCU retrofitting',
# 'sales, methanol',
# 'operating costs, H2 for methanol synthesis']

# for m in range(0,13):
#     cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(28,InsLy[m]))

# InsLby =['boiler shop',
# 'cold room',
# 'cement plant',
# 'pharmaceutical shop',
# 'mess hall',
# 'pumping station',
# 'woodworking shop ',
# 'coal gas station',
# 'repair shop',
# 'metalwork shop',
# 'acid pickling shop',
# 'processing shop',
# 'foundry shop',
# 'tool shop',
# 'assembly shop',
# 'grinning shop',
# 'engine shop',
# 'molding shop',
# 'power station',
# 'boiler room',
# 'transformer room',
# 'compressed air station',
# 'blacksmith casting room',
# 'plate work shop',
# 'heat treatment shop',
# 'machine repair shop',
# 'bathroom',
# 'shopping mall',
# 'gelatin shop',
# 'drinking shop',
# 'theatre',
# 'gymnasium',
# 'production room',
# 'convenience store',
# 'kindergarten',
# ]

# for m in range(0,35):
#     cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(13,InsLby[m]))

### Nov. 2024 update/fix
# remove incomplete upload of class. items 83:
#cur.execute("DELETE FROM classification_items WHERE classification_id = 83")            

#cur.execute("UPDATE classification_items SET attribute1_oto = 'diesel-powered heavy-duty truck' WHERE attribute1_oto = 'diesel-powered heavy heavy-duty truck' AND classification_id = 7")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'passenger train' WHERE attribute1_oto = 'reserved_176' AND classification_id = 7")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'freight train' WHERE attribute1_oto = 'reserved_177' AND classification_id = 7")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'container ship, fuel oil-powered' WHERE attribute1_oto = 'reserved_178' AND classification_id = 7")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'crude oil tanker, fuel oil-powered' WHERE attribute1_oto = 'reserved_179' AND classification_id = 7")

# Fix wrong upload, by replacing economic indicators by building types:
# 1. Uncomment and re-build the two lists NewLy and NewBld

# for m in range(0,28):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =13"
#     cur.execute(SQL,(NewBld[m],NewLy[m])) ###  Fix from above.

#cur.execute("UPDATE classification_items SET attribute1_oto = 'kerosene' WHERE attribute1_oto = 'kerosene ' AND classification_id = 10")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'stainless steel' WHERE attribute1_oto = 'stainless steel ' AND classification_id = 4")

#cur.execute("UPDATE classification_items SET attribute1_oto = 'CAPEX - retrofit, feedstock switch' WHERE attribute1_oto = 'CAPEX - retrofit, Feedstock switch' AND classification_id = 28")

#cur.execute("UPDATE classification_items SET attribute1_oto = 'copper slag' WHERE attribute1_oto = 'Copper slag' AND classification_id = 83")
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(83,'CO2 direct'))

# update dimension for class. 84:
#cur.execute("UPDATE classification_definition SET dimension = 14 WHERE id = 84")    
#cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(83,'Copper anode'))
#cur.execute("UPDATE classification_items SET attribute1_oto = 'copper anode' WHERE attribute1_oto = 'Copper anode' AND classification_id = 83")
#cur.execute("UPDATE classification_items SET attribute1_oto = '2040-2045' WHERE attribute1_oto = 'reserved_50' AND classification_id = 14")
#cur.execute("UPDATE classification_items SET attribute1_oto = '2030-2035' WHERE attribute1_oto = 'reserved_51' AND classification_id = 14")
#cur.execute("UPDATE classification_items SET attribute1_oto = '2025-2030' WHERE attribute1_oto = 'reserved_52' AND classification_id = 14")

# March 2025 update
# cur.execute("UPDATE classification_items SET attribute1_oto = 'CED' WHERE attribute1_oto = 'reserved_13' AND classification_id = 79")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'product system of a given commodity' WHERE attribute1_oto = 'reserved_45' AND classification_id = 6")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'obsolete stock' WHERE attribute1_oto = 'reserved_46' AND classification_id = 6")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'mass per unit' WHERE attribute1_oto = 'reserved_26' AND classification_id = 20")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'Odense' WHERE attribute1_oto = 'reserved_27' AND classification_id = 11")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'Toronto' WHERE attribute1_oto = 'reserved_28' AND classification_id = 11")
# cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(28,'aptinc_992_j, pre-tax national income'))
# cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(28,'ahweal_992_j, net personal wealth'))
# cur.execute("UPDATE classification_items SET attribute1_oto = 'services generated by household appliances' WHERE attribute1_oto = 'reserved_1' AND classification_id = 12")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'fossil energy carriers' WHERE attribute1_oto = 'reserved_7' AND classification_id = 10")
# cur.execute("INSERT INTO classification_items (classification_id, description, attribute1_oto, attribute2_oto, attribute3_oto) VALUES (%s,%s,%s,%s,%s)",(86,'No CE measure','none','none','none'))
#cur.execute("UPDATE classification_items SET attribute1_oto = 'motor coaches for own use' WHERE attribute1_oto = 'motor coache for own use' AND classification_id = 7")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'motor coaches for passengers' WHERE attribute1_oto = 'motor coache for passengers' AND classification_id = 7")

## Add regions
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Fmr German Democratic Republic', attribute2_oto = 10029 WHERE attribute1_oto = 'reserved_12' AND classification_id = 2")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'West Germany, Federal Republic of Germany, 1949-1990', attribute2_oto = 10030 WHERE attribute1_oto = 'reserved_13' AND classification_id = 2")

# bldtypes = ['terraced house',
# 'apartment building',
# 'aboveground and belowground part of a building',
# 'aboveground part of a building',
# 'belowground part of a building',
# 'institutions',
# 'factory and workshop buildings',
# 'storage buildings',
# 'other service buildings, not agricultural',
# 'agricultural buildings',
# 'nursery home',
# 'institutions',
# 'fire station / resque station',
# 'agricultural sheds',
# 'hotels and guest houses',
# 'car dealership',
# 'supermarkets',
# 'warehouse',
# 'production halls',
# 'sport hall / multi-purpose hall',
# 'decentral combined heat and power station',
# 'schools',
# 'underground parking',
# 'multi-storey car park / parking deck',
# 'low-rise multi-unit residential building, laneway',
# 'low-rise multi-unit residential building, semi-detached',
# 'low-rise multi-unit residential building, row houses',
# 'low-rise multi-unit residential building, multiplexes',
# 'low-rise multi-unit residential building, apartments']

#for m in range(12,29):
#    cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(13,bldtypes[m]))
#cur.execute("UPDATE classification_items SET description = 'buildings for temporary residence (hospitals, nursery homes, boarding schools, military barracks, and the like)' WHERE attribute1_oto = 'institutions' AND classification_id = 13")

# trangesx=['before 1850',
# '1850 - 1930',
# '1931 - 1950',
# '1951 - 1960',
# '1961 - 1972',
# '1973 - 1978',
# '1979 - 1998',
# '1999 - 2006',
# '2007 - 2010',
# '2011 - 2020',
# 'ca. 2015-2020',
# '2001 and later',
# 'ca. 1990-2010',
# 'after 1990',
# 'before 1948']

# for m in range(0,15):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =14"
#     cur.execute(SQL,(trangesx[m],'reserved_'+str(m+53)))

## Add years to time ranges
# cur.execute("UPDATE classification_items SET attribute1_oto = 2012 WHERE attribute1_oto = 'reserved_68' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = 2014 WHERE attribute1_oto = 'reserved_69' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = 2022 WHERE attribute1_oto = 'reserved_70' AND classification_id = 14")
# cur.execute("UPDATE classification_items SET attribute1_oto = 1995 WHERE attribute1_oto = 'reserved_71' AND classification_id = 14")

# two new scenarios:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'maximum recycling potential' WHERE attribute1_oto = 'reserved_23' AND classification_id = 8")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'maximum reuse potential' WHERE attribute1_oto = 'reserved_24' AND classification_id = 8")

# CMPList = ['preparing for reuse of waste concrete',
# 'recycling of waste concrete',
# 'backfilling of waste concrete',
# 'incineration of waste concrete',
# 'landfilling of waste concrete',
# 'preparing for reuse of waste bricks',
# 'recycling of waste bricks',
# 'backfilling of waste bricks',
# 'incineration of waste bricks',
# 'landfilling of waste bricks',
# 'preparing for reuse of waste ceramics and tiles',
# 'recycling of waste ceramics and tiles',
# 'backfilling of waste ceramics and tiles',
# 'incineration of waste ceramics and tiles',
# 'landfilling of waste ceramics and tiles',
# 'preparing for reuse of waste insulation materials',
# 'recycling of waste insulation materials',
# 'backfilling of waste insulation materials',
# 'incineration of waste insulation materials',
# 'landfilling of waste insulation materials',
# 'preparing for reuse of waste gypsum',
# 'recycling of waste gypsum',
# 'backfilling of waste gypsum',
# 'incineration of waste gypsum',
# 'landfilling of waste gypsum',
# 'preparing for reuse of aluminium scrap',
# 'recycling of aluminium scrap',
# 'backfilling of aluminium scrap',
# 'incineration of aluminium scrap',
# 'landfilling of aluminium scrap',
# 'preparing for reuse of steel scrap',
# 'recycling of steel scrap',
# 'backfilling of steel scrap',
# 'incineration of steel scrap',
# 'landfilling of steel scrap',
# 'preparing for reuse of PVC',
# 'recycling of PVC',
# 'backfilling of PVC',
# 'incineration of PVC',
# 'landfilling of PVC',
# 'preparing for reuse of EPS',
# 'recycling of EPS',
# 'backfilling of EPS',
# 'incineration of EPS',
# 'landfilling of EPS',
# 'preparing for reuse of waste wood',
# 'recycling of waste wood',
# 'backfilling of waste wood',
# 'incineration of waste wood',
# 'landfilling of waste wood',
# 'preparing for reuse of waste glass',
# 'recycling of waste glass',
# 'backfilling of waste glass',
# 'incineration of waste glass',
# 'landfilling of waste glass',
# 'preparing for reuse of soil waste',
# 'recycling of soil waste',
# 'backfilling of soil waste',
# 'incineration of soil waste',
# 'landfilling of soil waste',
# 'preparing for reuse of dredging spoils',
# 'recycling of dredging spoils',
# 'backfilling of dredging spoils',
# 'incineration of dredging spoils',
# 'landfilling of dredging spoils']

# for m in range(0,65):
#     cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(82,CMPList[m]))

# CMProcL =['manufacturing of food, beverages & tobacco',
# 'manufacturing of textile & leather products',
# 'manufacturing of wood & wood products, medical & optical equipment & other manufacturing',
# 'manufacturing of paper and paper products',
# 'manufacturing industries: publishing and printing',
# 'manufacturing of petroleum products; cokes, and nuclear fuel',
# 'manufacturing of basic chemicals and man-made fibers',
# 'manufacturing of rubber and plastic products',
# 'manufacturing of other non-metallic mineral products',
# 'manufacturing of basic metals',
# 'manufacturing of fabricated metal products',
# 'manufacturing of machinery and equipment n.e.c.',
# 'manufacturing of office machinery & computers, radio, TV & communication equipment',
# 'manufacturing of electrical machinery n.e.c.',
# 'manufacturing of transport equipment',
# 'use phase - vehicles',
# 'use phase - machinery',
# 'use phase - electricity infrastructure',
# 'use phase - appliances']

# for m in range(0,19):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =6"
#     cur.execute(SQL,(CMProcL[m],'reserved_'+str(m+47)))
    
# CMNMat = ['glass and ceramics',
# 'mortar and gypsum',
# 'asphalt concrete',
# 'granite',
# 'powdered asphalt',
# 'sand and earth',
# 'sand-asphalt concrete',
# 'bituminous binder',
# 'crushed sand',
# 'grit',
# 'hydraulic binder',
# 'rock dust',
# 'prestressing steel',
# 'concrete reinforcement steel',
# 'low-alloyed steel',
# 'beech wood',
# 'tar oil - creosote',
# 'iron parts',
# 'railway ballast',
# 'brickwork',
# 'concrete, standard',
# 'concrete, lightweight',
# 'other nonferrous metals',
# 'bricks with insulation',
# 'roof tiles',
# 'asbestos cement panels',
# 'asbestos roofing',
# 'calcareous plaster mortar',
# 'plastering and mortar based on gypsum and anhydrite',
# 'plastering and mortar based on clay and loam',
# 'plastering and mortar with synthetic components',
# 'calcareous screeds',
# 'screed, based on gypsum and anhydrite',
# 'dry screed, containing gypsum and anhydrite',
# 'screed with synthetic components',
# 'sand-lime bricks',
# 'aerated concrete blocks',
# 'concrete blocks',
# 'mud bricks',
# 'gypsum plasterboard',
# 'mineralic building boards',
# 'insulation material, mineralic',
# 'roofing tile, concrete',
# 'roofing tile, fibre cement',
# 'roofing tile, slate']    

# for m in range(0,45):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =4"
#     cur.execute(SQL,(CMNMat[m],'reserved_'+str(m+133)))
    
# CMNeM=['substrate layer (green roof)',
# 'mineral fillings',
# 'ferrous metals',
# 'coverings containing aluminum, sealing membranes',
# 'other mineralic construction material',
# 'sawnwood',
# 'processed wood',
# 'bio-based insulation material',
# 'roof cover, reed or straw',
# 'other non-mineralic construction materials',
# 'insulation material, petroleum-based',
# 'roof cover made of plastics',
# 'sealing sheeting, petroleum-based',
# 'roof cover made of bitumen',
# 'bituminous coverings, waterproofing membranes',
# 'metal roofing',
# 'tube insulation',
# 'R410A',
# 'lubricating oil',
# 'polyol',
# 'polyamide, glass fibre reinforced',
# 'tetrafluoroethane',
# 'steel, cold-rolled',
# 'aluminium, extruded',
# 'titanium dioxide',
# 'borosilicate glass',
# 'polyurethane',
# 'wood, plastics, and composites',
# 'thermal and moisture protection',
# 'openings (doors, windows)',
# 'finishes (coating)',
# 'exterior improvements',
# 'other metals',
# 'aggregate, for concrete',
# 'aggregate, for asphalt',
# 'nylon',
# 'printed circuit board',
# 'acrylonnitrile butadiene styrene (ABS)',
# 'assorted mixed plastics',
# 'cadmium',
# 'cyclopentane',
# 'CFC11',
# 'CFC12',
# 'cleaning agent',
# 'copper tube',
# 'copper wire',
# 'elastomer (as ABS)',
# 'enamel',
# 'EPDM (ethylene propylene diene monomer rubber)',
# 'polystyrene, expanded (EPS)',
# 'europium',
# 'fabric',
# 'felt and reycled cotton',
# 'fibers and paper',
# 'glass, white',
# 'polyethylene, high density (HDPE)',
# 'mercury',
# 'polystyrene, high impact (HiPS)',
# 'iron (gray cast)',
# 'isobutane',
# 'lacquer',
# 'niobium',
# 'oil',
# 'inert material and other waste',
# 'other plastics',
# 'other biomass',
# 'non-metallic minerals',
# 'polyamide',
# 'palladium',
# 'paper and packaging',
# 'polybutylene terephthalate (PBT)',
# 'polycarbonate',
# 'polyethylene foil',
# 'polyethylene terephthalate (PET)',
# 'polychlorinated biphenyls (PCB)',
# 'polymethyl methacrylate (PMMA)',
# 'polypropylene',
# 'polyurethane',
# 'PS & HiPS',
# 'refrigerant',
# 'ruthenium',
# 'selenium',
# 'silica',
# 'stainless steel (HE01 & HE02)',
# 'stainless steel (HE03)',
# 'terbium',
# 'wood or cardboard']  

#cur.execute("UPDATE classification_items SET description = 'German: Polyalkohol' WHERE attribute1_oto = 'polyol' AND classification_id = 4")
#cur.execute("UPDATE classification_items SET description = 'composition: 50 % Trifluoromethane instead of Diflluormethane / 50 % Difluoroethane instead of Pentafluorethane' WHERE attribute1_oto = 'R410A' AND classification_id = 4")

# for m in range(78,87):
#     cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(4,CMNeM[m]))
  
# for m in range(0,45):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =4"
#     cur.execute(SQL,(CMNMat[m],'reserved_'+str(m+133)))
    
# CMNePr =['biomass power plant',
# 'coal-fired power plant',
# 'light fuel oil power plant',
# 'oil-fired gas turbine (SCGT)',
# 'gas power plant (CCGT)',
# 'gas power plant (SCGT)',
# 'solar PV, utility scale',
# 'concentrating solar power without storage',
# 'concentrating solar power with storage',
# 'large hydropower plant (dam) ( > 100MW)',
# 'medium hydropower plant (10-100MW)',
# 'small hydropower plant ( < 10MW)',
# 'wind turbines, onshore',
# 'wind turbines, offshore',
# 'nuclear power plant',
# 'light fuel oil standalone generator (1kW)',
# 'solar PV (distributed, with storage)',
# 'primary traffic road',
# 'secondary traffic road',
# 'primary local road',
# 'secondary and tertiary local road, parking lots',
# 'main path',
# 'local path',
# 'pavement',
# 'bike lane',
# 'motorway',
# 'federal road',
# 'state road',
# 'county road',
# 'municipal road',
# 'steel composite bridge',
# 'concrete bridge',
# 'steel bridge',
# 'road tunnel',
# 'railway bridge, crossing a valley',
# 'railway bridge, crossing a road',
# 'railway bridge, steel',
# 'railway tunnel, trenchless construction',
# 'railway tunnel, trench-based construction',
# 'railway sleepers of concrete as part of rail, single track',
# 'railway sleepers of wood as part of rail, single track',
# 'railway sleepers of steel as part of rail, single track',
# 'railway sleeper fittings, for concrete railway sleepers as part of rail, single track',
# 'railway sleeper fittings, for wooden railway sleepers as part of rail, single track',
# 'railway sleeper fittings, for steel railway sleepers as part of rail, single track',
# 'slab track (railway), single track',
# 'rails, S49 profile, as part of rail, single track',
# 'rails, S54 profile, as part of rail, single track',
# 'rails, UIC60 profile, as part of rail, single track',
# 'catenary mast of steel as part of rail, single track, no tunnel',
# 'catenary mast of concrete as part of rail, single track, no tunnel',
# 'catenary mast of concrete as part of high speed rail, single track, no tunnel',
# 'catenary wire, as part of rail, single track',
# 'catenary wire, as part of high speed rail, single track',
# 'railway substation, as part of rail, electric',
# 'signalling, railway, single track',
# 'cable for signalling, railway, single track',
# 'cable trench for signalling, railway, single track',
# 'continuous automatic train-running control, railway, single track',
# 'dishwashers',
# 'freezers',
# 'fridges',
# 'ovens',
# 'tumble dryers',
# 'washing machines',
# 'air-water heat pump, 15 kW',
# 'air-water heat pump, 7 kW',
# 'air-water heat pump, 50 kW',
# 'air source heat pump (ASHP) ',
# 'conventional electric water heater (CEWH)',
# 'flat plate solar water heater (FPSWH)',
# 'textiles',
# 'civil engineering',
# 'civil engineering, other than roads',
# 'machinery and equipment',
# 'computers and precision instruments',
# 'electrical equipment',
# 'motor vehicles, trailers, and semi-trailers',
# 'other transport equipment',
# 'furniture and other manufactured goods',
# 'furniture',
# 'printed matter and recorded media',
# 'food packaging',
# 'products, other',
# 'mobile phone',
# 'computer mouse',
# 'keyboard (computer)',
# 'web camera',
# 'LCD monitor',
# 'boom box',
# 'cable boxes (standby losses)',
# 'CD Player',
# 'DVD Player',
# 'receiver',
# 'satellite stations (standby losses)',
# 'tape player',
# 'telephone answering machine',
# 'TV (CRT - projection)',
# 'TV (CRT)',
# 'TV (DLP)',
# 'TV (LCD)',
# 'TV (plasma)',
# 'VCRs',
# 'video games',
# 'computer CPU',
# 'home copiers',
# 'home facsimile machines (thermal)',
# 'home fax/multi-function device (inkjet)',
# 'laptop charger',
# 'monitor',
# 'printers (inkjet)',
# 'printers (laser)',
# 'router/DSL/cable modem',
# 'pool heater',
# 'pool pump',
# 'spa (24 hour electric)',
# 'spa (24 hour gas)',
# 'spa (on-demand electric)',
# 'spa (on-demand gas)',
# 'sump/sewage pump',
# 'irrigation/pond/waterfall circulation pump',
# 'bottled water dispenser',
# 'broilers',
# 'coffee maker: drip (brew)',
# 'coffee maker: drip (warm)',
# 'coffee maker: percolater (brew)',
# 'coffee maker: percolater (warm)',
# 'compactors',
# 'deep fryer',
# 'wash dryer',
# 'vacuum cleaners',
# 'electric kettle',
# 'microwave oven',
# 'refrigerator',
# 'television',
# 'headphones',
# 'espresso maker',
# 'fry pans',
# 'instant hot water',
# 'slow cookers',
# 'toaster',
# 'toaster oven - toasting',
# 'toaster oven - oven',
# 'aquariums',
# 'auto engine heaters',
# 'clocks',
# 'dehumidifiers',
# 'doorbell',
# 'electric blankets',
# 'electric grills',
# 'electronic air cleaner/filter',
# 'garage door openers',
# 'gas grills',
# 'gas lighting',
# 'hair dryers',
# 'heat tape',
# 'humidifier',
# 'irons',
# 'pipe and gutter heaters',
# 'rechargable handheld vacuum cleaner (charging)',
# 'vacuum cleaner - canister',
# 'vacuum cleaner - upright',
# 'water bed heaters',
# 'air conditioner',
# 'color TV set',
# 'smoke exhaust ventilators',
# 'electric cooker',
# 'electric cooking appliances',
# 'electric kettles',
# 'water cooler-heaters',
# 'microwave ovens',
# 'soybean milk machines',
# 'sterilized cupboards',
# 'disinfection bowl cabinet',
# 'electric pressure cookers',
# 'electric water heaters',
# 'dust collectors',
# 'solar water heaters',
# 'shavers',
# 'electric fans',
# 'water heater for shower',
# 'warmers',
# 'household air cooler-heaters',
# 'landline telephone',
# 'computers',
# 'servers',
# 'calculators',
# 'black and white TV sets',
# 'video recorders',
# 'radio receivers',
# 'Hi-Fi stereo component system',
# 'recording machines',
# 'video recorder-players',
# 'DVD players',
# 'cameras',
# 'desktop computer system, including CRT',
# 'washing machines, dishwashers, clothes dryers, electric cookers, ovens, all appliances which deliver automatically all kinds of products',
# 'refrigerators, freezers and air conditioning units',
# 'CFC fridge',
# 'pentane fridge']

# for m in range(0,200):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =7"
#     cur.execute(SQL,(CMNePr[m],'reserved_'+str(m+180)))
    
# CMnePr2=['mix of CFC and pentane fridge',
# 'microwaves, electric heating appliances, electric fans',
# 'vacuum cleaners, carpet sweepers, etc, appliances used for sewing, knitting, weaving etc., toasters, fryers, grinders, coffee machines etc, appliances for hair-cutting etc, clocks, watches etc.',
# 'printers, copying equipment, facsimile equipment, telephones (fixed and mobile), including answering equipment, calculators, computers (desktop and laptop)',
# 'video recorders and DVD players, video cameras, audio equipment, radio sets, musical instruments',
# 'drills, saws, sewing machines, equipment for turning, milling, sanding, grinding, sawing, cutting, shearing, tools for riveting etc., tools for welding etc.',
# 'electric trains or car racing sets, hand-held video game consoles etc, computers for biking, diving, running, rowing, etc.',
# 'CRT monitor ',
# 'TV (CRT)',
# 'LCD monitor',
# 'TV (LCD)',
# 'WEEE 1: large household appliances',
# 'WEEE 2: small household appliances',
# 'WEEE 3: IT & telecommunications equipment',
# 'WEEE 4: consumer equipment (& photovoltaic panels)',
# 'WEEE 5a: lighting equipment (lamps)',
# 'WEEE 5b: lighting equipment (luminaires)',
# 'WEEE 6: electrical & electronic tools',
# 'WEEE 7: toys, leisure and sports equipment',
# 'WEEE 8: medical devices',
# 'WEEE 9: monitoring & control instruments',
# 'WEEE 10: automatic dispensers',
# 'WEEE 5: lighting equipment ',
# 'top-mount refrigerator (with freezer) ',
# 'clothes washer',
# 'dishwashers',
# 'room air conditioner',
# 'conventional oven',
# 'high efficiency oven',
# 'blu-ray disc player',
# 'DVD player',
# 'VCRs',
# 'MP3 player',
# 'digital camcorder',
# 'digital camera',
# 'gaming console',
# 'TV (LED)',
# 'TV (plasma)',
# 'LED monitor',
# 'CRT monitor',
# 'printer',
# 'laptop',
# 'desktop computer',
# 'central heating (household installed)',
# 'photovoltaic panels (incl. converters)',
# 'professional heating & ventilation (excl. cooling equipment)',
# 'dishwashers',
# 'kitchen appliances (e.g., large furnaces, ovens, cooking equipment)',
# 'washing machines (incl. combined dryers)',
# 'dryers (wash dryers, centrifuges)',
# 'household heating & ventilation (e.g., hoods, ventilators, space heaters)',
# 'fridges (incl. combi-fridges)',
# 'freezers',
# 'air conditioners (household installed and portable)',
# 'other cooling (e.g., dehumidifiers, heat pump dryers)',
# 'professional cooling (e.g., large air conditioners, cooling displays)',
# 'microwaves (incl. combined, excl. grills)',
# 'other small appliances',
# 'food preparation (e.g., toaster, grills, food processing, frying pans)',
# 'hot water (e.g., coffee, tea, water cookers)',
# 'vacuum cleaners (excl. professional)',
# 'personal care (e.g., tooth brushes, hair dryers, razors)',
# 'small IT (e.g., routers, mice, keyboards, external drives & accessories)',
# 'desktop PCs (excl. monitors, accessories)',
# 'laptops (incl. tablets)',
# 'printers (e.g., scanners, multifunctionals, faxes)',
# 'telecommunication devices (e.g., (cordless) phones, answering machines)',
# 'mobile phones (incl. smartphones, pagers)',
# 'professional IT (e.g., servers, routers, data storage, copiers)',
# 'CRT monitor',
# 'flat display panel monitors (LCD, LED)',
# 'small consumer electronic devices (e.g., headphones, remote controls)',
# 'portable audio & video (e.g., MP3 players, e-readers, car navigation)',
# 'music Instruments, radio, HiFi (incl. audio sets)',
# 'video equipment (e.g., video recorders, DVD players, Blu-ray disc players, set-top boxes)',
# 'speakers',
# 'cameras (e.g., camcorders, photo & digital still cameras)',
# 'TV (CRT)',
# 'lamps (e.g., pocket, christmas, excl. LED & incandescent)',
# 'compact fluorescent lamps (incl. retrofit & non-retrofit)',
# 'straight tube fluorescent lamps',
# 'special lamps (e.g., professional mercury, high & low pressure sodium)',
# 'household luminaires (incl. household incandescent fittings)',
# 'professional luminaires (offices, public space, industry)',
# 'household tools (e.g., drills, saws, high pressure cleaners, lawn mowers)',
# 'professional tools (e.g., for welding, soldering, milling)',
# 'toys (e.g., car racing sets, electric trains, music toys, biking computers)',
# 'gaming consoles',
# 'leisure (e.g., large exercise, sports equipment)',
# 'household medical equipment (e.g., thermometers, blood pressure meters)',
# 'professional medical equipment (e.g., hospital, dentist, diagnostics)',
# 'household monitoring & control equipment (alarm, heat, smoke, excl. screens)',
# 'professional monitoring & control equipment (e.g., laboratory, control panels)',
# 'non-cooled dispensers (e.g., for vending, hot drinks, tickets, money)',
# 'cooled dispensers (e.g., for vending, cold drinks)',
# 'flat display panel TV sets (LCD, LED, plasma)',
# 'LED lamps (incl. retrofit LED lamps & household LED luminaires)',
# 'washing machines',
# 'refrigerator',
# 'water heater for shower',
# 'air conditioner',
# 'smoke absorbers',
# 'microwave oven',
# 'mobile phone',
# 'cameras',
# 'desktop computer system, including CRT',
# 'desktop computer system, including LCD monitor',
# 'telephones',
# 'electric fans',
# 'fitness equipment',
# 'musical instruments',
# 'sewing machines',
# 'fans',
# 'air-cooler',
# 'air conditioner',
# 'refrigerator',
# 'microwave ovens',
# 'washing machines',
# 'tumble dryers',
# 'television',
# 'VCR/DVD',
# 'PCs & laptops',
# 'other small appliances',
# 'industrial digital printing press',
# 'vehicle parts']
    
# for m in range(123,125):
#     cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(7,CMnePr2[m]))
  
# CM83New=['brick-concrete structure',
# 'Frame structure',
# 'Shell wall structure',
# 'Urban Residential',
# 'Non-Residential',
# 'Residential building (not including the rural house)',
# 'Commercial building',
# 'Office',
# 'Education & Culture & Healthcare & Research',
# 'Plant & Warehouse',
# 'Other buildings',
# 'Rural house',
# 'garage/lightweight building',
# 'single-family residential building',
# 'multi-family building',
# 'multi-family high-rise building',
# 'commercial and industrial building',
# 'residential',
# 'commercial',
# 'non-residential buildings, concrete structure',
# 'non-residential buildings, masonry',
# 'non-residential buildings, steel structure',
# 'non-residential buildings, timber structure',
# 'multi-family houses, concrete structure',
# 'multi-family houses, masonry',
# 'multi-family houses, steel structure',
# 'multi-family houses, timber structure',
# 'single-family house, concrete structure',
# 'single-family house, masonry',
# 'single-family house, steel structure',
# 'single-family house, timber structure',
# 'detached houses, residential building',
# 'educational buildings, service building',
# 'health care buildings, service building',
# 'hotels and restaurants, service building',
# 'multi-family dwellings, residential building',
# 'offices, service building',
# 'semi-detached houses, residential building',
# 'single family dwellings, residential building',
# 'wholesale and retail trade buildings, service building',
# 'residential building',
# 'service building',
# 'industrial building',
# 'other building',
# 'nonres_health_ZEB, RES0',
# 'nonres_health_ZEB, RES2.1',
# 'nonres_health_ZEB, RES2.1+RES2.2',
# 'nonres_health_ZEB, RES2.2',
# 'nonres_health_efficient, RES0',
# 'nonres_health_efficient, RES2.1',
# 'nonres_health_efficient, RES2.1+RES2.2',
# 'nonres_health_efficient, RES2.2',
# 'nonres_health_non-standard, RES0',
# 'nonres_health_non-standard, RES2.1',
# 'nonres_health_non-standard, RES2.1+RES2.2',
# 'nonres_health_non-standard, RES2.2',
# 'nonres_health_standard, RES0',
# 'nonres_health_standard, RES2.1',
# 'nonres_health_standard, RES2.1+RES2.2',
# 'nonres_health_standard, RES2.2',
# 'nonres_hotels_restaurants_ZEB, RES0',
# 'nonres_hotels_restaurants_ZEB, RES2.1',
# 'nonres_hotels_restaurants_ZEB, RES2.1+RES2.2',
# 'nonres_hotels_restaurants_ZEB, RES2.2',
# 'nonres_hotels_restaurants_efficient, RES0',
# 'nonres_hotels_restaurants_efficient, RES2.1',
# 'nonres_hotels_restaurants_efficient, RES2.1+RES2.2',
# 'nonres_hotels_restaurants_efficient, RES2.2',
# 'nonres_hotels_restaurants_non-standard, RES0',
# 'nonres_hotels_restaurants_non-standard, RES2.1',
# 'nonres_hotels_restaurants_non-standard, RES2.1+RES2.2',
# 'nonres_hotels_restaurants_non-standard, RES2.2',
# 'nonres_hotels_restaurants_standard, RES0',
# 'nonres_hotels_restaurants_standard, RES2.1',
# 'nonres_hotels_restaurants_standard, RES2.1+RES2.2',
# 'nonres_hotels_restaurants_standard, RES2.2',
# 'nonres_offices_ZEB, RES0',
# 'nonres_offices_ZEB, RES2.1',
# 'nonres_offices_ZEB, RES2.1+RES2.2',
# 'nonres_offices_ZEB, RES2.2',
# 'nonres_offices_efficient, RES0',
# 'nonres_offices_efficient, RES2.1',
# 'nonres_offices_efficient, RES2.1+RES2.2',
# 'nonres_offices_efficient, RES2.2',
# 'nonres_offices_non-standard, RES0',
# 'nonres_offices_non-standard, RES2.1',
# 'nonres_offices_non-standard, RES2.1+RES2.2',
# 'nonres_offices_non-standard, RES2.2',
# 'nonres_offices_standard, RES0',
# 'nonres_offices_standard, RES2.1',
# 'nonres_offices_standard, RES2.1+RES2.2',
# 'nonres_offices_standard, RES2.2',
# 'nonres_commercial_ZEB, RES0',
# 'nonres_commercial_ZEB, RES2.1',
# 'nonres_commercial_ZEB, RES2.1+RES2.2',
# 'nonres_commercial_ZEB, RES2.2',
# 'nonres_commercial_efficient, RES0',
# 'nonres_commercial_efficient, RES2.1',
# 'nonres_commercial_efficient, RES2.1+RES2.2',
# 'nonres_commercial_efficient, RES2.2',
# 'nonres_commercial_non-standard, RES0',
# 'nonres_commercial_non-standard, RES2.1',
# 'nonres_commercial_non-standard, RES2.1+RES2.2',
# 'nonres_commercial_non-standard, RES2.2',
# 'nonres_commercial_standard, RES0',
# 'nonres_commercial_standard, RES2.1',
# 'nonres_commercial_standard, RES2.1+RES2.2',
# 'nonres_commercial_standard, RES2.2',
# 'nonres_education_ZEB, RES0',
# 'nonres_education_ZEB, RES2.1',
# 'nonres_education_ZEB, RES2.1+RES2.2',
# 'nonres_education_ZEB, RES2.2',
# 'nonres_education_efficient, RES0',
# 'nonres_education_efficient, RES2.1',
# 'nonres_education_efficient, RES2.1+RES2.2',
# 'nonres_education_efficient, RES2.2',
# 'nonres_education_non-standard, RES0',
# 'nonres_education_non-standard, RES2.1',
# 'nonres_education_non-standard, RES2.1+RES2.2',
# 'nonres_education_non-standard, RES2.2',
# 'nonres_education_standard, RES0',
# 'nonres_education_standard, RES2.1',
# 'nonres_education_standard, RES2.1+RES2.2',
# 'nonres_education_standard, RES2.2',
# 'nonres_other_ZEB, RES0',
# 'nonres_other_ZEB, RES2.1',
# 'nonres_other_ZEB, RES2.1+RES2.2',
# 'nonres_other_ZEB, RES2.2',
# 'nonres_other_efficient, RES0',
# 'nonres_other_efficient, RES2.1',
# 'nonres_other_efficient, RES2.1+RES2.2',
# 'nonres_other_efficient, RES2.2',
# 'nonres_other_non-standard, RES0',
# 'nonres_other_non-standard, RES2.1',
# 'nonres_other_non-standard, RES2.1+RES2.2',
# 'nonres_other_non-standard, RES2.2',
# 'nonres_other_standard, RES0',
# 'nonres_other_standard, RES2.1',
# 'nonres_other_standard, RES2.1+RES2.2',
# 'nonres_other_standard, RES2.2',
# 'MFH_ZEB, RES0',
# 'MFH_ZEB, RES2.1',
# 'MFH_ZEB, RES2.1+RES2.2',
# 'MFH_ZEB, RES2.2',
# 'MFH_efficient, RES0',
# 'MFH_efficient, RES2.1',
# 'MFH_efficient, RES2.1+RES2.2',
# 'MFH_efficient, RES2.2',
# 'MFH_non-standard, RES0',
# 'MFH_non-standard, RES2.1',
# 'MFH_non-standard, RES2.1+RES2.2',
# 'MFH_non-standard, RES2.2',
# 'MFH_standard, RES0',
# 'MFH_standard, RES2.1',
# 'MFH_standard, RES2.1+RES2.2',
# 'MFH_standard, RES2.2',
# 'RT_ZEB, RES0',
# 'RT_ZEB, RES2.1',
# 'RT_ZEB, RES2.1+RES2.2',
# 'RT_ZEB, RES2.2',
# 'RT_efficient, RES0',
# 'RT_efficient, RES2.1',
# 'RT_efficient, RES2.1+RES2.2',
# 'RT_efficient, RES2.2',
# 'RT_non-standard, RES0',
# 'RT_non-standard, RES2.1',
# 'RT_non-standard, RES2.1+RES2.2',
# 'RT_non-standard, RES2.2',
# 'RT_standard, RES0',
# 'RT_standard, RES2.1',
# 'RT_standard, RES2.1+RES2.2',
# 'RT_standard, RES2.2',
# 'SFH_ZEB, RES0',
# 'SFH_ZEB, RES2.1',
# 'SFH_ZEB, RES2.1+RES2.2',
# 'SFH_ZEB, RES2.2',
# 'SFH_efficient, RES0',
# 'SFH_efficient, RES2.1',
# 'SFH_efficient, RES2.1+RES2.2',
# 'SFH_efficient, RES2.2',
# 'SFH_non-standard, RES0',
# 'SFH_non-standard, RES2.1',
# 'SFH_non-standard, RES2.1+RES2.2',
# 'SFH_non-standard, RES2.2',
# 'SFH_standard, RES0',
# 'SFH_standard, RES2.1',
# 'SFH_standard, RES2.1+RES2.2',
# 'SFH_standard, RES2.2',
# 'large apartment building developed horizontally',
# 'large apartment building developed vertically',
# 'medium apartment building',
# 'semi-detached house with concrete structure',
# 'semi-detached house with wooden structure',
# 'single-family house with concrete structure',
# 'single-family house with wooden structure',
# 'Tables and desks',
# 'Upholstered chairs',
# 'Unupholstered chairs',
# 'Beds',
# 'Storage units',
# 'Stock of household furniture',
# 'Solid wood',
# 'Layer wood',
# 'Particle-board',
# 'Paper',
# 'Metals',
# 'Ferrous metal',
# 'Plastic',
# 'Concrete',
# 'Glass',
# 'Rubber',
# 'Paints',
# 'Adhesive',
# 'Textiles',
# 'Other polymers',
# 'Other substances',
# 'Boron Steel',
# 'Manganese Steel',
# 'Nickel Steel',
# 'Vanadium Steel',
# 'Chrome-Vanadium Steel',
# 'Tungsten',
# 'Chrome Steel',
# 'Chrome-Nickel Steel',
# 'Stainless Steel',
# 'Gas Boiler',
# 'Heat pump',
# 'PV panels',
# 'Splits',
# 'Printer (OEM new)',
# 'Printer',
# 'US industrial digital printing press (#1) (OEM new)',
# 'US industrial digital printing press (#1)',
# 'US industrial digital printing press (#2) (OEM new)',
# 'US industrial digital printing press (#2)',
# 'vehicle alternator (OEM new)',
# 'vehicle alternator',
# 'vehicle alternator',
# 'traditional vehicle engine (OEM new)',
# 'traditional vehicle engine',
# 'traditional vehicle engine, lightweight (OEM new)',
# 'traditional vehicle engine, lightweight',
# 'US HDOR engine (OEM new)',
# 'US HDOR engine',
# 'US HDOR alternator (OEM new)',
# 'US HDOR alternator',
# 'US HDOR turbocharger (OEM new)',
# 'industrial digital printers',
# 'vehicle parts',
# 'Heavy-duty and off-road (HDOR) equipment parts',
# 'Large and medium-sized tractors',
# 'Mini tractors',
# 'Motorized shellers',
# 'Combined Harvesters',
# 'Drainage and irrigation machinery',
# 'Pumps',
# 'Total power of agricultural machinery',
# 'General Power of industrial Machinery',
# 'Construction articulated hauler, 235 kW',
# 'Construction large articulated hauler, 470 kW',
# 'Construction wheeled excavator, 105kW',
# 'Construction large excavator, 278kW',
# 'Construction soil compaction equipment, 55kW',
# 'Construction asphalt compaction equipment, 31.4 kW',
# 'Construction asphalt compaction equipment, 110 kW',
# 'Construction medium wheeled excavator, 129.5kW',
# 'Construction large crawler excavator, 450kW',
# 'Construction asphalt wheeled pavening equipment, 55kW',
# 'Construction large asphalt pavening equipment, 200kW',
# 'Construction compact excavator, 12kW',
# 'Construction compact excavator, 43kW',
# 'Skid Steer and Compact wheeled Track Loaders, 36kW',
# 'Skid Steer and Compact Track Loaders, 46kW',
# 'Electric compact excavator, 15.6kW',
# 'Construction wheel loader, 204kW',
# 'Construction wheel loader, 397kW',
# 'Compact wheel loader, 36.4kW',
# 'Compact wheel loader, 87kW',
# 'Electric ompact wheel loader, 22kW',
# 'Power Saw',
# 'Water Pump 40kw',
# 'Conveyor belt',
# 'Elevator, hydraulic',
# 'Pump 40W',
# 'Air compressor, screw-type, 300kW',
# 'Air compressor, screw-type, 40kW',
# 'Tractor, T1',
# 'Tractor, T2',
# 'Tractor, T3',
# 'Tractor, T4',
# 'Sugarcane havester',
# 'Coffee harvester',
# 'self-propelled sprayer',
# 'Planter',
# 'Combiner',
# 'Average industrial machine',
# 'Average electronic component machinery',
# 'Average metal working machine',
# 'Refrigeration and A/C compressor, 15 kW',
# 'Ultra China Altitude Elevator',
# 'Synchronous reluctance motor, 10kW',
# 'Permanent magnet assissted synchronous reluctance motor, 10kW',
# 'Induction motor, 10kW',
# 'roads, asphalt paving',
# 'roads, stone paving',
# 'roads, mixed stone and soil paving',
# 'roads, soil paving',
# 'roads, motorway',
# 'roads, primary',
# 'roads, secondary',
# 'roads, tertiary',
# 'roads, local',
# 'roads, rural',
# 'bridges, motorway bridge',
# 'bridges, other road bridges',
# 'tunnel, road tunnel',
# 'runway(flexible), runway (flexible)',
# 'runway (rigid), runway (rigid)',
# 'railway, railway',
# 'railway bridge, railway bridge',
# 'railway tunnel, railway tunnel',
# 'subway underground, subway underground',
# 'subway elevated, subway elevated',
# 'subway ground-level, subway ground-level',
# 'tram / other, tram',
# 'roads, highway',
# 'rails, standard rail',
# 'rails, electrified rail',
# 'rails, high speed rail',
# 'rails, tram',
# 'rails, rail bridge low',
# 'rails, rail bridge, average',
# 'rails, rail tunnel, average',
# 'roads, road bridge, average',
# 'roads, road tunnel, average',
# 'roads, expressway',
# 'roads, ordinary highway',
# 'roads, urban road',
# 'urban rails, subway lines',
# 'urban rails, subway station',
# 'pipelines, sewage pipelines',
# 'pipelines, water supply pipelines',
# 'pipelines, nature gas pipelines',
# 'pipelines, coal gas pipelines',
# 'pipelines, liquefied petroleum gas (lpg) pipelines',
# 'pipelines, heat supply pipelines',
# 'others, street lamps',
# 'others, telecommunications',
# 'roads, secondary road',
# 'roads, pipes',
# 'roads, primary road upgrade',
# 'roads, primary road widening',
# 'roads, highway, backfill',
# 'roads, highway, baseline, granular sub-base course',
# 'roads, highway, baseline, unbound base course',
# 'roads, highway, baseline, 4% bitument asphalt base course',
# 'roads, highway, baseline, 4% bitumen asphalt binder course',
# 'roads, highway, baseline, 4.5% bitumen asphalt wearing course',
# 'roads, highway, 80% rcw, unbound base course',
# 'roads, highway, 25% sub-base, 80% rcw u-base, granular sub base course',
# 'roads, highway, 25% sub-base, 80% rcw u-base, unbound base course',
# 'roads, highway,10% rap, asphalt base course',
# 'roads, highway,10% rap, asphalt binder course',
# 'roads, highway,10% rap, asphalt wearing course',
# 'roads, highway,15% rap, asphalt base course',
# 'roads, highway,15% rap, asphalt binder course',
# 'roads, highway,15% rap, asphalt wearing course',
# 'roads, highway,25% rap a-base, 15% rap binder & wearing, asphalt base course',
# 'roads, highway,25% rap a-base, 15% rap binder & wearing, asphalt binder course',
# 'roads, highway,25% rap a-base, 15% rap binder & wearing, asphalt wearing course',
# 'roads, highway,virgin wma & virgin aggregates, granular sub-base course',
# 'roads, highway,virgin wma & virgin aggregates, unbound base course',
# 'roads, highway,virgin wma & virgin aggregates, asphalt wearing course',
# 'roads, highway,virgin wma & virgin aggregates, asphalt base course',
# 'roads, highway,virgin wma & virgin aggregates, asphalt binder course',
# 'roads, highway,25% rcw sub-base, 80% rcw u-base, 25% wma rap a-base, 15% wma rap binder & wearing, granular sub-base course',
# 'roads, highway,25% rcw sub-base, 80% rcw u-base, 25% wma rap a-base, 15% wma rap binder & wearing, unbound base course',
# 'roads, highway,25% rcw sub-base, 80% rcw u-base, 25% wma rap a-base, 15% wma rap binder & wearing, asphalt wearing course',
# 'roads, highway,25% rcw sub-base, 80% rcw u-base, 25% wma rap a-base, 15% wma rap binder & wearing, asphalt base course',
# 'roads, highway,25% rcw sub-base, 80% rcw u-base, 25% wma rap a-base, 15% wma rap binder & wearing, asphalt binder course',
# 'roads, highway, concrete works, baseline',
# 'roads, highway, concrete works, alternate/65% ggbfs case',
# 'waterworks, concrete consumption for waterworks',
# 'building sublayers, cement consumption = cement production + cement import - cement export',
# 'roads, road, expressway',
# 'roads, road, class i',
# 'roads, road, class ii',
# 'roads, road, class iii-iv',
# 'roads, road, urban road',
# 'roads, road, rural road',
# 'railway, high-speed railway',
# 'railway, general speed railway',
# 'rail transit, light rail',
# 'rail transit, subway',
# 'pipeline, tap pipe',
# 'pipeline, sewer pipe',
# 'park, park and green space area',
# 'high-speed rail, rail, ballasted track',
# 'high-speed rail, rail, non-ballasted track',
# 'high-speed rail, bridge',
# 'high-speed rail, tunnel',
# 'high-speed rail, subgrade',
# 'high-speed rail, subgrade (reinforced)',
# 'high-speed rail, others',
# 'various infrastructure, motorway',
# 'various infrastructure, primary',
# 'various infrastructure, secondary',
# 'various infrastructure, tertiary',
# 'various infrastructure, other',
# 'various infrastructure, gravel',
# 'various infrastructure, motorway on bridge',
# 'various infrastructure, motorway bridge',
# 'various infrastructure, all other roads on bridge',
# 'various infrastructure, roadbridge',
# 'various infrastructure, road tunnel',
# 'various infrastructure, airport runway',
# 'various infrastructure, railway',
# 'various infrastructure, tram',
# 'various infrastructure, subway underground',
# 'various infrastructure, subway bridge',
# 'various infrastructure, subway surface',
# 'various infrastructure, all other tracks',
# 'various infrastructure, railway bridge',
# 'various infrastructure, railway tunnel',
# 'industrial digital printing press',
# 'US traditional vehicle engine',
# 'Heavy-duty and off-road (HDOR) equipment parts',
# 'production printer',
# 'Printing Press #1',
# 'Printing Press #2',
# 'Vehicle engine',
# 'Vehicle Alternator',
# 'Vehicle Starter',
# 'HDOR Engine',
# 'HDOR Alternator',
# 'HDOR Turbocharger',
# 'Box-type Al Die Casting for automotive industry',
# 'Structural type Al Die Casting for automotive industry',
# 'Printer (OEM new)',
# 'Printer',
# 'US industrial digital printing press (#1) (OEM new)',
# 'US industrial digital printing press (#1)',
# 'US industrial digital printing press (#2) (OEM new)',
# 'US industrial digital printing press (#2)',
# 'US vehicle alternator (OEM new)',
# 'US vehicle alternator',
# 'US vehicle starter motor (OEM new)',
# 'US vehicle starter motor',
# 'US traditional vehicle engine (OEM new)',
# 'US traditional vehicle engine',
# 'US lightweight vehicle engine (OEM new)',
# 'US lightweight vehicle engine',
# 'US HDOR engine (OEM new)',
# 'US HDOR engine',
# 'US HDOR alternator (OEM new)',
# 'US HDOR alternator',
# 'US HDOR turbocharger (OEM new)',
# 'US HDOR turbocharger',
# 'industrial digital printers',
# 'vehicle parts',
# 'Heavy-duty and off-road (HDOR) equipment parts',
# 'steel',
# 'stainless steel',
# 'cast iron',
# 'copper',
# 'aluminum',
# 'brass',
# 'printed circuit board',
# 'Fabricated metal products, except machinery and equipment (28)',
# 'Machinery and equipment n.e.c. (29)',
# 'Office machinery and computers (30)',
# 'Electrical machinery and apparatus n.e.c. (31)',
# 'Radio, television and communication equipment and apparatus (32)',
# 'Medical, precision and optical instruments, watches and clocks (33)',
# 'Box type Aluminium Die Casting',
# 'Structural Type Aluminium Die casting',
# 'Refrigeration and A/C compressor, 15 kW',
# 'Mining Machinery',
# 'Boom cylinder for mining machinery',
# 'Travel device for mining machinery',
# 'Hydraulic pump for mining machinery',
# 'Machine tool',
# 'Loading machine',
# 'Milling Machine Tool, low level of automation',
# 'Milling Machine Tool, high level of automation',
# 'Generation - Hydro (run-of-river)',
# 'Generation - Hydro (storage)',
# 'Generation - Geothermal',
# 'Generation - Wind Onshore',
# 'Generation - Wind Offshore',
# 'Generation - PV (rooftop)',
# 'Generation - PV (ground-mntd.)',
# 'Generation - CSP',
# 'Generation - Bioenergy',
# 'Generation - Coal',
# 'Generation - Gas',
# 'Generation - Oil',
# 'Generation - Nuclear',
# 'Transmission - HV lines - underground',
# 'Transmission - HV lines - overhead',
# 'Transmission - MV lines - overhead',
# 'Transmission - MV lines - underground',
# 'Transmission - LV lines - underground',
# 'Transmission - LV lines - overhead',
# 'Generation - PV',
# 'Generation - Hydro',
# 'Generation - Coal CCS',
# 'Generation - Gas CCS',
# 'Generation - Biomass',
# 'Generation - Biomass CCS',
# 'solar PV',
# 'solar PV residential',
# 'CSP',
# 'Wind onshore',
# 'Wind offshore',
# 'Wave energy',
# 'Auxiliary grid-equipment',
# 'Grid - Lines - HV - Overhead',
# 'Grid - Lines - HV - Underground',
# 'Grid - Lines - MV - Overhead',
# 'Grid - Lines - MV - Underground',
# 'Grid - Lines - HV',
# 'Grid - Lines - MV',
# 'Grid - Lines - LV',
# 'gaswork gas pipelines',
# 'natural gas supply pipelines',
# 'liquefied petroleum gas pipelines',
# 'electricity generation from hydropower station',
# 'thermal power',
# 'electricity generation from wind turbines',
# 'electricity transmission_500kv',
# 'electricity transmission_330kv',
# 'electricity transmission_220kv',
# 'electricity transmission_110kv',
# 'electricity transmission_35kv',
# 'cables',
# 'electricity transformer_500kv',
# 'electricity transformer_330kv',
# 'electricitytransformer_220kv',
# 'electricity transformer_110kv',
# 'electricity transformer_35kv',
# 'Grid (all elements)',
# 'Grid - Transformers',
# 'Grid - Lines',
# 'Grid - Transformers (HV)',
# 'Grid - Lines (Underground)',
# 'Grid - Lines (Aboveground)',
# 'Generation - Solar PV',
# 'Generation - Wind',
# 'Generation - Other Renewables',
# 'Generation - Fossil Fuel Based',
# 'Storage - Pumped Hydro Storage',
# 'Storage - Flywheel',
# 'Storage - Compressed air',
# 'Storage - Hydrogen Fuel Cells',
# 'Storage - Batteries - NiMH',
# 'Storage - Batteries - Lead Acid',
# 'Storage - Batteries - LMO',
# 'Storage - Batteries - NMC',
# 'Storage - Batteries - NCA',
# 'Storage - Batteries - LFP',
# 'Storage - Batteries - LTO',
# 'Storage - Batteries - Zinc-Bromide',
# 'Storage - Batteries - Vanadium Redox',
# 'Storage - Batteries - Sodium Sulfur',
# 'Storage - Batteries - ZEBRA',
# 'Storage - Batteries - Lithium Sulfur',
# 'Storage - Batteries - Lithium Ceramic',
# 'Storage - Batteries - Lithium-air',
# 'Grid - Equipment - Circuit breaker',
# 'Grid - Equipment - Transformer',
# 'Grid - Equipment - Power Transformer',
# 'Grid - Equipment - SF6-substation',
# 'Grid - Equipment - Electrocmechanic protection',
# 'Grid - Lines - Aboveground',
# 'Grid - Lines - Cables',
# 'Grid - Equipment - Towers',
# 'Grid - Equipment - Wood poles',
# 'single-family detached house, residential building',
# 'multifamily house, residential building',
# 'manufactured housing, residential building',
# 'urban households',
# 'rural households',
# 'total urban residential floorspace',
# 'total rural residential floorspace',
# 'total urban non-residential floorspace',
# 'total rural non-residential floorspace',
# 'urban residential buildings floor space',
# 'rural residential buildings floor space',
# 'commercial building',
# 'industrial building',
# 'residential building',
# 'NonRes',
# 'Service buldings - hospitals and other health',
# 'Service buldings - hotels and restaurants',
# 'Service buldings - sports and recreation',
# 'Service buldings - shops',
# 'Service buldings - Offices (Offices, Schools/Universities, Museums etc)',
# 'service building',
# 'single-family house, residential building',
# 'Wholesale & trade, service sector',
# 'Offices (all), service sector',
# 'Private offices, service sector',
# 'Public offices, service sector',
# 'Hotel & restaurent, service sector',
# 'Health, service sector',
# 'Education, service sector',
# 'Other, service sector',
# 'Total stock of dwellings, residential building',
# 'Stock of dwellings (permanently occupied), residential building',
# 'Stock of multifamily dwellings (permanently occupied), residential building',
# 'Stock of single family dwellings (permanently occupied), residential building',
# 'Floor area of dwellings (average), residential building',
# 'Floor area of single family dwellings, residential building',
# 'Floor area of multifamily dwellings, residential building',
# 'Floor area of services, service building',
# 'Floor area of hotels restaurants, service building',
# 'Floor area of health, service building',
# 'Floor area of education research, service building',
# 'Floor area of public and private offices, service building',
# 'Floor area of public offices and administrations, service building',
# 'Floor area of private offices, service building',
# 'Floor area of trade, service building',
# 'rural detached building',
# 'rural semi-detached building',
# 'rural high-rise building',
# 'urban detached building',
# 'urban semi-detached building',
# 'urban appartments building',
# 'urban high-rise building',
# 'commercial office building',
# 'commercial retail building',
# 'commercial hotels building',
# 'commercial govern building',
# 'office floor area',
# 'commercial floor area',
# 'health floor area',
# 'other_nonresidential floor area',
# 'single-family floor area',
# 'residential tower floor area',
# 'education floor area',
# 'informal floor area',
# 'hotels_restaurants floor area',
# 'multifamily floor area',
# 'Single family- Terraced houses, Residential sector',
# 'Multifamily houses, Residential sector',
# 'Appartment blocks, Residential sector',
# 'Offices, Service sector',
# 'Trade, Service sector',
# 'Hotels and Restaurants, Service sector',
# 'Other non-residential buildings, Service sector',
# 'Apartment blocks, Residential sector',
# 'GW Insulation',
# 'Exterior coating',
# 'Stone',
# 'Wood frame',
# 'Shuttered concrete',
# 'Concrete blocs',
# 'Aerated concrete',
# 'Multi cell bricks',
# 'Plaster board',
# 'Outside frames',
# 'Roof covering',
# 'Foundations',
# 'Beams and wall ties',
# 'Plumbing',
# 'Rain water evacuation',
# 'Residential building (not including the rural house)',
# 'non-residential building (not including the rural house)',
# 'rural house',
# 'Urban Detached building',
# 'Urban Semi-detached building',
# 'Urban Appartments building',
# 'Urban High-rise building',
# 'Rural Detached building',
# 'Rural Semi-detached building',
# 'Rural Appartments building',
# 'Rural High-rise building']

# for m in range(678,678):
#     cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(83,CM83New[m]))

# Fix class. 91:
#cur.execute("UPDATE classification_items SET attribute2_oto = 'Nickel-cadmium electric accumulators' WHERE attribute2_oto = 'Nickel-cadmium' AND classification_id = 91")
#cur.execute("UPDATE classification_items SET attribute2_oto = 'Nickel-iron electric accumulators' WHERE attribute2_oto = 'Nickel-iron' AND classification_id = 91")
    
# Add to class. 7:
# NewPr=['audio equipment',
# 'rice cooker',
# 'microscope',
# 'heating appliances',
# 'Hi-Fi stereo system',
# 'television and video appliances',
# 'machinery',
# 'other electronic appliances',
# 'other electrothermal cooking appliances',
# 'other electric appliances',
# 'other video equipment',
# 'TV (except for LCD)',
# 'transport equipment',
# 'video cameras',
# 'X-ray systems']    
# for m in range(0,15):
#     cur.execute("INSERT INTO classification_items (classification_id, attribute1_oto) VALUES (%s,%s)",(7,NewPr[m]))

# add and fix regions
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Serbia (incl. Kosovo)', attribute4_oto = 10031 WHERE attribute1_oto = 'reserved_14' AND classification_id = 2")
# cur.execute("UPDATE classification_items SET attribute4_oto = 10029 WHERE attribute2_oto = 10029 AND classification_id = 2")
# cur.execute("UPDATE classification_items SET attribute2_oto = NULL WHERE attribute2_oto = 10029 AND classification_id = 2")
# cur.execute("UPDATE classification_items SET attribute4_oto = 10030 WHERE attribute2_oto = 10030 AND classification_id = 2")
# cur.execute("UPDATE classification_items SET attribute2_oto = NULL WHERE attribute2_oto = 10030 AND classification_id = 2")

# delete redundant and mis-spelled product labels:
#cur.execute("DELETE from classification_items WHERE id = 106978 AND classification_id = 7")    
#cur.execute("DELETE from classification_items WHERE id = 1430 AND classification_id = 7")    
#cur.execute("DELETE from classification_items WHERE id = 107058 AND classification_id = 7")    
#cur.execute("DELETE from classification_items WHERE id = 1432 AND classification_id = 7")    
#cur.execute("DELETE from classification_items WHERE id = 1354 AND classification_id = 7")    

# Add 5 more RECC regions to class. 89:
# cur.execute("INSERT INTO classification_items (classification_id,description,reference,attribute1_oto,attribute2_oto,attribute5_anc) VALUES (%s,%s,%s,%s,%s,%s)",(89,'https://github.com/iiasa/circomod-workflow/blob/main/definitions/region/RECC_2.6.yaml','https://github.com/iiasa/circomod-workflow/blob/main/mappings/RECC_2.6.yaml','RECC 2.6|USA','RECC 2.6|R32USA','R32USA'))
# cur.execute("INSERT INTO classification_items (classification_id,description,reference,attribute1_oto,attribute2_oto,attribute5_anc) VALUES (%s,%s,%s,%s,%s,%s)",(89,'https://github.com/iiasa/circomod-workflow/blob/main/definitions/region/RECC_2.6.yaml','https://github.com/iiasa/circomod-workflow/blob/main/mappings/RECC_2.6.yaml','RECC 2.6|Japan','RECC 2.6|R32JPN','R32JPN'))
# cur.execute("INSERT INTO classification_items (classification_id,description,reference,attribute1_oto,attribute2_oto,attribute5_anc) VALUES (%s,%s,%s,%s,%s,%s)",(89,'https://github.com/iiasa/circomod-workflow/blob/main/definitions/region/RECC_2.6.yaml','https://github.com/iiasa/circomod-workflow/blob/main/mappings/RECC_2.6.yaml','RECC 2.6|Canada','RECC 2.6|R32CAN','R32CAN'))
# cur.execute("INSERT INTO classification_items (classification_id,description,reference,attribute1_oto,attribute2_oto,attribute5_anc) VALUES (%s,%s,%s,%s,%s,%s)",(89,'https://github.com/iiasa/circomod-workflow/blob/main/definitions/region/RECC_2.6.yaml','https://github.com/iiasa/circomod-workflow/blob/main/mappings/RECC_2.6.yaml','RECC 2.6|China','RECC 2.6|R32CHN','R32CHN'))
# cur.execute("INSERT INTO classification_items (classification_id,description,reference,attribute1_oto,attribute2_oto,attribute5_anc) VALUES (%s,%s,%s,%s,%s,%s)",(89,'https://github.com/iiasa/circomod-workflow/blob/main/definitions/region/RECC_2.6.yaml','https://github.com/iiasa/circomod-workflow/blob/main/mappings/RECC_2.6.yaml','RECC 2.6|India','RECC 2.6|R32IND','R32IND'))

# add new layer to class. 20:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Power generation capacity' WHERE attribute1_oto = 'reserved_27' AND classification_id = 20")  

# add to class. 18:
#cur.execute("INSERT INTO classification_items (classification_id,description,attribute1_oto) VALUES (%s,%s,%s)",(18,'ore, non-metallic mineral, harvested biomass, extracted fossil fuel','raw material'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(18,'refined metal'))

# EnCList =['bagasse (cane stalks)',
# 'chaff (seed casings)',
# 'animal dung, manure',
# 'dried plants',
# 'wood fuel',
# 'charcoal',
# 'uranium 235',
# 'fusion fuel (2H->3H)',
# 'coal',
# 'crude oil',
# 'ethane',
# 'methane',
# 'hydrogen',
# 'pyrolysis oil',
# 'methanol',
# 'ethanol',
# 'ecalene',
# 'butanol',
# 'fat',
# 'biodiesel',
# 'sunflower oil',
# 'castor oil',
# 'olive oil']

# for m in range(0,23):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =10"
#     cur.execute(SQL,(EnCList[m],'reserved_'+str(m+8)))

# add news process scopes to class. 6:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'product system of a given commodity, primary production from ore' WHERE attribute1_oto = 'reserved_66' AND classification_id = 6")  
#cur.execute("UPDATE classification_items SET attribute1_oto = 'product system of a given commodity, secondary production from scrap' WHERE attribute1_oto = 'reserved_67' AND classification_id = 6")  

# add to 11:
#cur.execute("UPDATE classification_items SET attribute1_oto = 'rural and urban regions' WHERE attribute1_oto = 'reserved_29' AND classification_id = 11")  
#cur.execute("UPDATE classification_items SET attribute1_oto = 'urban regions' WHERE attribute1_oto = 'reserved_30' AND classification_id = 11")  
#cur.execute("UPDATE classification_items SET attribute1_oto = 'rural regions' WHERE attribute1_oto = 'reserved_31' AND classification_id = 11")  

# add to 7:
# cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(7,'clothes dryer'))
# cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(7,'other musical instruments'))
# cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(7,'pianos'))
# cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(7,'stereo equipment'))
# cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(7,'water heater'))

# add to 14:
#cur.execute("UPDATE classification_items SET attribute1_oto = '2003-2015' WHERE attribute1_oto = 'reserved_72' AND classification_id = 14")  
#cur.execute("UPDATE classification_items SET attribute1_oto = '2004-2010' WHERE attribute1_oto = 'reserved_73' AND classification_id = 14")  
#cur.execute("UPDATE classification_items SET attribute1_oto = '2009-2013' WHERE attribute1_oto = 'reserved_74' AND classification_id = 14")  

# add to 1:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(1,'all metals'))

# add to 7:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(7,'feature phone'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(7,'smartphone'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(7,'multimedia phone'))

# add to 90:
# Komps = ['screen',
# 'camera',
# 'cameras and speakers',
# 'electronic components',
# 'metal parts: mounts, screws',
# 'plastic parts: housing components, cases, enclosures, covers',
# 'displays',
# 'entire device, without battery']

# for mk in range(0,8):
#     cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(90,Komps[mk]))

# update 1
#cur.execute("UPDATE classification_items SET attribute4_oto = 'All metals' WHERE attribute1_oto = 'all metals' AND classification_id = 1")  

# add to 4:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(4,'calcium'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(4,'barium'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(4,'other non-metallic minerals'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(4,'PET & HDPE'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(4,'excavated material'))

# tranges =[1983,1993,1996,2000,'1978-2020','2000-2020','before 1999','2011-2020','ca. 1995']
# for mk in range(0,9):
#     SQL = "UPDATE classification_items SET attribute1_oto = %s WHERE attribute1_oto = %s AND classification_id =14"
#     cur.execute(SQL,(tranges[mk],'reserved_'+str(mk+75)))

# Fix class. 86:	remove all trailing blank spaces for attribute 2+3
# CE_strats = ['R0',
# 'R1',
# 'R2',
# 'R2a',
# 'R2b',
# 'R2c',
# 'R2d',
# 'R2e',
# 'R2f',
# 'R2g',
# 'R2h',
# 'R2i',
# 'R3a',
# 'R3b',
# 'R4',
# 'R5',
# 'R6',
# 'R7',
# 'R8',
# 'R8a',
# 'R8b',
# 'R9']
# for si in range(0,22):
#     cur.execute("SELECT attribute2_oto, attribute3_oto FROM classification_items WHERE classification_id = 86 AND attribute1_oto =%s",(CE_strats[si]))
#     for row in cur:
#         #print(row)  
#         # fetch and fix labels
#         attr2_new = row[0].replace(u'\xa0', u'')
#         attr3_new = row[1].replace(u'\xa0', u'')
#         # insert new labels
#         cur.execute("UPDATE classification_items SET attribute2_oto = %s WHERE attribute1_oto = %s AND classification_id = 86",(attr2_new,CE_strats[si]))  
#         cur.execute("UPDATE classification_items SET attribute3_oto = %s WHERE attribute1_oto = %s AND classification_id = 86",(attr3_new,CE_strats[si]))  

# add to 6:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(6,'manufacturing of appliances'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(6,'other manufacturing'))

# add to 14:
#cur.execute("UPDATE classification_items SET attribute1_oto = 2060 WHERE attribute1_oto = 'reserved_92' AND classification_id = 14")  

# appl = ['Tablet',
# 'Laptop computer',
# 'Printer, laser color',
# 'CD/DVD player',
# 'appliances',
# 'other products']

# for mk in range(0,6):
#     cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,appl[mk]))

# applm= ['raw material processing of refrigerators',
# 'manufacturing of refrigerators',
# 'raw material processing of clothes washer',
# 'manufacturing of clothes washer',
# 'assembly process of clothes washer',
# 'raw material processing of dish washer',
# 'raw material processing of air conditioner',
# 'manufacturing of air conditioner',
# 'raw material processing (Silver)',
# 'raw material processing (Aluminium)',
# 'raw material processing (Gold)',
# 'raw material processing (Ceramics)',
# 'raw material processing (Copper)',
# 'raw material processing (Epoxy)',
# 'raw material processing (Iron)',
# 'raw material processing (Glass)',
# 'raw material processing (Nickel)',
# 'raw material processing (Lead)',
# 'raw material processing (Palladium)',
# 'raw material processing (Aggregated plastics, excl, PVC)',
# 'raw material processing (Platinum)',
# 'raw material processing (PVC)',
# 'raw material processing (Silicon)',
# 'raw material processing (Tin)',
# 'raw material processing (Stainless steel)',
# 'raw material processing (Steel)',
# 'raw material processing (Zinc)',
# 'raw material processing (Timber e.g. wood, cardboard)',
# 'raw material processing (Paper, packaging)',
# 'production of semiconductor ',
# 'production of circuit board',
# 'manufacturing/assembly of CRT',
# 'assembly of computer',
# 'manufacturing of Vacuum cleaners',
# 'manufacturing of Electric kettle',
# 'manufacturing of Hair Dryer',
# 'manufacturing of Microwave oven',
# 'manufacturing of Washing machine',
# 'manufacturing of Coffee maker',
# 'manufacturing of Cookstove',
# 'manufacturing of Dishwasher',
# 'manufacturing of Dryer',
# 'manufacturing of Refrigerator',
# 'manufacturing of Television',
# 'manufacturing of Tablet',
# 'manufacturing of Laptop computer',
# 'manufacturing of Printer, laser color',
# 'manufacturing of CD/DVD player',
# 'manufacture of washing machine']

# for mk in range(0,49):
#     cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(82,applm[mk]))

# prodx = ['water supply pipelines',
# 'street lamps',
# 'sewage pipelines',
# 'subway lines',
# 'subway station',
# 'pumps',
# 'roads, urban',
# 'pipelines, for heat supply',
# 'expressway',
# 'highway, ordinary',
# 'pipelines, for natural gas',
# 'pipelines, for coal gas',
# 'pipelines, for liquefied petroleum gas (LPG)',
# 'tractors, large and medium-sized',
# 'tractors, mini',
# 'shellers, motorized',
# 'combined harvester',
# 'drainage and irrigation machinery']

# for mk in range(0,18):
#     cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(7,prodx[mk]))

# add to 13:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(13,'office and administrative buildings'))
# add to 90:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(90,'inverter'))
# add to 4:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(4,'polyvinyl fluoride '))
#cur.execute("UPDATE classification_items SET attribute1_oto = 'polyvinyl fluoride' WHERE attribute1_oto = 'polyvinyl fluoride ' AND classification_id = 4")  
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(4,'acrylic foam'))
# add to 20:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(20,'Energy per unit of output'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(20,'Energy per mass or output'))    
#cur.execute("UPDATE classification_items SET attribute1_oto = 'remanufacturing potential of materials or components of end-of-life goods, expressed as mass ratio' WHERE attribute1_oto = 'reserved_28' AND classification_id = 20")  
#cur.execute("UPDATE classification_items SET attribute1_oto = 'recycling potential of materials or components extracted from end-of-life goods, expressed as mass ratio' WHERE attribute1_oto = 'reserved_29' AND classification_id = 20")  
#cur.execute("UPDATE classification_items SET attribute1_oto = 'reuse potential of materials or components extracted from end-of-life goods, expressed as mass ratio' WHERE attribute1_oto = 'reserved_30' AND classification_id = 20")  
#cur.execute("UPDATE classification_items SET attribute1_oto = 'current mid-life repair rate as % of sales' WHERE attribute1_oto = 'reserved_31' AND classification_id = 20")  
#cur.execute("UPDATE classification_items SET attribute1_oto = 'refurbishment potential of materials or components extracted from end-of-life goods, expressed as mass ratio' WHERE attribute1_oto = 'reserved_32' AND classification_id = 20")  
# add to 6:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(6,'recovery'))    
#cur.execute("UPDATE classification_items SET attribute1_oto = 'recycling' WHERE attribute1_oto = 'recyling' AND classification_id = 6")  
# add to 83:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,'Generation - PV PERC (rooftop)'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,'Major appliances (including refrigerators, washing machines and water heaters)'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,'small appliances (including toasters, hair dryers and electric coffee pots)'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,'Screens, monitors, and equipment containing screens having a surface greater than 100 cm2'))
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,'all materials'))
# add to 14:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(14,'1946-1980'))
#cur.execute("UPDATE classification_items SET attribute1_oto = 1980 WHERE attribute1_oto = 'reserved_95' AND classification_id = 14")  
# add to 86:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto,attribute2_oto,attribute3_oto) VALUES (%s,%s,%s,%s)",(86,'R3','Re-use','R3 Re-use'))


# CEst = ['other: remanufacturing or refurbishment, low potential',
# 'other: remanufacturing or refurbishment, high potential',
# 'other: repair or maintenance, low potential',
# 'other: repair or maintenance, high potential',
# 'other: reuse, low potential',
# 'other: reuse, high potential',
# 'other: remanufacturing, maximum part replacement',
# 'other: new product',
# 'other: remanufacturing, light-weighting',
# 'other: repair, light-weighting',
# 'other: refuse light-weighting',
# 'other: refuse, low potential',
# 'other: refuse, high potential']

# for mk in range(0,13):
#     cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(86,CEst[mk]))

# CLI = ['Coffee machines',
# 'Vacuum cleaners',
# 'Dishwashers',
# 'Washing machines',
# 'household appliances',
# 'TV sets, computer monitors',
# 'All WEEE',
# 'End-of-life PC',
# 'Plastics casing',
# 'Non-ferrous metal',
# 'E-motor',
# 'PCB',
# 'Composite material',
# 'Cable with plug',
# 'Battery/storage battery',
# 'CRT-panel glass',
# 'CRT-clean cone',
# 'Other',
# 'Mineral',
# 'Plastics',
# 'Mother board and hard disk']

# for mk in range(0,21):
#     cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,CLI[mk]))

# Waste1 = ['[WEEE] Manual sorting of plastics from WEEE, informal sector',
# '[WEEE] Manual soritng of plastics from WEEE, formal sector',
# '[Packaging] Treatment of mixed lightweight packaging waste, mechanical recycling',
# '[Packaging] Treatment of mixed lightweight packaging waste, chemical recycling',
# '[Packaging] Sorting of plastic packaging waste',
# '[Packaging] Sorting of paper/cardboard packaging waste',
# '[Packaging] Sorting of waste packaging paperboard',
# '[Packaging] Sorting of waste packaging paper',
# '[Packaging] Sorting of waste tinplate packaging ',
# '[Packaging] Sorting of waste aluminium packaging',
# '[Packaging] Sorting of glass packaging waste',
# '[Packaging] Sorting and shredding of waste wood',
# '[Packaging] Treatment of PET, mechanical recycling',
# '[Packaging] Treatment of HDPE, mechanical recycling',
# '[Packaging] Treatment of LDPE, mechanical recycling',
# '[Packaging] Treatment of PP, mechanical recycling',
# '[Packaging] Treatment of PS, mechanical recycling',
# '[Packaging] Treatment of mixed plastics waste, pyrolisis oil production',
# '[Packaging] Treatment of mixed plastics waste, mechanical recycling',
# '[Packaging] Ethylene production from purified pyrolisis Oil',
# '[Packaging] Energy recovery of mixed plastic waste, 100% incineration',
# '[Packaging] Energy recovery of mixed plastic waste, 100% refuse-derived fuel',
# '[Packaging] Energy recovery of mixed plastic waste, 30% incineration, 70% refuse-derived fuel',
# '[ELV] Shredding of used glider, electric scooter',
# '[ELV] Treatment of waste car tyres',
# '[ELV] Treatment of waste large vehicle tyres',
# '[Packaging] Sorting of waste wood/MDF',
# '[WEEE] Treatment of WEEE from large appliances',
# '[WEEE] Treatment of WEEE from small appliances',
# '[WEEE] Treatment of electronic scrap from control units, manual dismantling',
# '[WEEE] Treatment of WEEE used Printed wiring boards',
# '[WEEE] Treatment of WEEE waste cables',
# '[WEEE] Treatment of WEEE from used fridges and freezers',
# '[WEEE] Sorting and preparation of aluminium scrap',
# '[WEEE] Sorting and preparation of metal scrap',
# '[Packaging] Waste mixed plastics sorting',
# '[Packaging] Sorting and preparation of metal scrap',
# '[WEEE] Treatment of used washing machine, dismantling',
# '[WEEE] Treatment of used A/C unit, dismantling',
# '[WEEE] Treatment of used refrigerator, dismantling',
# '[WEEE] Treatment of used TV, dismantling',
# '[WEEE] Treatment of used photovoltaic module',
# '[WEEE] Treatment of waste Printed Circuit Board (PCB)',
# '[ELV] Treatment of automotive shredder residue (ASR), metals recovery',
# '[ELV] Treatment of automotive shredder residue (ASR), themal treatment and energy recovery',
# '[ELV] Treatment of automotive shredder residue (ASR), advanced material recovery and incineration',
# '[ELV] Treatment of automotive shredder residue (ASR), feedstock recycling',
# '[WEEE] Treatment of WEEE, high grade',
# '[ELV] Treatment of used vehicle, dismantling and shredding',
# '[ELV] Treatment of used vehicle, manual dismantling of ECU, shredding',
# '[ELV] Treatment of diesel engine motor end-of-life vehicle (ELV)',
# '[ELV] Treatment of automotive plastic waste (APW), waste to energy in MSWI plants',
# '[ELV] Treatment of automotive plastic waste (APW), waste to energy in RDF plant',
# '[ELV] Treatment of automotive plastic waste (APW), chemical recycling',
# '[WEEE] Treatment of mixed plastics from WEEE, catalytic pyrolisis',
# '[ELV] Treatment of mixed plastics from ELV, catalytic pyrolisis',
# '[ELV] Treatment of ELV Hulk, machine-based dismantling',
# '[ELV] Treatment of ELV hulk, shredding',
# '[ELV] Treatmeant of ELV, dismantling',
# '[ELV] Treatment of waste passenger tires, pyrolisis and deep processing',
# '[ELV] Treatment of waste passenger tires, conventional pyrolisis',
# '[ELV] Treatment of waste passenger tires, ambient grinding',
# '[ELV] Treatment of waste passenger tires, dynamic devulcanization',
# '[ELV] Treatment of waste passenger tires, pyrolisis',
# '[ELV] Treatment of waste passenger tires, informal tire oil extraction',
# 'pyrometallurgical treatment of used Li-ion battery',
# 'treatment of non-Fe-Co-metals, from pyrometallurgical treatment of used Li-ion battery',
# 'hydrometallurgical treatment of used Li-ion battery',
# 'treatment of non-Fe-Co-metals, from hydrometallurgical treatment of used Li-ion battery',
# 'treatment of spent lead-acid batteries',
# 'Treatment of used Ni-Cd batteries, pyrometallurgy',
# 'Treatment of used Ni-Cd batteries, hydrometallurgy',
# 'Treatment of used Li-Ion battery (LFP), hydrometallurgy',
# 'Treatment of used Li-Ion battery (NCM), hydrometallurgy',
# 'Treatment of used Li-Ion battery (LFP), direct recycling A',
# 'Treatment of used Li-Ion battery (LFP), direct recycling B',
# 'Treatment of used Li-Ion battery (NCM), direct recycling B',
# 'Treatment of used Li-Ion battery (LFP), direct recycling C',
# 'Treatment of used Li-Ion battery (NCM), direct recycling C']

# for mk in range(0,79):
#     try:
#         cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(82,Waste1[mk]))
#     except:
#         None
        
# Waste2 = ['Manual sorting of one tonne of plastics from WEEE, informal sector',
# 'waste plastic, consumer electronics, sorted',
# 'scrap steel',
# 'waste plastic',
# 'waste polyurethane foam',
# 'electricity, low voltage',
# 'formic acid',
# 'liquefied petroleum gas',
# 'sodium chloride powder',
# 'sodium hydroxide NaOH',
# 'waste plastic, consumer electronics, unsorted',
# 'water',
# 'carbon dioxide, fossil',
# 'carbon monoxide, fossil',
# 'nitrogen oxides',
# 'Particulate Matter, > 10 um ',
# 'Particulate Matter, > 2.5 um and < 10um',
# 'Sulfur dioxide',
# 'BOD5, Biological Oxygen Demand ',
# 'COD, Chemical Oxygen Demand',
# 'Chloride',
# 'DOC, Dissolved Organic Carbon',
# 'Dissolved solids',
# 'Nitrogen',
# 'Oils, non-fossil',
# 'Phosphorus',
# 'Sodium I',
# 'TOC, Total Organic Carbon',
# 'Water ',
# 'Manual sorting of one tonne of plastics from WEEE, formal sector',
# 'Treatment of one tonne of mixed lightweight packaging waste',
# 'Mixed lightweight packaging waste',
# 'Cumulative energy demand',
# 'Re-granulate plastics',
# 'Waste',
# 'Waste plastics',
# 'Ethylene',
# 'Sorting of 1kg of plastic packaging waste',
# 'Electricity',
# 'Diesel',
# 'Lubricants',
# 'Plastic waste, generic, sorted',
# 'Unsorted waste packaging plastics',
# 'Waste (rejected), after sorting',
# 'Paper/cardboard from packaging waste, sorted',
# 'Paper/cardboard packaging waste, unsorted',
# 'Sorting of 1kg of waste packaging paperboard',
# 'waste paperboard, sorted',
# 'Electricity, medium voltage',
# 'heat',
# 'lubricating oil',
# 'steel, alloyed',
# 'waste paperboard, unsorted',
# 'scrap steel, to recycling',
# 'waste graphical paper',
# 'waste paperboard',
# 'waste plastic, mixture',
# 'waste textile, soiled',
# 'waste wood, untreated',
# 'Waste paper, sorted',
# 'waste paper, unsorted',
# 'tinplate scrap, sorted',
# 'diesel, burned in building machine',
# 'tinplate, in mixed metal scrap',
# 'municipal solid waste',
# 'aluminium scrap, sorted',
# 'used aluminium packaging',
# 'Glass from packaging waste, sorted',
# 'Electricity consumption sorting facility',
# 'Lubricants consumption sorting facility',
# 'Glass packaging waste, unsorted',
# 'Wood chips, post consumer wood',
# 'Waste wood, post consumer',
# 'steel, low-alloyed, hot rolled',
# 'Recycled plastic, at plant',
# 'NaOH',
# 'Wastewater',
# 'Waste PET, sorted',
# 'Waste residues',
# 'Waste HDPE, sorted',
# 'Waste rejected, after sorting',
# 'Waste LDPE, sorted',
# 'Waste PP, sorted',
# 'Waste PS, sorted',
# 'Purified pyrolisis Oil',
# 'Mixed plastic waste',
# 'Natural gas',
# 'Char',
# 'Heavy vaccum residue',
# 'Treatment of mixed plastic wasted, via mechanical recycling',
# 'Plastic granulate',
# 'Residual waste, to incineration',
# 'Sodium hydroxide',
# 'Other fuels',
# 'Energy recovery of one tonne of mixed plastic waste, 100% incineration',
# 'Carbon dioxide',
# 'Steam',
# 'Energy recovery of one tonne of mixed plastic waste, 100% refuse-derived fuel',
# 'Energy recovery of one tonne of mixed plastic waste, 30% incineration, 70% refuse-derived fuel',
# 'Shredding of used glider, electric scooter',
# 'used glider, electric scooter',
# 'aluminium scrap, post-consumer',
# 'iron scrap, unsorted',
# 'residue from shredder fraction',
# 'copper scrap, medium grade',
# 'Treatment of one tonne of waste tyres',
# 'Waste tyres',
# 'Steel, to steel production',
# 'Rubber granulate <3mm',
# 'Rubber crumb <20mm',
# 'Steel, to disposal',
# 'Rubber, to disposal',
# 'Fibre, to disposal',
# 'Sorting of one tonne of waste wood/MDF (furniture)',
# 'Sorted waste MDF, for recycling',
# 'Waste wood/MDF',
# 'Heat, natural gas',
# 'Contaminants, to landfill',
# 'Wastewater, to treatment',
# 'Treatment of one tonne of WEEE from large appliances',
# 'Waste EEE from a large appliance',
# 'Ferrous metals to recycling',
# 'Non-ferrous metals to recycling',
# 'Other plastic non-packaging to recycling',
# 'Sorted Printed wiring board (PWB), to shredding',
# 'Others non-recyclable',
# 'Waste non-recyclable',
# 'Treatment of one tonne of WEEE from small appliances',
# 'Waste EEE from a small appliance',
# 'Sorted Batteries, to treatment',
# 'Manual dismantling of one tonne of electronics scrap from control units',
# 'electronics scrap from control units',
# 'used cable from EEE',
# 'waste PWB',
# 'waste plastic, industrial electronics',
# 'Treatment of one tonne of used PWB',
# 'Electronics scrap',
# 'Treatment of one tonne of waste cable',
# 'Waste, mostly plastics, non recyclable',
# 'Treatment of one tonne of WEEE from used fridges and freezers',
# 'Used fridges and freezers',
# 'Plastics, to recycling',
# 'Glass, to recycling',
# 'Sorting and preparation of one tonne of aluminium scrap',
# 'Unsorted aluminium scrap',
# 'Aluminium scrap, sorted, for recycling',
# 'Heat, heavy fuel oil',
# 'Ferro-silicon',
# 'Light fuel oil',
# 'Hydraulic oil (lubricant)',
# 'Detergent',
# 'Lime',
# 'Additives',
# 'Oil, to incineration',
# 'Hazardous waste',
# 'Inert waste',
# 'Filter dust, to disposal',
# 'Sorting and preparation of one tonne of metallic scrap',
# 'Unsorted metal scrap',
# 'Steel scrap, sorted, to EAF for recycling',
# 'Scrap metal, to diposal',
# 'Sorting of one tonne of mixed plastics',
# 'Waste mixed plastics',
# 'Waste PET, sorted, to recycling',
# 'Waste HDPE, sorted, to recycling',
# 'Waste PVC, sorted, to recycling',
# 'Waste PP, sorted, to recycling',
# 'Waste, non-recyclable',
# 'Sorting and preparation of one tonne of mixed cans',
# 'Mixed cans, unsorted',
# 'Steel reject, to re-processing',
# 'Dismantling of one tonne of used washing machine',
# 'Used Washing Machine',
# 'LPG',
# 'Ferrous materials, to smelting for recycling',
# 'Copper scrap, middle grade',
# 'Al, to smelting for recycling',
# 'Plastics, for recycling',
# 'Pb, for recycling',
# 'Zn, for recycling',
# 'Dismantling of one tonne of used A/C',
# 'Used A/C',
# 'Dismantling of one tonne of used refrigerator',
# 'Used Refrigerator',
# 'Dismantling of one tonne of used TV',
# 'Used TV',
# 'Glass, for recycling',
# 'Treatment of one tonne of a used refrigerator',
# 'Cr',
# 'Mn',
# 'Ni',
# 'Treatment of one tonne of PV modules',
# 'Used PV module',
# 'HNO3',
# 'CA(OH)2',
# 'Aluminium, to recycling',
# 'Steel, to recycling',
# 'Copper, to recycling',
# 'Silver, to recycling',
# 'Silicon, metallurgical grade',
# 'Thermal energy',
# 'Contaminated glass',
# 'Fly ash',
# 'Liquid waste',
# 'Sludge',
# 'NOx',
# 'Treatment of one tonne of PCB',
# 'waste PCB',
# 'tin scrap',
# 'iron scrap',
# 'lead scrap',
# 'nickel scrap',
# 'aluminium scrap',
# 'zinc scrap',
# 'silver scrap',
# 'gold scrap',
# 'resin',
# 'glass fiber',
# 'Treatment of one tonne of ASR',
# 'ASR',
# 'Scrap metals, to recycling',
# 'Waste to landfill',
# 'thermal energy, recovered',
# 'electricity, recovered',
# 'oxygen',
# 'cooling water',
# 'zinc',
# 'NaCl',
# 'sulphur',
# 'waste, to landfill',
# 'hydrogen gas',
# 'methanol',
# 'Treatment of one tonne of WEEE, high grade',
# 'WEEE, high grade',
# 'scrap aluminium',
# 'scrap iron and magnetic steel',
# 'copper and precious metals',
# 'Waste special treatment substances',
# 'Fluff and residual waste',
# 'Dismantling and shredding of one tonne of used vehicle without engine and battery',
# 'Used vehicle without engine and battery',
# 'Fuel',
# 'Magnetite',
# 'Salted solution',
# 'Copper scrap',
# 'Sand',
# 'Plastics scrap',
# 'Carbon black',
# 'Wiring board',
# 'Dismantling and shredding of one tonne of used vehicle without engine and battery, removing ECU',
# 'Treatment of one tonne of an ICE vehicle',
# 'Used vehicle',
# 'Acetylen',
# 'Lead acid battery, to recycling',
# 'Air conditioner refrigerant, to recycling',
# 'Three way catalyst, to recycling',
# 'Used engine, for remanufacturing',
# 'Scrap aluminium, to recycling',
# 'Scrap copper, to recycling',
# 'Scrap zinc, to recycling',
# 'Scrap plastic, to recycling',
# 'Scrap glass, to recycling',
# 'Scrap tire, to recycling',
# 'Scrap wiring board, to recycling',
# 'Waste oil, to recycling',
# 'Automotive shredder residue',
# 'Waste diesel',
# 'Particulates',
# 'Chemical oxygen demand',
# 'Non-methane hydrocarbon',
# 'Treatment of one tonne of Automotive plastic waste (APW)',
# 'Mixed automotive shredder residue waste',
# 'Scrap ferrous metals, to recycling',
# 'Scrap non-ferrous metals, to recycling',
# 'Processing costs',
# 'Mixed automotive shredder residue',
# 'Ethene',
# 'Propene',
# 'Butadiene',
# 'Pyrolysis gasoline',
# 'Treatment of one tonne of mixed waste plastics from WEEE',
# 'Mixed waste plastics from WEEE',
# 'Catalyst',
# 'Chemical for air pollution control',
# 'Solid waste to landfill',
# 'Unrefined light sweet crude oil',
# 'Treatment of one tonne of mixed waste plastics from ELV',
# 'Mixed waste plastics from ELV',
# 'Dismantling of one tonne of ELV hulk',
# 'ELV Hulk',
# 'Ferrous metals scrap',
# 'H2O Vapour',
# 'CO',
# 'CH2O',
# 'Particulate matter<2.5μm²',
# 'Particulate matter<10μm²',
# 'Polycyclic aromatic hydrocarbons ',
# 'SO2',
# 'Total volatile organic compounds',
# 'Shredding one tonne of ELV hulk',
# 'Ferrous metals scrap, to recycling',
# 'Non-ferrous metals scrap, to recycling',
# 'Mixed waste',
# 'Process water',
# 'NO2',
# 'Particulate matter',
# 'Dismantling of ELV',
# 'Used ELV',
# 'Fluids, to recycling',
# 'Gasoline, to reuse',
# 'Antifreeze fluid, to reuse',
# 'Catalytic convertor',
# 'Aluminium rims, to recycling',
# 'Steel rims, to recycling',
# 'Copper radiators, to recycling',
# 'Aluminium radiators, to recycling',
# 'Batteries, to recycling',
# 'Tires, to recycling',
# 'Starters, to remanufacturing',
# 'Alternators, to remanufacturing',
# 'Air conditoner /compressor, to remanufacturing',
# 'Other parts, direct reuse',
# 'Tires, direct reuse',
# 'Treatment of one tonne of waste passenger tires',
# 'Waste passenger tires',
# 'Cast iron',
# 'Coal',
# 'Steel wire',
# 'Gasoline',
# 'Heavy oil',
# 'Carbon black, refined',
# 'Carbon black, crude',
# 'Fuel oil',
# 'Ferrous metals',
# '60 mesh crumb rubber',
# 'Devulcanized rubber',
# 'CH4',
# 'NMVOC',
# 'H2S',
# 'Dust',
# 'As',
# 'Cd',
# 'Hg',
# 'Pb',
# 'Zn',
# 'Low-quality oil',
# 'pyrometallurgical treatment of 1 kg of used Li-ion battery',
# 'used Li-ion battery',
# 'iron scrap, unsorted, recyclable',
# 'manganese dioxide',
# 'cobalt',
# 'non-Fe-Co-metals',
# 'particulate matter, < 2.5 um',
# 'particulate matter, > 10 um',
# 'sulfate',
# 'treatment of 1 kg non-Fe-Co-metals from pyrometallurgical treatment of used Li-ion batteries',
# 'non-Fe-Co-metals, from pyrometallurgical treatment of used Li-ion battery',
# 'electricity, high voltage',
# 'heat, district or industrial, other than natural gas',
# 'oxygen, liquid',
# 'copper cathode',
# 'chlorine',
# 'copper',
# 'dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin',
# 'fluorine',
# 'hydrometallurgical treatment of 1 kg of used Li-ion battery',
# 'chemical, inorganic',
# 'lime, hydrated, packed',
# 'sulfuric acid',
# 'lithium carbonate',
# 'inert waste, for final disposal',
# 'waste gypsum',
# 'NMVOC, non-methane volatile organic compounds, unspecified origin',
# 'BOD5, Biological Oxygen Demand',
# 'cobalt II',
# 'copper ion',
# 'fluoride',
# 'hydrocarbons, unspecified',
# 'nickel II',
# 'suspended solids, unspecified',
# 'treatment of 1 kg non-Fe-Co-metals from hyrometallurgical treatment of used Li-ion batteries',
# 'non-Fe-Co-metals, from Li-ion battery, hydrometallurgical processing',
# 'ammonia, anhydrous, liquid',
# 'manganese',
# 'treatment of 3499.97 kg spent lead-acid batteries',
# 'spent lead-acid batteries',
# 'antimony',
# 'arsenic',
# 'coke',
# 'scrap iron',
# 'slaked lime',
# 'potassium carbonate',
# 'selenium',
# 'sodium carbonate',
# 'sodium chloride',
# 'sodium nitrate',
# 'sulfur',
# 'tin',
# 'refined lead',
# 'carbon monoxide',
# 'lead',
# 'particulates, unspecified',
# 'plastic mix to recycling',
# 'plastic mix to landfill',
# 'sludge from neutralization',
# 'smelting residues',
# 'treatment of 1 kg spent Ni-Cd batteries, pyrometallurgy',
# 'spent Ni-Cad batteries',
# 'furnace gas',
# 'cadmium (emission to air)',
# 'nickel (emission to air)',
# 'cadmium (emission to water)',
# 'nickel (emission to water)',
# 'cadmium (secondary)',
# 'ferronickel (secondary)',
# 'treatment of 1500 kg spent Ni-Cd batteries, hydrometallurgy',
# 'external cases (~ 95 % steel, ~ 5 % PVC and PA)',
# 'sulphuric acid',
# 'ammonia',
# 'hydrogen peroxide, 30 %',
# 'energy',
# 'nickel, secondary (98-99 % purity)',
# 'cadmium, secondary (98-100 % purity)',
# 'Fe(OH)3 with ~ 3 % coprecipitated Nickel',
# 'insoluble powder (> 53 % Nickel, ca. 40 % Cadmium)',
# 'solid residues of the electrode scrap (> 70 % iron, 20-30 % Nickel)',
# 'treatment of 1 kWh LFP Li-Ion battery',
# 'retired LFP battery',
# 'hydrochloric acid, 30%',
# 'hydrogen peroxide, 7.5%',
# 'sodium hydroxide, 32%',
# 'calcium chloride',
# 'lithium chloride',
# 'hydrogen fluoride',
# 'VOC',
# 'hydrochloric acid mist',
# 'plastic casing scrap',
# 'separator scrap',
# 'waste battery management system',
# 'aluminium, scrap',
# 'waste graphite',
# 'other solid waste',
# 'treatment of 1 kWh NCM Li-Ion battery',
# 'retired NCM battery',
# 'NMP (N-Methyl-2-pyrrolydone)',
# 'decarbonised water',
# 'hydrochloric acid',
# 'hydrogen peroxide',
# 'sodium carbonide',
# 'deionised water',
# 'chromium steel 18/8',
# 'aluminium',
# 'cathode active material',
# 'waste copper',
# 'waste aluminium',
# 'waste printed wiring board',
# 'waste chromium steel 18/8',
# 'waste coolant',
# 'waste fibre glass',
# 'waste steel',
# 'waste PP',
# 'waste PE',
# 'waste PET',
# 'waste sludge',
# 'waste PVDF',
# 'waste water',
# 'nitrogen, liquid',
# 'DMC solvent',
# 'glucose',
# 'cathode materials',
# 'graphite scrap',
# 'aluminium foil scrap',
# 'copper foil scrap',
# 'plastic scrap',
# 'electrolyte scrap',
# 'aluminium case scrap',
# 'lithium hydroxide',
# 'citric acid',
# 'transport (freight rail)',
# 'transport (freight lorry)',
# 'LFP (lithium iron phosphate)',
# 'lithium hexafluorophosphate (LiPF6)',
# 'ethylene carbonate (EC)',
# 'dimethyl carbonate (DMC)',
# 'lithium hydroxide (LiOH)',
# 'chrominium steel 18/8']
        
# for mk in range(0,486):
#     try:
#         cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,Waste2[mk]))
#     except:
#         None

# Add regions to class 2:
# cur.execute("UPDATE classification_items SET attribute1_oto = 'South Asia, nec', attribute4_oto = 10032 WHERE attribute1_oto = 'reserved_15' AND classification_id = 2")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'Southern Africa, nec', attribute4_oto = 10033 WHERE attribute1_oto = 'reserved_16' AND classification_id = 2")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'Central America, nec', attribute4_oto = 10034 WHERE attribute1_oto = 'reserved_17' AND classification_id = 2")
# cur.execute("UPDATE classification_items SET attribute1_oto = 'South America, nec', attribute4_oto = 10035 WHERE attribute1_oto = 'reserved_18' AND classification_id = 2")
#cur.execute("UPDATE classification_items SET attribute1_oto = 'Central Europe', attribute4_oto = 10036 WHERE attribute1_oto = 'reserved_19' AND classification_id = 2")

# AppL = ['urban refrigerator',
# 'urban washing machine',
# 'urban electric fan',
# 'urban air conditioner',
# 'urban water heater',
# 'urban stereo combination',
# 'urban video',
# 'urban camera',
# 'urban other musical instrument',
# 'urban fitness equipment',
# 'urban telephone',
# 'urban mobile phone',
# 'urban piano',
# 'urban dish washer',
# 'urban disinfection cupboard',
# 'urban smoke absorber',
# 'urban microwave oven',
# 'urban TV set',
# 'urban computer',
# 'urban bicycles',
# 'urban sewing machine',
# 'rural refrigerator',
# 'rural washing machine',
# 'rural microwave oven',
# 'rural air conditioner',
# 'rural smoke absorber',
# 'rural water heater',
# 'rural electric fan',
# 'rural computer',
# 'rural TV set',
# 'rural bicycle',
# 'rural sewing machine',
# 'Domestic appliances - Fans',
# 'Domestic appliances - Air-coolers',
# 'Domestic appliances - Air-conditioners',
# 'Domestic appliances - Refridgerators',
# 'Domestic appliances - Microwave',
# 'Domestic appliances - Washing Machine',
# 'Domestic appliances - Tumbler Dryer',
# 'Domestic appliances - Dishwasher',
# 'Domestic appliances - Television',
# 'Domestic appliances - VCR/DVD',
# 'Domestic appliances - Laptops & PCs',
# 'Domestic appliances - Other small appliances',
# 'Radio, television and communication equipment and apparatus, (used in), Agriculture and Food sector',
# 'Radio, television and communication equipment and apparatus, (used in), Extraction & Mining sector',
# 'Radio, television and communication equipment and apparatus, (used in), Other Manufacturing sector',
# 'Radio, television and communication equipment and apparatus, (used in), Machinery sector',
# 'Radio, television and communication equipment and apparatus, (used in), Utility sector',
# 'Radio, television and communication equipment and apparatus, (used in), Construction sector',
# 'Radio, television and communication equipment and apparatus, (used in), Transport sector',
# 'Radio, television and communication equipment and apparatus, (used in), Other Services sector',
# 'Office machinery and computers, (used in), Agriculture and Food sector',
# 'Office machinery and computers, (used in), Extraction & Mining sector',
# 'Office machinery and computers, (used in), Other Manufacturing sector',
# 'Office machinery and computers, (used in), Machinery sector',
# 'Office machinery and computers, (used in), Utility sector',
# 'Office machinery and computers, (used in), Construction sector',
# 'Office machinery and computers, (used in), Transport sector',
# 'Office machinery and computers, (used in), Other Services sector',
# 'Washing machine',
# 'Washing machine, A2041',
# 'Washing machine, A2031',
# 'Washing machine, A2021',
# 'Washing machine, A+++',
# 'Wasching machine, A++',
# 'Washing machine, A+',
# 'Washing machine, A',
# 'Washing machine, B',
# 'Washing machine, C',
# 'Washing machine, D']

# for mk in range(0,71):
#     try:
#         cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,AppL[mk]))
#     except:
#         None

# add to 14:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(14,'1946-1980'))

# add to 86:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(86,'other: maintenance'))
# add to 6:
#cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(6,'manufacturing of buildings and infrastructure'))    
#cur.execute("UPDATE classification_items SET attribute1_oto = 2045 WHERE attribute1_oto = 'reserved_97' AND classification_id = 14")  

# add to 83:
# L83n = ['Generation - PV PERC (rooftop)',
# 'Generation - PV PERC (ground mounted)',
# 'Generation - PV SHJ (rooftop)',
# 'Generation - PV SHJ (ground mounted)',
# 'Generation - PV CIGS (rooftop)',
# 'Generation - PV CIGS (ground mounted)',
# 'Generation - PV III-V/Si (rooftop)',
# 'Generation - PV III-V/Si (ground mounted)',
# 'Generation - Wind Onshore - EESG-DD',
# 'Generation - Wind Onshore - PMSG-DD',
# 'Generation - Wind Offshore - PMSG-DD',
# 'Generation - Wind Offshore - PMSG-MS',
# 'Battery Storage - VFRB (Vandium Redox Flow Battery)',
# 'Battery Storage - NMC (Nickel Manganese Cobalt Lithium-Ion Battery)',
# 'Transmission Grid Line - 380 kV AC circuit',
# 'Transmission Grid Line - HC DC circuit Underground',
# 'Air to Water Heat Pump (AWHP)']
    
# L90n=['module, transparent conductive oxide layer (TCO)',
# 'module, absorber layer',
# 'module, buffer layer',
# 'module, III-V top cell',
# 'module, GaAs substrate layer',
# 'module, silicon bottom cell',
# 'rotor',
# 'nacelle',
# 'hybrid tower',
# 'foundation',
# 'nacelle, permanent magnets',
# 'monopile',
# 'inner-park cabling',
# 'transformer platform',
# 'electrolyte',
# 'electrode',
# 'stack, bipolar plate membrane',
# 'stack, conductor',
# 'stack',
# 'stack, gasket',
# 'stack, housing',
# 'cell, housing',
# 'pumps',
# 'heat exchanger',
# 'process control system',
# 'cathode',
# 'cathode, conductor foil',
# 'cathode, binder',
# 'anode',
# 'anode, conductor foil',
# 'anode, binder',
# 'electrolyte, membranes',
# 'housing',
# 'battery management system',
# 'AC circuit',
# 'DC circuit',
# 'housing',
# 'motor wiring valve',
# 'insulation piping',
# 'air fan']

# L4n= ['additive',
# 'adhesive',
# 'balsa wood',
# 'carbon felt',
# 'carbon fibre',
# 'composite core',
# 'elastomer',
# 'solvent',
# 'epoxy fibre',
# 'epoxy resin',
# 'sulfuric acid',
# 'FKM (fluorocarbon-based fluoroelastomer materials)',
# 'fluorine',
# 'glass fibre',
# 'glass fibre reinforced plastic',
# 'steel, teflon coated',
# 'steel, high-alloyed',
# 'LiPF6',
# 'mineral oil',
# 'nafion',
# 'NdFeB',
# 'phosphor',
# 'phosphoric acid',
# 'steel, plastic coated',
# 'vanadium pentoxide',
# 'polymer',
# 'polyolefine',
# 'polyvinylidene fluoride',
# 'R-134a']

# New83E=['Manual sorting of one tonne of plastics from WEEE, informal sector',
# 'waste plastic, consumer electronics, sorted',
# 'scrap steel',
# 'waste plastic',
# 'waste polyurethane foam',
# 'electricity, low voltage',
# 'formic acid',
# 'liquefied petroleum gas',
# 'sodium chloride powder',
# 'sodium hydroxide NaOH',
# 'waste plastic, consumer electronics, unsorted',
# 'water',
# 'carbon dioxide, fossil',
# 'carbon monoxide, fossil',
# 'nitrogen oxides',
# 'Particulate Matter, > 10 um ',
# 'Particulate Matter, > 2.5 um and < 10um',
# 'Sulfur dioxide',
# 'BOD5, Biological Oxygen Demand ',
# 'COD, Chemical Oxygen Demand',
# 'Chloride',
# 'DOC, Dissolved Organic Carbon',
# 'Dissolved solids',
# 'Nitrogen',
# 'Oils, non-fossil',
# 'Phosphorus',
# 'Sodium I',
# 'TOC, Total Organic Carbon',
# 'Water ',
# 'Manual sorting of one tonne of plastics from WEEE, formal sector',
# 'Treatment of one tonne of mixed lightweight packaging waste',
# 'Mixed lightweight packaging waste',
# 'Cumulative energy demand',
# 'Re-granulate plastics',
# 'Waste',
# 'Waste plastics',
# 'Ethylene',
# 'Sorting of 1kg of plastic packaging waste',
# 'Electricity',
# 'Diesel',
# 'Lubricants',
# 'Plastic waste, generic, sorted',
# 'Unsorted waste packaging plastics',
# 'Waste (rejected), after sorting',
# 'Paper/cardboard from packaging waste, sorted',
# 'Paper/cardboard packaging waste, unsorted',
# 'Sorting of 1kg of waste packaging paperboard',
# 'waste paperboard, sorted',
# 'Electricity, medium voltage',
# 'heat',
# 'lubricating oil',
# 'steel, alloyed',
# 'waste paperboard, unsorted',
# 'scrap steel, to recycling',
# 'waste graphical paper',
# 'waste paperboard',
# 'waste plastic, mixture',
# 'waste textile, soiled',
# 'waste wood, untreated',
# 'Waste paper, sorted',
# 'waste paper, unsorted',
# 'tinplate scrap, sorted',
# 'diesel, burned in building machine',
# 'tinplate, in mixed metal scrap',
# 'municipal solid waste',
# 'aluminium scrap, sorted',
# 'used aluminium packaging',
# 'Glass from packaging waste, sorted',
# 'Electricity consumption sorting facility',
# 'Lubricants consumption sorting facility',
# 'Glass packaging waste, unsorted',
# 'Wood chips, post consumer wood',
# 'Waste wood, post consumer',
# 'steel, low-alloyed, hot rolled',
# 'Recycled plastic, at plant',
# 'NaOH',
# 'Wastewater',
# 'Waste PET, sorted',
# 'Waste residues',
# 'Waste HDPE, sorted',
# 'Waste rejected, after sorting',
# 'Waste LDPE, sorted',
# 'Waste PP, sorted',
# 'Waste PS, sorted',
# 'Purified pyrolisis Oil',
# 'Mixed plastic waste',
# 'Natural gas',
# 'Char',
# 'Heavy vaccum residue',
# 'Treatment of mixed plastic wasted, via mechanical recycling',
# 'Plastic granulate',
# 'Residual waste, to incineration',
# 'Sodium hydroxide',
# 'Other fuels',
# 'Energy recovery of one tonne of mixed plastic waste, 100% incineration',
# 'Carbon dioxide',
# 'Steam',
# 'Energy recovery of one tonne of mixed plastic waste, 100% refuse-derived fuel',
# 'Energy recovery of one tonne of mixed plastic waste, 30% incineration, 70% refuse-derived fuel',
# 'Shredding of used glider, electric scooter',
# 'used glider, electric scooter',
# 'aluminium scrap, post-consumer',
# 'iron scrap, unsorted',
# 'residue from shredder fraction',
# 'copper scrap, medium grade',
# 'Treatment of one tonne of waste tyres',
# 'Waste tyres',
# 'Steel, to steel production',
# 'Rubber granulate <3mm',
# 'Rubber crumb <20mm',
# 'Steel, to disposal',
# 'Rubber, to disposal',
# 'Fibre, to disposal',
# 'Sorting of one tonne of waste wood/MDF (furniture)',
# 'Sorted waste MDF, for recycling',
# 'Waste wood/MDF',
# 'Heat, natural gas',
# 'Contaminants, to landfill',
# 'Wastewater, to treatment',
# 'Treatment of one tonne of WEEE from large appliances',
# 'Waste EEE from a large appliance',
# 'Ferrous metals to recycling',
# 'Non-ferrous metals to recycling',
# 'Other plastic non-packaging to recycling',
# 'Sorted Printed wiring board (PWB), to shredding',
# 'Others non-recyclable',
# 'Waste non-recyclable',
# 'Treatment of one tonne of WEEE from small appliances',
# 'Waste EEE from a small appliance',
# 'Sorted Batteries, to treatment',
# 'Manual dismantling of one tonne of electronics scrap from control units',
# 'electronics scrap from control units',
# 'used cable from EEE',
# 'waste PWB',
# 'waste plastic, industrial electronics',
# 'Treatment of one tonne of used PWB',
# 'Electronics scrap',
# 'Treatment of one tonne of waste cable',
# 'Waste, mostly plastics, non recyclable',
# 'Treatment of one tonne of WEEE from used fridges and freezers',
# 'Used fridges and freezers',
# 'Plastics, to recycling',
# 'Glass, to recycling',
# 'Sorting and preparation of one tonne of aluminium scrap',
# 'Unsorted aluminium scrap',
# 'Aluminium scrap, sorted, for recycling',
# 'Heat, heavy fuel oil',
# 'Ferro-silicon',
# 'Light fuel oil',
# 'Hydraulic oil (lubricant)',
# 'Detergent',
# 'Lime',
# 'Additives',
# 'Oil, to incineration',
# 'Hazardous waste',
# 'Inert waste',
# 'Filter dust, to disposal',
# 'Sorting and preparation of one tonne of metallic scrap',
# 'Unsorted metal scrap',
# 'Steel scrap, sorted, to EAF for recycling',
# 'Scrap metal, to diposal',
# 'Sorting of one tonne of mixed plastics',
# 'Waste mixed plastics',
# 'Waste PET, sorted, to recycling',
# 'Waste HDPE, sorted, to recycling',
# 'Waste PVC, sorted, to recycling',
# 'Waste PP, sorted, to recycling',
# 'Waste, non-recyclable',
# 'Sorting and preparation of one tonne of mixed cans',
# 'Mixed cans, unsorted',
# 'Steel reject, to re-processing',
# 'Dismantling of one tonne of used washing machine',
# 'Used Washing Machine',
# 'LPG',
# 'Ferrous materials, to smelting for recycling',
# 'Copper scrap, middle grade',
# 'Al, to smelting for recycling',
# 'Plastics, for recycling',
# 'Pb, for recycling',
# 'Zn, for recycling',
# 'Dismantling of one tonne of used A/C',
# 'Used A/C',
# 'Dismantling of one tonne of used refrigerator',
# 'Used Refrigerator',
# 'Dismantling of one tonne of used TV',
# 'Used TV',
# 'Glass, for recycling',
# 'Treatment of one tonne of a used refrigerator',
# 'Cr',
# 'Mn',
# 'Ni',
# 'Treatment of one tonne of PV modules',
# 'Used PV module',
# 'HNO3',
# 'CA(OH)2',
# 'Aluminium, to recycling',
# 'Steel, to recycling',
# 'Copper, to recycling',
# 'Silver, to recycling',
# 'Silicon, metallurgical grade',
# 'Thermal energy',
# 'Contaminated glass',
# 'Fly ash',
# 'Liquid waste',
# 'Sludge',
# 'NOx',
# 'Treatment of one tonne of PCB',
# 'waste PCB',
# 'tin scrap',
# 'iron scrap',
# 'lead scrap',
# 'nickel scrap',
# 'aluminium scrap',
# 'zinc scrap',
# 'silver scrap',
# 'gold scrap',
# 'resin',
# 'glass fiber',
# 'Treatment of one tonne of ASR',
# 'ASR',
# 'Scrap metals, to recycling',
# 'Waste to landfill',
# 'thermal energy, recovered',
# 'electricity, recovered',
# 'oxygen',
# 'cooling water',
# 'zinc',
# 'NaCl',
# 'sulphur',
# 'waste, to landfill',
# 'hydrogen gas',
# 'methanol',
# 'Treatment of one tonne of WEEE, high grade',
# 'WEEE, high grade',
# 'scrap aluminium',
# 'scrap iron and magnetic steel',
# 'copper and precious metals',
# 'Waste special treatment substances',
# 'Fluff and residual waste',
# 'Dismantling and shredding of one tonne of used vehicle without engine and battery',
# 'Used vehicle without engine and battery',
# 'Fuel',
# 'Magnetite',
# 'Salted solution',
# 'Copper scrap',
# 'Sand',
# 'Plastics scrap',
# 'Carbon black',
# 'Wiring board',
# 'Dismantling and shredding of one tonne of used vehicle without engine and battery, removing ECU',
# 'Treatment of one tonne of an ICE vehicle',
# 'Used vehicle',
# 'Acetylen',
# 'Lead acid battery, to recycling',
# 'Air conditioner refrigerant, to recycling',
# 'Three way catalyst, to recycling',
# 'Used engine, for remanufacturing',
# 'Scrap aluminium, to recycling',
# 'Scrap copper, to recycling',
# 'Scrap zinc, to recycling',
# 'Scrap plastic, to recycling',
# 'Scrap glass, to recycling',
# 'Scrap tire, to recycling',
# 'Scrap wiring board, to recycling',
# 'Waste oil, to recycling',
# 'Automotive shredder residue',
# 'Waste diesel',
# 'Particulates',
# 'Chemical oxygen demand',
# 'Non-methane hydrocarbon',
# 'Treatment of one tonne of Automotive plastic waste (APW)',
# 'Mixed automotive shredder residue waste',
# 'Scrap ferrous metals, to recycling',
# 'Scrap non-ferrous metals, to recycling',
# 'Processing costs',
# 'Mixed automotive shredder residue',
# 'Ethene',
# 'Propene',
# 'Butadiene',
# 'Pyrolysis gasoline',
# 'Treatment of one tonne of mixed waste plastics from WEEE',
# 'Mixed waste plastics from WEEE',
# 'Catalyst',
# 'Chemical for air pollution control',
# 'Solid waste to landfill',
# 'Unrefined light sweet crude oil',
# 'Treatment of one tonne of mixed waste plastics from ELV',
# 'Mixed waste plastics from ELV',
# 'Dismantling of one tonne of ELV hulk',
# 'ELV Hulk',
# 'Ferrous metals scrap',
# 'H2O Vapour',
# 'CO',
# 'CH2O',
# 'Particulate matter<2.5μm²',
# 'Particulate matter<10μm²',
# 'Polycyclic aromatic hydrocarbons ',
# 'SO2',
# 'Total volatile organic compounds',
# 'Shredding one tonne of ELV hulk',
# 'Ferrous metals scrap, to recycling',
# 'Non-ferrous metals scrap, to recycling',
# 'Mixed waste',
# 'Process water',
# 'NO2',
# 'Particulate matter',
# 'Dismantling of ELV',
# 'Used ELV',
# 'Fluids, to recycling',
# 'Gasoline, to reuse',
# 'Antifreeze fluid, to reuse',
# 'Catalytic convertor',
# 'Aluminium rims, to recycling',
# 'Steel rims, to recycling',
# 'Copper radiators, to recycling',
# 'Aluminium radiators, to recycling',
# 'Batteries, to recycling',
# 'Tires, to recycling',
# 'Starters, to remanufacturing',
# 'Alternators, to remanufacturing',
# 'Air conditoner /compressor, to remanufacturing',
# 'Other parts, direct reuse',
# 'Tires, direct reuse',
# 'Treatment of one tonne of waste passenger tires',
# 'Waste passenger tires',
# 'Cast iron',
# 'Coal',
# 'Steel wire',
# 'Gasoline',
# 'Heavy oil',
# 'Carbon black, refined',
# 'Carbon black, crude',
# 'Fuel oil',
# 'Ferrous metals',
# '60 mesh crumb rubber',
# 'Devulcanized rubber',
# 'CH4',
# 'NMVOC',
# 'H2S',
# 'Dust',
# 'As',
# 'Cd',
# 'Hg',
# 'Pb',
# 'Zn',
# 'Low-quality oil',
# 'pyrometallurgical treatment of 1 kg of used Li-ion battery',
# 'used Li-ion battery',
# 'iron scrap, unsorted, recyclable',
# 'manganese dioxide',
# 'cobalt',
# 'non-Fe-Co-metals',
# 'particulate matter, < 2.5 um',
# 'particulate matter, > 10 um',
# 'sulfate',
# 'treatment of 1 kg non-Fe-Co-metals from pyrometallurgical treatment of used Li-ion batteries',
# 'non-Fe-Co-metals, from pyrometallurgical treatment of used Li-ion battery',
# 'electricity, high voltage',
# 'heat, district or industrial, other than natural gas',
# 'oxygen, liquid',
# 'copper cathode',
# 'chlorine',
# 'copper',
# 'dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin',
# 'fluorine',
# 'hydrometallurgical treatment of 1 kg of used Li-ion battery',
# 'chemical, inorganic',
# 'lime, hydrated, packed',
# 'sulfuric acid',
# 'lithium carbonate',
# 'inert waste, for final disposal',
# 'waste gypsum',
# 'NMVOC, non-methane volatile organic compounds, unspecified origin',
# 'BOD5, Biological Oxygen Demand',
# 'cobalt II',
# 'copper ion',
# 'fluoride',
# 'hydrocarbons, unspecified',
# 'nickel II',
# 'suspended solids, unspecified',
# 'treatment of 1 kg non-Fe-Co-metals from hyrometallurgical treatment of used Li-ion batteries',
# 'non-Fe-Co-metals, from Li-ion battery, hydrometallurgical processing',
# 'ammonia, anhydrous, liquid',
# 'manganese',
# 'treatment of 3499.97 kg spent lead-acid batteries',
# 'spent lead-acid batteries',
# 'antimony',
# 'arsenic',
# 'coke',
# 'scrap iron',
# 'slaked lime',
# 'potassium carbonate',
# 'selenium',
# 'sodium carbonate',
# 'sodium chloride',
# 'sodium nitrate',
# 'sulfur',
# 'tin',
# 'refined lead',
# 'carbon monoxide',
# 'lead',
# 'particulates, unspecified',
# 'plastic mix to recycling',
# 'plastic mix to landfill',
# 'sludge from neutralization',
# 'smelting residues',
# 'treatment of 1 kg spent Ni-Cd batteries, pyrometallurgy',
# 'spent Ni-Cad batteries',
# 'furnace gas',
# 'cadmium (emission to air)',
# 'nickel (emission to air)',
# 'cadmium (emission to water)',
# 'nickel (emission to water)',
# 'cadmium (secondary)',
# 'ferronickel (secondary)',
# 'treatment of 1500 kg spent Ni-Cd batteries, hydrometallurgy',
# 'external cases (~ 95 % steel, ~ 5 % PVC and PA)',
# 'sulphuric acid',
# 'ammonia',
# 'hydrogen peroxide, 30 %',
# 'energy',
# 'nickel, secondary (98-99 % purity)',
# 'cadmium, secondary (98-100 % purity)',
# 'Fe(OH)3 with ~ 3 % coprecipitated Nickel',
# 'insoluble powder (> 53 % Nickel, ca. 40 % Cadmium)',
# 'solid residues of the electrode scrap (> 70 % iron, 20-30 % Nickel)',
# 'treatment of 1 kWh LFP Li-Ion battery',
# 'retired LFP battery',
# 'hydrochloric acid, 30%',
# 'hydrogen peroxide, 7.5%',
# 'sodium hydroxide, 32%',
# 'calcium chloride',
# 'lithium chloride',
# 'hydrogen fluoride',
# 'VOC',
# 'hydrochloric acid mist',
# 'plastic casing scrap',
# 'separator scrap',
# 'waste battery management system',
# 'aluminium, scrap',
# 'waste graphite',
# 'other solid waste',
# 'treatment of 1 kWh NCM Li-Ion battery',
# 'retired NCM battery',
# 'NMP (N-Methyl-2-pyrrolydone)',
# 'decarbonised water',
# 'hydrochloric acid',
# 'hydrogen peroxide',
# 'sodium carbonide',
# 'deionised water',
# 'chromium steel 18/8',
# 'aluminium',
# 'cathode active material',
# 'waste copper',
# 'waste aluminium',
# 'waste printed wiring board',
# 'waste chromium steel 18/8',
# 'waste coolant',
# 'waste fibre glass',
# 'waste steel',
# 'waste PP',
# 'waste PE',
# 'waste PET',
# 'waste sludge',
# 'waste PVDF',
# 'waste water',
# 'nitrogen, liquid',
# 'DMC solvent',
# 'glucose',
# 'cathode materials',
# 'graphite scrap',
# 'aluminium foil scrap',
# 'copper foil scrap',
# 'plastic scrap',
# 'electrolyte scrap',
# 'aluminium case scrap',
# 'lithium hydroxide',
# 'citric acid',
# 'transport (freight rail)',
# 'transport (freight lorry)',
# 'LFP (lithium iron phosphate)',
# 'lithium hexafluorophosphate (LiPF6)',
# 'ethylene carbonate (EC)',
# 'dimethyl carbonate (DMC)',
# 'lithium hydroxide (LiOH)',
# 'chrominium steel 18/8']


# for mk in range(0,486):
#     try:
#         cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,New83E[mk]))
#     except:
#         None
        
# Aa = 'Filter dust, to disposal'        
# cur.execute("INSERT INTO classification_items (classification_id,attribute1_oto) VALUES (%s,%s)",(83,Aa))

# Close connection
cur.close()
conn.close()


#
#
#
#


