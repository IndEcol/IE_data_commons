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

# categories
cur.execute("ALTER TABLE categories ADD CONSTRAINT UC_categories UNIQUE (name)")

# aspects
cur.execute("ALTER TABLE aspects ADD CONSTRAINT UC_aspects_1 UNIQUE (aspect)")
cur.execute("ALTER TABLE aspects MODIFY index_letter varchar(1) BINARY NOT NULL") # swith datatype to make column case-sensitive
cur.execute("ALTER TABLE aspects ADD CONSTRAINT UC_aspects_2 UNIQUE (index_letter)")

# dimensions
cur.execute("ALTER TABLE dimensions ADD CONSTRAINT UC_dimensions UNIQUE (name)")

# datagroups
cur.execute("ALTER TABLE datagroups ADD CONSTRAINT UC_datagroups UNIQUE (datagroup_name)")

# datasets
cur.execute("ALTER TABLE datasets ADD CONSTRAINT UC_datasets UNIQUE (dataset_name, dataset_version)")

#classification_definition
cur.execute("ALTER TABLE classification_definition ADD CONSTRAINT UC_classification_definition UNIQUE (classification_name)")

# classification_items
cur.execute("ALTER TABLE classification_items ADD CONSTRAINT UC_classification_items UNIQUE (classification_id, attribute1_oto)")

# layers
cur.execute("ALTER TABLE layers ADD CONSTRAINT UC_layers UNIQUE (name)")

# licenses
cur.execute("ALTER TABLE licences ADD CONSTRAINT UC_licences UNIQUE (name)")

# projects
cur.execute("ALTER TABLE projects ADD CONSTRAINT UC_projects UNIQUE (project_name)")

# provenance
cur.execute("ALTER TABLE provenance ADD CONSTRAINT UC_provenance UNIQUE (name)")

# source_type
cur.execute("ALTER TABLE source_type ADD CONSTRAINT UC_source_type UNIQUE (name)")

# types
cur.execute("ALTER TABLE types ADD CONSTRAINT UC_types_1 UNIQUE (name)")
cur.execute("ALTER TABLE types ADD CONSTRAINT UC_types_2 UNIQUE (symbol)")

# units
# Replace 'reserved' by 'reserved_123 etc.'
cur.execute("SELECT id FROM units WHERE unit_name = 'reserved'")
for row in cur:
    print(row[0])
    cur.execute("UPDATE units SET unit_name = 'reserved_%s' WHERE id = %s", (row[0],row[0]))
    cur.execute("UPDATE units SET unitcode  = 'reserved_%s' WHERE id = %s", (row[0],row[0]))
    
# add keys
cur.execute("ALTER TABLE units ADD CONSTRAINT UC_unit_1 UNIQUE (unit_name)")
cur.execute("ALTER TABLE units MODIFY unitcode varchar(30) BINARY NOT NULL") # swith datatype to make column case-sensitive
cur.execute("ALTER TABLE units ADD CONSTRAINT UC_unit_2 UNIQUE (unitcode)")

# users
cur.execute("ALTER TABLE users ADD CONSTRAINT UC_users UNIQUE (username)")


## close connection
cur.close()
conn.close()
#
#    
#    
# The End