# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:01:15 2018

@author: spauliuk

LIST OF MODIFICATIONS to IEDC database. Changes are already carried out add entered in db creation master files.
Listed here for documenation purposes.
"""

import pymysql
import datetime
import IEDC_PW
import pandas as pd


#conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc_review', autocommit=True, charset='utf8')
conn = pymysql.connect(host='www.industrialecology.uni-freiburg.de', port=3306, user=IEDC_PW.IEDC_write_access_user, passwd=IEDC_PW.IEDC_write_access_user_PW, db='iedc', autocommit=True, charset='utf8')

cur = conn.cursor()

# 1) Change classification_items.attribute2_oto from VARCHAR(255) to TEXT to accommodate for long descriptions.
cur.execute("ALTER TABLE classification_items MODIFY attribute2_oto TEXT")
cur.execute("UPDATE classification_definition SET meaning_attribute1 = 'Commodity code (NACEv2)' WHERE id = 5")
cur.execute("UPDATE classification_definition SET meaning_attribute2 = 'Commodity group name' WHERE id = 5")

# 2) Fix ; wrapping in NACEv2_(ProdCom)_data.xlsx
Filein  = 'C:\\Users\\spauliuk\\Desktop\\NACEv2_(ProdCom)_data.xlsx'
Fileout = 'C:\\Users\\spauliuk\\Desktop\\NACEv2_(ProdCom)_data.csv'
Delimiter = ';'
DF = pd.read_excel(Filein,index_col=0)
DF.to_csv(Fileout,sep = Delimiter)
# Still needs manual fix as some character cannot be decoded (use editor and save as utf-8).

## close connection
cur.close()
conn.close()
#
#    
#    
# The End