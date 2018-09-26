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

# add FOREIGN KEY Constraints to main tables

# projects
cur.execute("ALTER TABLE projects ADD CONSTRAINT project_license_id FOREIGN KEY (project_license) REFERENCES licences(id)")
cur.execute("ALTER TABLE projects ADD CONSTRAINT project_sources_id FOREIGN KEY (type_of_source)  REFERENCES source_type(id)")
cur.execute("ALTER TABLE projects ADD CONSTRAINT project_users_id   FOREIGN KEY (submitting_user) REFERENCES users(id)")

# datagroups
cur.execute("ALTER TABLE datagroups ADD CONSTRAINT datagroups_license_id FOREIGN KEY (project_license) REFERENCES licences(id)")
cur.execute("ALTER TABLE datagroups ADD CONSTRAINT datagroups_sources_id FOREIGN KEY (type_of_source)  REFERENCES source_type(id)")
cur.execute("ALTER TABLE datagroups ADD CONSTRAINT datagroups_users_id   FOREIGN KEY (submitting_user) REFERENCES users(id)")
cur.execute("ALTER TABLE datagroups ADD CONSTRAINT datagroups_project_id FOREIGN KEY (project_id)      REFERENCES projects(id)")

# datasets
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_datagroups_id      FOREIGN KEY (datagroup_id)     REFERENCES datagroups(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_categories_id      FOREIGN KEY (data_category)    REFERENCES categories(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_types_id           FOREIGN KEY (data_type)        REFERENCES types(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_layers_id          FOREIGN KEY (data_layer)       REFERENCES layers(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_provenance_id      FOREIGN KEY (data_provenance)  REFERENCES provenance(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_source_id          FOREIGN KEY (type_of_source)   REFERENCES source_type(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_licenses_id        FOREIGN KEY (project_license)  REFERENCES licences(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_submitting_user_id FOREIGN KEY (submitting_user)  REFERENCES users(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_reviewing_user_id  FOREIGN KEY (review_user)      REFERENCES users(id)")

cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect1            FOREIGN KEY (aspect_1)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect2            FOREIGN KEY (aspect_2)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect3            FOREIGN KEY (aspect_3)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect4            FOREIGN KEY (aspect_4)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect5            FOREIGN KEY (aspect_5)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect6            FOREIGN KEY (aspect_6)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect7            FOREIGN KEY (aspect_7)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect8            FOREIGN KEY (aspect_8)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect9            FOREIGN KEY (aspect_9)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect10           FOREIGN KEY (aspect_10)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect11           FOREIGN KEY (aspect_11)         REFERENCES aspects(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect12           FOREIGN KEY (aspect_12)         REFERENCES aspects(id)")

cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect1_classf     FOREIGN KEY (aspect_1_classification)  REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect2_classf     FOREIGN KEY (aspect_2_classification)  REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect3_classf     FOREIGN KEY (aspect_3_classification)  REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect4_classf     FOREIGN KEY (aspect_4_classification)  REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect5_classf     FOREIGN KEY (aspect_5_classification)  REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect6_classf     FOREIGN KEY (aspect_6_classification)  REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect7_classf     FOREIGN KEY (aspect_7_classification)  REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect8_classf     FOREIGN KEY (aspect_8_classification)  REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect9_classf     FOREIGN KEY (aspect_9_classification)  REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect10_classf    FOREIGN KEY (aspect_10_classification) REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect11_classf    FOREIGN KEY (aspect_11_classification) REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE datasets ADD CONSTRAINT datasets_aspect12_classf    FOREIGN KEY (aspect_12_classification) REFERENCES classification_definition(id)")

# data
cur.execute("ALTER TABLE data ADD CONSTRAINT data_datasets_id      FOREIGN KEY (dataset_id) REFERENCES datasets(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_unitsnom_id      FOREIGN KEY (unit_nominator) REFERENCES units(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_unitsden_id      FOREIGN KEY (unit_denominator) REFERENCES units(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_stats_array_id   FOREIGN KEY (stats_array_1) REFERENCES stats_array(id)")

cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_1         FOREIGN KEY (aspect1) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_2         FOREIGN KEY (aspect2) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_3         FOREIGN KEY (aspect3) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_4         FOREIGN KEY (aspect4) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_5         FOREIGN KEY (aspect5) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_6         FOREIGN KEY (aspect6) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_7         FOREIGN KEY (aspect7) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_8         FOREIGN KEY (aspect8) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_9         FOREIGN KEY (aspect9) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_10        FOREIGN KEY (aspect10) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_11        FOREIGN KEY (aspect11) REFERENCES classification_items(id)")
cur.execute("ALTER TABLE data ADD CONSTRAINT data_aspect_12        FOREIGN KEY (aspect12) REFERENCES classification_items(id)")

# classification_definition
## Add 13 dimension first ('custom' dimension)
cur.execute("INSERT INTO dimensions (id,name,description) Values (13,'custom','placeholder for custom classification and dimension')")
cur.execute("UPDATE classification_definition SET dimension = 13 WHERE id = 15")
cur.execute("ALTER TABLE classification_definition ADD CONSTRAINT classification_dimension_id FOREIGN KEY (dimension) REFERENCES dimensions(id)")

# classification_items
cur.execute("ALTER TABLE classification_items ADD CONSTRAINT classification_items_classification_id FOREIGN KEY (classification_id) REFERENCES classification_definition(id)")
cur.execute("ALTER TABLE classification_items ADD CONSTRAINT classification_items_hierarchy FOREIGN KEY (parent_id) REFERENCES classification_items(id)")

# add FOREIGN KEY constraints to lookup tables

# types
cur.execute("ALTER TABLE types ADD CONSTRAINT types_category_id FOREIGN KEY (reference_data_category) REFERENCES categories(id)")

# aspects
cur.execute("ALTER TABLE aspects ADD CONSTRAINT aspects_dimension_id FOREIGN KEY (dimension) REFERENCES dimensions(id)")



# Drop wrongly specified constraints:
##cur.execute("ALTER TABLE data DROP FOREIGN KEY data_aspect_10")

    
    

## close connection
cur.close()
conn.close()
#
#    
#    
# The End