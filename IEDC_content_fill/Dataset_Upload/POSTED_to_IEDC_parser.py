# -*- coding: utf-8 -*-
"""
posted-v0.4.0 to IEDC parser

https://github.com/PhilippVerpoort/posted
https://zenodo.org/records/18155305

Created on Thu Feb 12 06:33:43 2026

@author: Stefan Pauliuk
"""

import pandas as pd
import os

inpath = 'C:\\Users\\Stefan Pauliuk\\FILES\\ARBEIT\\PROJECTS\\Database\\IE_DataCommons\\NEW\\_NEW_RAW_DATA\\POSTED\\PhilippVerpoort-posted-9facc5b\\inst\\extdata\\database\\tedfs\\Tech'
directory = os.fsencode(inpath)

all_datasets = []
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"): 
        print(filename)
        ps = pd.read_csv(os.path.join(inpath,filename), index_col=None) # plot sheet
        ps.insert(loc=0, column='process', value=filename)
        if 'subtech' not in ps.columns:
            ps.insert(loc=1, column='subtech', value='')
        if 'component' not in ps.columns:
            ps.insert(loc=3, column='component', value='')
        all_datasets.append(ps)

main = pd.concat(all_datasets, axis=0, ignore_index=True)

main.to_excel('POSTED_all.xlsx')
