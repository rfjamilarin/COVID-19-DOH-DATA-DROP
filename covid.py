# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:00:11 2023

@author: Roger
"""
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

#CSV reading via file path
#Determining file folder


# def lab_f(dat_fold,n):
#     n = int(n)
#     metadat_l = 'DOH COVID Data Drop_ 20230610 - 03 Metadata - Fields.csv';
#     dat_fold = '../'+dat_fold+'/';
#     metadat_df = pd.read_csv(f"{dat_fold}{metadat_l}");
#     l1 = 'Sheet';
#     l2 = 'Field';
#     n = n-4;
#     lab_lst = metadat_df.groupby([l1])[l2].apply(list);
#     lab_lst = lab_lst.to_list();
#     lab_lst = lab_lst[n];
#     sheet_lst = list(sorted(set(metadat_df[l1])));
#     sheet_n = sheet_lst[n];
#     return lab_lst, sheet_n;

def main():
    #dat_fold = input('Location of data: ');
    dat_fold = 'DOH_COVID_DATA_DROP';
    #sheet_code_n = input('Sheet code: ')
    # lab_lst, sheet_n = lab_f(dat_fold,sheet_code_n);
    
    #print(lab_lst);
    #print(lab_f(dat_fold,sheet_code_n)[0][10]) #access specific label 'label1'
    
    # min_keydat = input('Initial date (yyyy-mm-dd): ');
    # max_keydat = input('Final date (yyyy-mm-dd): ');
    
    batch_n = 0;
    batch_n = str(batch_n)
    casdat_fold = '../'+dat_fold+'/';
    casdat_l = 'DOH COVID Data Drop_ 20230610 - 04 Case Information_batch_'+batch_n+'.csv'
    cas_df = pd.read_csv(f"{casdat_fold}{casdat_l}");
    key_lab_lst = ['CaseCode',
               'Age',
               'Sex',
               'DateRepConf',
               'RegionRes',];
    cas_cln_df = cas_df.dropna(subset=key_lab_lst);
    cas_key_df = cas_cln_df[key_lab_lst];
    
    #date
    # cas_keydat_df = cas_key_df[[key_lab_lst[0],key_lab_lst[3]]];
    # cas_cntdat_lst = np.unique(cas_keydat_df[key_lab_lst[3]],return_counts=True);
    # set_keydat_lst = list(cas_cntdat_lst[0]);
    # set_cntdat_lst = list(cas_cntdat_lst[1]);
    # lim_keydat_lst = set_keydat_lst[set_keydat_lst.index(min_keydat):set_keydat_lst.index(max_keydat)];
    # lim_cntdat_lst = set_cntdat_lst[set_keydat_lst.index(min_keydat):set_keydat_lst.index(max_keydat)];

    # plt.bar(lim_keydat_lst,lim_cntdat_lst, 
    #         width=0.3, 
    #         facecolor = 'k', 
    #         alpha=.5);
    # plt.xticks([min_keydat,max_keydat]);
    # plt.xlabel("Date confirmed");
    # plt.ylabel('Number of cases');
    # plt.title("Daily no. of confirmed COVID-19 cases");
    
    #sex
    cas_keysx_df = cas_key_df[[key_lab_lst[0],key_lab_lst[2]]];
    cas_cntsx_lst = np.unique(cas_keysx_df[key_lab_lst[2]],return_counts=True);
    
if __name__ == "__main__":
    main()    