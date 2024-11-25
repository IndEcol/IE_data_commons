# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:00:19 2024

@author: Stefan Pauliuk
"""

'''
From Tomer Fishman, March 12th, 2024:
    
Just a quick reply on the RASMI data (https://github.com/TomerFishman/MaterialIntensityEstimator):

The dataset proper is in /MI_results/MI_ranges_20230905.xlsx

Yes indeed NR = non-residential, RM: MFH, RS: SHF, C: Concrete structure, T: timber structure, S: steel structure, M: masonry

The regions are the 32 SSP regions. 

We recommend using the 25th, median, and 75th percentiles. Especially the 0th and 100th percentiles are not recommended because they tend to capture outliers whose realism can’t be confirmed.

'''

import pandas as pd
import openpyxl
import os

dpath = 'C:\\Users\\Stefan Pauliuk\\FILES\\ARBEIT\\PROJECTS\\Database\\IE_DataCommons\\NEW\\CIRCOMOD'

RASMI_materials  = ['concrete','brick','wood','steel','glass','plastics','aluminum','copper']
iedc_4_materials = ['concrete','bricks','wood','steel','glass','plastics','aluminium','copper']


fn = os.path.join(dpath,'MI_ranges_20230905.xlsx')

li = []

for m in range(0,8):
    ps = pd.read_excel(fn, sheet_name=RASMI_materials[m], index_col=0) # plot sheet
    ps['engineering_material'] = iedc_4_materials[m]
    li.append(ps)
    
RASMI_df = pd.concat(li, axis=0, ignore_index=True)


RASMI_df.to_excel(os.path.join(dpath,'3_MC_RASMI_v20230905_raw.xlsx'), merge_cells=False)  


#
#
#
#
# The end
#
#