# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 18:14:25 2023

@author: Roger
"""

import pandas as pd;
cov_csv = ['csv1_batch_0.csv',
           'csv1_batch_1.csv',
           'csv1_batch_2.csv',
           'csv1_batch_3.csv',
           'csv1_batch_4.csv'];
cov1_df = pd.DataFrame();
for file in cov_csv:
    cov_dat = pd.read_csv(file)
    cov_dat = cov_dat['Batch 0'].to_frame()
    cov1_df = pd.concat([cov1_df,cov_dat], axis=1)
cov1_df.to_csv('cov1.csv', index=False);

cov2_csv = ['csv2_batch_0.csv',
           'csv2_batch_1.csv',
           'csv2_batch_2.csv',
           'csv2_batch_3.csv',
           'csv2_batch_4.csv'];
cov2_df = pd.DataFrame();
for file in cov2_csv:
    cov_dat = pd.read_csv(file)
    cov_dat = cov_dat['Address'].to_frame()
    cov2_df = pd.concat([cov2_df,cov_dat], axis=1)
cov2_df.to_csv('cov2.csv', index=False);

cov3_csv = ['csv3_batch_0.csv',
           'csv3_batch_1.csv',
           'csv3_batch_2.csv',
           'csv3_batch_3.csv',
           'csv3_batch_4.csv'];
cov_ind = pd.read_csv('csv3_batch_0.csv')['DateRepConf'];
cov3_df = pd.DataFrame();
cov3_df = pd.concat([cov_ind],axis=1);
for file in cov3_csv:
    cov_dat = pd.read_csv(file)
    cov_dat = cov_dat['Conf'].to_frame()
    cov3_df = pd.concat([cov3_df,cov_dat], axis=1)
cov3_df.to_csv('cov2.csv', index=False);