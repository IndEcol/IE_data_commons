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


# Close connection
cur.close()
conn.close()


#
#
#
#
#


