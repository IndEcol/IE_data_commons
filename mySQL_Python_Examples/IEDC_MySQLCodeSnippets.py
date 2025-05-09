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

# get total number of data
cur.execute("SELECT COUNT(*) FROM data")
for row in cur:
    print(row)  
    
cur.execute("SELECT COUNT(*) FROM datasets")
for row in cur:
    print(row)  
    
cur.execute("Show tables")
for row in cur:
    print(row)

cur.execute("DESCRIBE iedc_review.datasets")
DSD = []
for row in cur:
    print(row)
    DSD.append(row)

# Select all from table:
cur.execute("DESCRIBE iedc_review.licences")
for row in cur:
    print(row)

cur.execute("SELECT index_letter FROM aspects")
for row in cur:
    print(row)
    
cur.execute("SELECT index_letter FROM aspects WHERE index_letter = 'D' ")
for row in cur:
    print(row)
    
cur.execute("SELECT * FROM aspects")
for row in cur:
    print(row)   

cur.execute("SELECT * FROM types")
for row in cur:
    print(row)    
    
cur.execute("SELECT * FROM layers")
for row in cur:
    print(row)      
    
cur.execute("SELECT * FROM dimensions")
for row in cur:
    print(row)       
    
cur.execute("SELECT * FROM datagroups")
for row in cur:
    print(row)
    
cur.execute("SELECT * FROM datagroups WHERE id = 27")
for row in cur:
    print(row)    
        
cur.execute("SELECT * FROM datasets")
for row in cur:
    print(row)
    
cur.execute("SELECT * FROM units")
for row in cur:
    print(row)    
    
cur.execute("SELECT * FROM projects")
for row in cur:
    print(row)        
    
cur.execute("SELECT * FROM users")
for row in cur:
    print(row)      
    
cur.execute("SELECT * FROM classification_definition")
for row in cur:
    print(row)

A = []
cur.execute("SELECT attribute1_oto FROM classification_items WHERE classification_id = 13")
for row in cur:
    print(row)
    A.append(row[0])
    
# Show table creation statement    
cur.execute("SHOW CREATE TABLE dimensions")
for row in cur:
    print(row)   
    
cur.execute("SHOW CREATE TABLE units")
for row in cur:
    print(row)  
    
cur.execute("SHOW CREATE TABLE data")
for row in cur:
    print(row)      
    
cur.execute("SHOW CREATE TABLE classification_items")
for row in cur:
    print(row)        
    
cur.execute("SHOW TABLE STATUS FROM iedc_review WHERE `name` LIKE 'datasets'")    
for row in cur:
    print(row)
    
# Get current auto_increment values:    
cur.execute("SELECT table_name, Auto_increment FROM information_schema.tables WHERE table_schema = DATABASE()")    
for row in cur:
    print(row)

cur.execute("SELECT COUNT(*) FROM datasets")
for row in cur:
    print(row)    


cur.execute("SELECT COUNT(*) FROM data WHERE dataset_id = 420")
for row in cur:
    print(row)   
    
cur.execute("SELECT COUNT(*) FROM data WHERE aspect7 = 5987") # search for wrong entry for Kosovo 3 digit code
for row in cur:
    print(row)     
    
cur.execute("SELECT DISTINCT dataset_id FROM data WHERE aspect6 = 5987") # search for wrong entry for Kosovo 3 digit code
for row in cur:
    print(row)     
    
cur.execute("SELECT COUNT(*) FROM classification_definition")
for row in cur:
    print(row)       
    
cur.execute("SELECT * FROM data WHERE id = 722907")
for row in cur:
    print(row)    
    
    
cur.execute("SELECT MAX(id) FROM data")
for row in cur:
    print(row)    
    
    
# get total number of classification_items
cur.execute("SELECT COUNT(*) FROM classification_items")
for row in cur:
    print(row)    
    
cur.execute("SELECT count(*) FROM classification_items WHERE classification_id = 24")
for row in cur:
    print(row) 
    
cur.execute("SELECT * FROM classification_definition WHERE id = 2")
for row in cur:
    print(row)     
    
cur.execute("SELECT attribute1_oto FROM classification_items  WHERE classification_id = 25")
for row in cur:
    print(row)
    
cur.execute("SELECT * FROM classification_items  WHERE classification_id = 2 AND attribute3_oto = 'PSE'")
for row in cur:
    print(row)    
    
cur.execute("SELECT unit_denominator FROM data WHERE dataset_id = 112")
for row in cur:
    print(row)      
    
cur.execute("SELECT * FROM data WHERE dataset_id = 195 AND aspect1 = 6094")
for row in cur:
    print(row)     

cur.execute("SELECT * FROM datasets WHERE id = 69")
for row in cur:
    print(row)     
    
cur.execute("SELECT * FROM projects WHERE id = 7")
for row in cur:
    print(row)   
    
# Check licenses of projects
cur.execute("SELECT datagroup_name,submitting_user FROM datagroups ORDER BY id")
Tuples = cur.fetchall()
Pnames  = [x[0] for x in Tuples]      
Psourc  = [x[1] for x in Tuples]      
    
#cur.execute("UPDATE data SET unit_denominator = 1 WHERE dataset_id = 112") 
# Change auto_increment    
#cur.execute("ALTER TABLE iedc_review.licences AUTO_INCREMENT = 5")
#cur.execute("ALTER TABLE iedc_review.datasets AUTO_INCREMENT = 1")
    
# Insert data into tables with auto_increment and default NULL columns:
#SQL = "INSERT INTO iedc_review.licences (name,description) VALUES ('Crown Copyright','')"
#cur.execute(SQL)
#D = ['Test','']
#SQL = "INSERT INTO iedc_review.licences (name,description) VALUES (%s,%s)"
#cur.execute(SQL,('Test',''))
    
# Delete
#cur.execute("DELETE FROM iedc_review.licences WHERE id = 5")    
#cur.execute("DELETE FROM iedc_review.datasets WHERE id = 1") 
#
#cur.execute("DELETE FROM datagroups")
#cur.execute("DELETE FROM datasets")
#cur.execute("DELETE FROM classification_items")
#
#cur.execute("DELETE FROM iedc_review.data")
#cur.execute("ALTER TABLE data AUTO_INCREMENT = 1")
#
#
#cur.execute("DELETE FROM data")
   
#cur.execute("DELETE FROM data WHERE dataset_id = 369")
    
#
#cur.execute("ALTER TABLE data AUTO_INCREMENT = 10478")
#cur.execute("ALTER TABLE datagroups AUTO_INCREMENT = 10")
#cur.execute("TRUNCATE TABLE data")
#cur.execute("DROP TABLE data")
 
# cur.execute("DELETE FROM classification_items WHERE classification_id > 23")        
cur.execute("DELETE FROM classification_definition WHERE id > 23")   

cur.execute("ALTER TABLE classification_definition AUTO_INCREMENT = 10000")
    
# get units
cur.execute("SELECT * FROM licences")
for row in cur:
    print(row)
    
cur.execute("SELECT DISTINCT(process_id) FROM stocks")
for row in cur:
    print(row)    

# Insert into datasets:
# id is not set because of auto_increment

cur.execute("SELECT dataset_name,aspect_4_classification FROM datasets WHERE id = 11") 
for row in cur:
    print(row) 
    
#cur.execute("UPDATE datasets SET aspect_4_classification = 14 WHERE id = 10") 


conn.commit()

# Create new read only user
'''
CREATE USER 'sample_user'@'www.industrialecology.uni-freiburg.de' IDENTIFIED BY '...';
GRANT ALL ON iedc.* TO 'sample_user'@'www.industrialecology.uni-freiburg.de';
FLUSH PRIVILEGES;

CREATE USER 'sample_user'@'%' IDENTIFIED BY '...';
GRANT ALL ON iedc.* TO 'sample_user'@'%';
FLUSH PRIVILEGES;
'''

# move data ids in data table:
for m in range(0,118650):
    print(m)
    cur.execute("UPDATE data SET id = %s WHERE id = %s",(m+1,m+93724)) 


cur.execute("SELECT * FROM units")
for row in cur:
    print(row)

m=10
print('Aspect and classification mismatch for dataset %s and aspect %s.' % ((m+1), m))


# cur.execute("CREATE TABLE data (id int(11) NOT NULL AUTO_INCREMENT,dataset_id int(11) NOT NULL,aspect1 int(11) NOT NULL,aspect2 int(11) DEFAULT NULL,aspect3 int(11) DEFAULT NULL,aspect4 int(11) DEFAULT NULL,aspect5 int(11) DEFAULT NULL,aspect6 int(11) DEFAULT NULL,aspect7 int(11) DEFAULT NULL,aspect8 int(11) DEFAULT NULL,aspect9 int(11) DEFAULT NULL,aspect10 int(11) DEFAULT NULL,aspect11 int(11) DEFAULT NULL,aspect12 int(11) DEFAULT NULL,value double DEFAULT NULL,unit_nominator int(11) NOT NULL,unit_denominator int(11) DEFAULT NULL,stats_array_1 int(11) DEFAULT NULL,stats_array_2 double DEFAULT NULL,stats_array_3 double DEFAULT NULL,stats_array_4 double DEFAULT NULL,comment text,reserve1 varchar(255) DEFAULT NULL,reserve2 varchar(255) DEFAULT NULL,reserve3 varchar(255) DEFAULT NULL,PRIMARY KEY (`id`),KEY `data_datasets_id` (`dataset_id`),KEY `data_unitsnom_id` (`unit_nominator`),KEY `data_unitsden_id` (`unit_denominator`),KEY `data_stats_array_id` (`stats_array_1`),KEY `data_aspect_1` (`aspect1`),KEY `data_aspect_2` (`aspect2`),KEY `data_aspect_3` (`aspect3`),KEY `data_aspect_4` (`aspect4`),KEY `data_aspect_5` (`aspect5`),KEY `data_aspect_6` (`aspect6`),KEY `data_aspect_7` (`aspect7`),KEY `data_aspect_8` (`aspect8`),KEY `data_aspect_9` (`aspect9`),KEY `data_aspect_10` (`aspect10`),KEY `data_aspect_11` (`aspect11`),KEY `data_aspect_12` (`aspect12`),CONSTRAINT `data_aspect_1` FOREIGN KEY (`aspect1`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_10` FOREIGN KEY (`aspect10`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_11` FOREIGN KEY (`aspect11`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_12` FOREIGN KEY (`aspect12`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_2` FOREIGN KEY (`aspect2`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_3` FOREIGN KEY (`aspect3`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_4` FOREIGN KEY (`aspect4`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_5` FOREIGN KEY (`aspect5`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_6` FOREIGN KEY (`aspect6`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_7` FOREIGN KEY (`aspect7`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_8` FOREIGN KEY (`aspect8`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_aspect_9` FOREIGN KEY (`aspect9`) REFERENCES `classification_items` (`id`),CONSTRAINT `data_datasets_id` FOREIGN KEY (`dataset_id`) REFERENCES `datasets` (`id`),CONSTRAINT `data_stats_array_id` FOREIGN KEY (`stats_array_1`) REFERENCES `stats_array` (`id`),CONSTRAINT `data_unitsden_id` FOREIGN KEY (`unit_denominator`) REFERENCES `units` (`id`),CONSTRAINT `data_unitsnom_id` FOREIGN KEY (`unit_nominator`) REFERENCES `units` (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci")

#CREATE TABLE data (
#id int(11) NOT NULL AUTO_INCREMENT,
#dataset_id int(11) NOT NULL,
#aspect1 int(11) NOT NULL,
#aspect2 int(11) DEFAULT NULL,
#aspect3 int(11) DEFAULT NULL,
#aspect4 int(11) DEFAULT NULL,
#aspect5 int(11) DEFAULT NULL,
#aspect6 int(11) DEFAULT NULL,
#aspect7 int(11) DEFAULT NULL,
#aspect8 int(11) DEFAULT NULL,
#aspect9 int(11) DEFAULT NULL,
#aspect10 int(11) DEFAULT NULL,
#aspect11 int(11) DEFAULT NULL,
#aspect12 int(11) DEFAULT NULL,
#value double DEFAULT NULL,
#unit_nominator int(11) NOT NULL,
#unit_denominator int(11) DEFAULT NULL
#stats_array_1 int(11) DEFAULT NULL,
#stats_array_2 double DEFAULT NULL,
#stats_array_3 double DEFAULT NULL,
#stats_array_4 double DEFAULT NULL,
#comment text,
#reserve1 varchar(255) DEFAULT NULL,
#reserve2 varchar(255) DEFAULT NULL,
#reserve3 varchar(255) DEFAULT NULL,
#PRIMARY KEY (`id`),
#KEY `data_datasets_id` (`dataset_id`),
#KEY `data_unitsnom_id` (`unit_nominator`),
#KEY `data_unitsden_id` (`unit_denominator`),
#KEY `data_stats_array_id` (`stats_array_1`),
#KEY `data_aspect_1` (`aspect1`),
#KEY `data_aspect_2` (`aspect2`),
#KEY `data_aspect_3` (`aspect3`),
#KEY `data_aspect_4` (`aspect4`),
#KEY `data_aspect_5` (`aspect5`),
#KEY `data_aspect_6` (`aspect6`),
#KEY `data_aspect_7` (`aspect7`),
#KEY `data_aspect_8` (`aspect8`),
#KEY `data_aspect_9` (`aspect9`),
#KEY `data_aspect_10` (`aspect10`),
#KEY `data_aspect_11` (`aspect11`),
#KEY `data_aspect_12` (`aspect12`),
#CONSTRAINT `data_aspect_1` FOREIGN KEY (`aspect1`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_10` FOREIGN KEY (`aspect10`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_11` FOREIGN KEY (`aspect11`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_12` FOREIGN KEY (`aspect12`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_2` FOREIGN KEY (`aspect2`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_3` FOREIGN KEY (`aspect3`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_4` FOREIGN KEY (`aspect4`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_5` FOREIGN KEY (`aspect5`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_6` FOREIGN KEY (`aspect6`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_7` FOREIGN KEY (`aspect7`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_8` FOREIGN KEY (`aspect8`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_aspect_9` FOREIGN KEY (`aspect9`) REFERENCES `classification_items` (`id`),
#CONSTRAINT `data_datasets_id` FOREIGN KEY (`dataset_id`) REFERENCES `datasets` (`id`),
#CONSTRAINT `data_stats_array_id` FOREIGN KEY (`stats_array_1`) REFERENCES `stats_array` (`id`),
#CONSTRAINT `data_unitsden_id` FOREIGN KEY (`unit_denominator`) REFERENCES `units` (`id`),
#CONSTRAINT `data_unitsnom_id` FOREIGN KEY (`unit_nominator`) REFERENCES `units` (`id`)
#) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci 

#cur.execute("SELECT * FROM datasets WHERE id = 1 ")
#for row in cur:
#    print(row)
##cur.execute("UPDATE datasets SET datagroup_id = 8 WHERE id = 1") 
#    
#    
## Create table to test auto increment    
#cur.execute("CREATE TABLE test (id int(11) NOT NULL AUTO_INCREMENT, text int(11) NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci")
#cur.execute("INSERT INTO test (text) VALUES (10)")
#cur.execute("INSERT INTO test (text) VALUES (11)")
#cur.execute("INSERT INTO test (text) VALUES (12)")
#cur.execute("INSERT INTO test (text) VALUES (13)")        
#
#cur.execute("INSERT INTO test (id, text) VALUES (10, 20)")        
#
#cur.execute("INSERT INTO test (text) VALUES (30)")  
#
#cur.execute("INSERT INTO test (id, text) VALUES (7, 99)")  
#
#cur.execute("INSERT INTO test (text) VALUES (101)")  
#
#cur.execute("SELECT * FROM test")
#for row in cur:
#    print(row)
#
#cur.execute("DROP TABLE IF EXISTS test")
#
#
## Drop NOT NULL constraint for data table:
#cur.execute("ALTER TABLE data MODIFY COLUMN value double")

### 
#Try out 1 : Select data for CIRCOMOD CE profile prototype
cur.execute("SELECT id FROM classification_items WHERE classification_id = 77 AND attribute1_oto = 'Italy'")
for row in cur:
    print(row)
    SelectedRegionId = row[0]
    
cur.execute("SELECT id FROM classification_items WHERE classification_id = 8 AND attribute1_oto = 'SSP1'")
for row in cur:
    print(row)    
    SelectedScenarioId = row[0]    
    
query = 'select ci4.attribute1_oto as aspect_4, d.value, u1.unitcode, u2.unitcode from iedc.data d '
query += 'left join iedc.units u1 on d.unit_nominator = u1.id left join iedc.units u2 on d.unit_denominator = u2.id '
query += 'left join iedc.classification_items ci4 on d.aspect4 = ci4.id '
query += 'inner join iedc.datasets ds on d.dataset_id = ds.id where d.dataset_id = 304 and d.aspect3 = %s and d.aspect5 = %s'
cur.execute(query,(SelectedRegionId,SelectedScenarioId))    
for row in cur:
    print(row)   
    
#Try out 2 : Select data for CIRCOMOD CE profile prototype    
cur.execute("SELECT id FROM classification_items WHERE classification_id = 77 AND attribute1_oto = 'Italy'")
for row in cur:
    print(row)
    SelectedRegionId = row[0]
    
cur.execute("SELECT id FROM classification_items WHERE classification_id = 8 AND attribute1_oto = 'SSP2'")
for row in cur:
    print(row)    
    SelectedScenarioId = row[0]    


query = 'select ci8.attribute1_oto as aspect_8, d.value, u1.unitcode, u2.unitcode from iedc.data d '
query += 'left join iedc.units u1 on d.unit_nominator = u1.id '
query += 'left join iedc.units u2 on d.unit_denominator = u2.id '
query += 'left join iedc.classification_items ci8 on d.aspect8 = ci8.id '
query += 'inner join iedc.datasets ds on d.dataset_id = ds.id '
query += 'where d.dataset_id = 307 and d.aspect1 = %s and d.aspect3 = %s and d.aspect4 = %s and d.aspect6 = 9 and d.aspect7 = %s'

# With class. ids for 'Italy', 'passenger vehicles', 'energy supply', 'HIY-RLU-MSU' and 9 (for SSP2)
cur.execute(query,(102920,1071,57,102960))  
for row in cur:
    print(row)      
    
## 4) close connection
cur.close()
conn.close()
#
#    
#    
# The End