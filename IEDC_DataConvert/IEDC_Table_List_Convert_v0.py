# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 10:52:07 2025

@author: Stefan Pauliuk
"""

import pandas as pd
import openpyxl
import os

dpath = 'C:\\Users\\Stefan Pauliuk\\FILES\\ARBEIT\\PROJECTS\\Database\\IE_DataCommons\\NEW\\CMS_Inbox'

fn = os.path.join(dpath,'HW_Baublock_Stichprobe_Tabellisiert.xlsx')

ps = pd.read_excel(fn, sheet_name='Daten', index_col=0) # table with data
    
list_df = ps.unstack().reset_index()


list_df.to_excel(os.path.join(dpath,'HW_Baublock_Stichprobe_Tabellisiert_list.xlsx'), merge_cells=False)  


#
#
#
#
# The end
#
#