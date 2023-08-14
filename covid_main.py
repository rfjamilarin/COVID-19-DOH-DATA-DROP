# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:49:10 2023

@author: Roger
"""

# PRELIMINARIES
import pandas as pd;
import matplotlib.pyplot as plt;

# DATA EXTRACTION
# For backend use: retrieval of CSV data files per specified folder,
# batch number using pandas--
dat_fold = 'PYTHON/DOH_COVID_DATA_DROP';
batch_n = 0;
batch_n = str(batch_n);
casdat_fold = '../'+dat_fold+'/';
casdat_l = 'DOH COVID Data Drop_ 20230610 - 04 Case Information_batch_'+batch_n+'.csv'
cas_df = pd.read_csv(f"{casdat_fold}{casdat_l}");

# DATA CLEANING
# Trimming of batch data based on pre-selected key data features and
# dropping data records with NaN/NA/empty key data record--
key_lab_lst = ['CaseCode',
           'Age',
           'Sex',
           'DateRepConf',
           'RegionRes',];
cas_cln_df = cas_df.dropna(subset=key_lab_lst);
cas_key_df = cas_cln_df;
# Removing the 'Validation Status' field
cas_key_df1 = cas_key_df.drop('ValidationStatus', axis=1);

# SUBQUERY-BASED DATA CLEANING
# Removing records with inconsistent, untimely, & incorrect entries
# on related fields--

# QUERY 1
cas1_df = cas_key_df1.drop(
    cas_key_df1[
        (cas_key_df1['HealthStatus'] == 'RECOVERED') & (cas_key_df1['RemovalType'] != 'RECOVERED') |
        (cas_key_df1['HealthStatus'] == 'DIED') & (cas_key_df1['RemovalType'] != 'DIED')
        ].index
    );
# QUERY 2
cas2_df = cas1_df.drop(
    cas1_df[
        (cas1_df['DateSpecimen'] >  cas1_df['DateResultRelease']) |
        (cas1_df['DateResultRelease'] >  cas1_df['DateRepConf'])
        ].index
    );
# QUERY 3
cas3_df = cas2_df.drop(
    cas2_df[
        (cas2_df['Sex'] != 'MALE') & (pd.isna(cas2_df['Pregnanttab'])) |
        (cas2_df['Sex'] == 'MALE') & (pd.notna(cas2_df['Pregnanttab']))
        ].index
    );
# QUERY 4
cas4_df = cas3_df[
    ((cas3_df['Age'] >= 0) & (cas3_df['Age'] < 5)) & (cas3_df['AgeGroup'] == '0 to 4') |
    ((cas3_df['Age'] >= 5) & (cas3_df['Age'] < 10)) & (cas3_df['AgeGroup'] == '5 to 9') |
    ((cas3_df['Age'] >= 10) & (cas3_df['Age'] < 15)) & (cas3_df['AgeGroup'] == '10 to 14') |
    ((cas3_df['Age'] >= 15) & (cas3_df['Age'] < 20)) & (cas3_df['AgeGroup'] == '15 to 19') |
    ((cas3_df['Age'] >= 20) & (cas3_df['Age'] < 25)) & (cas3_df['AgeGroup'] == '20 to 24') |
    ((cas3_df['Age'] >= 25) & (cas3_df['Age'] < 30)) & (cas3_df['AgeGroup'] == '25 to 29') |
    ((cas3_df['Age'] >= 30) & (cas3_df['Age'] < 35)) & (cas3_df['AgeGroup'] == '30 to 34') |
    ((cas3_df['Age'] >= 35) & (cas3_df['Age'] < 40)) & (cas3_df['AgeGroup'] == '35 to 39') |
    ((cas3_df['Age'] >= 40) & (cas3_df['Age'] < 45)) & (cas3_df['AgeGroup'] == '40 to 44') |
    ((cas3_df['Age'] >= 45) & (cas3_df['Age'] < 50)) & (cas3_df['AgeGroup'] == '45 to 49') |
    ((cas3_df['Age'] >= 50) & (cas3_df['Age'] < 55)) & (cas3_df['AgeGroup'] == '50 to 54') |
    ((cas3_df['Age'] >= 55) & (cas3_df['Age'] < 60)) & (cas3_df['AgeGroup'] == '55 to 59') |
    ((cas3_df['Age'] >= 60) & (cas3_df['Age'] < 65)) & (cas3_df['AgeGroup'] == '60 to 64') |
    ((cas3_df['Age'] >= 65) & (cas3_df['Age'] < 70)) & (cas3_df['AgeGroup'] == '65 to 69') |
    ((cas3_df['Age'] >= 70) & (cas3_df['Age'] < 75)) & (cas3_df['AgeGroup'] == '70 to 74') |
    ((cas3_df['Age'] >= 75) & (cas3_df['Age'] < 80)) & (cas3_df['AgeGroup'] == '75 to 79') |
    (cas3_df['Age'] >= 80) & (cas3_df['AgeGroup'] == '80+') 
    ];
# QUERY 5
cas5_df = cas4_df.drop(
    cas4_df[
        (cas4_df['HealthStatus'] == 'DIED') & (pd.isna(cas4_df['DateDied']))
        ].index  
    );
# QUERY 6
cas6_df = cas5_df.drop(
    cas5_df[
        (cas5_df['HealthStatus'] == 'RECOVERED') & (pd.isna(cas5_df['DateRecover']))
        ].index  
    );
# CSV 1
csv1_lst = [len(cas1_df),len(cas2_df),len(cas3_df),
            len(cas4_df),len(cas5_df),len(cas6_df)];
query_lst = ['Query 1','Query 2','Query 3',
             'Query 4','Query 5','Query 6'];
csv1_df = pd.DataFrame(
    list(
        zip(query_lst,csv1_lst)
        ),
    columns = ['Query','Batch 0']
    );
csv1_df.to_csv('csv1_batch_'+batch_n+'.csv');
# QUERY 7
cas_adrs_df = cas_key_df1[['RegionRes',
                          'ProvRes',
                          'CityMunRes',
                          'BarangayRes'
                          ]];

cas_adrs_lst = cas_adrs_df.isna().sum(axis=1);
cas_adrs_lst1 = cas_adrs_lst.value_counts()
# CSV 2
csv2_df = pd.DataFrame(
    list(
        zip(cas_adrs_lst1)
        ),
    columns = ['Address']
    );
csv2_df.to_csv('csv2_batch_'+batch_n+'.csv');
# QUERY 8
datconf_min = min(cas_df['DateRepConf']);
datconf_max = max(cas_df['DateRepConf']);
dat_lst = pd.date_range(datconf_min,datconf_max,freq='D');
dat_lst = dat_lst.date;
dat_lst = pd.Series(dat_lst).astype(str);
dat_lst = dat_lst.reset_index(drop=True);
dat_lst = dat_lst.rename('DateRepConf').to_frame();

datconf_lst = cas_key_df1[['DateRepConf',
                          'DateDied',
                          'DateRecover'
                          ]];
datconf_lst1 = datconf_lst['DateRepConf'].value_counts().rename_axis('DateRepConf').to_frame('Count');
datconf_lst1 = datconf_lst1.reset_index(names='DateRepConf');
dat_lst['Count'] = 0;
dat_lst1 = pd.merge(dat_lst,datconf_lst1,how='left',on='DateRepConf');
dat_lst2 = dat_lst1[['DateRepConf','Count_y']].fillna(0);
dat_lst2['Count_y'] = dat_lst2['Count_y'].astype(int);
dat_lst3 = [];
for i in range(len(dat_lst2)):
    dat_lst3.append(dat_lst2['Count_y'][i]+ sum(dat_lst2['Count_y'][:i]))

# With cleaned data--
datconf1_lst = cas6_df[['DateRepConf',
                          'DateDied',
                          'DateRecover'
                          ]];
datconf1_lst = datconf1_lst['DateRepConf'].value_counts().rename_axis('DateRepConf').to_frame('Count');
datconf1_lst = datconf1_lst.reset_index(names='DateRepConf');
dat1_lst1 = pd.merge(dat_lst,datconf1_lst,how='left',on='DateRepConf');
dat1_lst2 = dat1_lst1[['DateRepConf','Count_y']].fillna(0);
dat1_lst2['Count_y'] = dat1_lst2['Count_y'].astype(int);
dat1_lst3 = [];
for i in range(len(dat1_lst2)):
    dat1_lst3.append(dat1_lst2['Count_y'][i]+ sum(dat1_lst2['Count_y'][:i]))
    
# CSV 3
csv3_df = pd.DataFrame(
    list(
        zip(dat_lst['DateRepConf'],dat_lst3,dat1_lst3)
        ),
    columns = ['DateRepConf','Conf','ConfNew']
    );
csv3_df.to_csv('csv3_batch_'+batch_n+'.csv');
