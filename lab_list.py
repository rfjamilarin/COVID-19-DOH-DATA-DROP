# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:12:45 2023

@author: Roger
"""

def lab_lst(dat_fold,n):
    import pandas as pd;
    n = int(n)
    metadat_l = 'DOH COVID Data Drop_ 20230610 - 03 Metadata - Fields.csv';
    dat_fold = '../'+dat_fold+'/';
    metadat_df = pd.read_csv(f"{dat_fold}{metadat_l}");
    l1 = 'Sheet';
    l2 = 'Field';
    n = n-4;
    lab_lst = metadat_df.groupby([l1])[l2].apply(list);
    lab_lst = lab_lst.to_list();
    lab_lst = lab_lst[n];
    sheet_lst = list(sorted(set(metadat_df[l1])));
    sheet_n = sheet_lst[n];
    return lab_lst, sheet_n;