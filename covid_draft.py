# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:12:45 2023

@author: Roger
"""

import pandas as pd
import matplotlib.pyplot as plt;
import math;
import numpy as np
# min_keydat = input('Initial date (yyyy-mm-dd): ');
# max_keydat = input('Final date (yyyy-mm-dd): ');
min_keydat = '2020-08-08';
max_keydat = '2021-03-03'
dat_fold = 'DOH_COVID_DATA_DROP';
batch_n = 0;
batch_n = str(batch_n)
casdat_fold = 'C:/Users/Roger/Documents/PYTHON/'+dat_fold+'/';
casdat_l = 'DOH COVID Data Drop_ 20230610 - 04 Case Information_batch_'+batch_n+'.csv'
cas_df = pd.read_csv(f"{casdat_fold}{casdat_l}",index_col=0);
# key_lab_lst = [
#            'Age',
#            'Sex',
#            'DateRepConf',  
#            'RegionRes',];
# field_lst = cas_df.columns;
# cas_key_df = cas_df.dropna(subset=key_lab_lst);
cas_key_df1 = cas_df.drop('ValidationStatus', axis=1);  

# cas1_df = cas_key_df1[
#     (cas_key_df1['Sex'] != 'MALE') & (pd.isna(cas_key_df1['Pregnanttab'])) |
#     (cas_key_df1['Sex'] == 'MALE') & (pd.notna(cas_key_df1['Pregnanttab']))
#     ].index;

cas1_df = cas_key_df1.drop(
    cas_key_df1[
        (cas_key_df1['HealthStatus'] == 'RECOVERED') & (cas_key_df1['RemovalType'] != 'RECOVERED') |
        (cas_key_df1['HealthStatus'] == 'DIED') & (cas_key_df1['RemovalType'] != 'DIED')
        ].index
    );
cas2_df = cas1_df.drop(
    cas1_df[
        (cas1_df['DateSpecimen'] >  cas1_df['DateResultRelease']) |
        (cas1_df['DateResultRelease'] >  cas1_df['DateRepConf'])
        ].index
    );
cas3_df = cas2_df.drop(
    cas2_df[
        (cas2_df['Sex'] != 'MALE') & (pd.isna(cas2_df['Pregnanttab'])) |
        (cas2_df['Sex'] == 'MALE') & (pd.notna(cas2_df['Pregnanttab']))
        ].index
    );

# cas1_df = cas_key_df1.drop(
#     cas_key_df1[
#         (cas_key_df1['Sex'] != 'MALE') & (pd.isna(cas_key_df1['Pregnanttab'])) |
#         (cas_key_df1['Sex'] == 'MALE') & (pd.notna(cas_key_df1['Pregnanttab']))
#         ].index
#     );

# cas2_df = cas1_df.drop(
#     cas1_df[
#         (cas1_df['HealthStatus'] == 'RECOVERED') & (cas1_df['RemovalType'] != 'RECOVERED') |
#         (cas1_df['HealthStatus'] == 'DIED') & (cas1_df['RemovalType'] != 'DIED')
#         ].index
#     );

# cas2_df = cas1_df[
#     (cas1_df['HealthStatus'] == 'RECOVERED') & (cas1_df['RemovalType'] == 'RECOVERED') |
#     (cas1_df['HealthStatus'] == 'DIED') & (cas1_df['RemovalType'] == 'DIED')
#     ];

# cas3_df = cas2_df.drop(
#     cas2_df[
#         (cas2_df['HealthStatus'] == 'RECOVERED') & (pd.isna(cas2_df['DateRecover']))
#         ].index
#     );

# cas3_df = cas2_df[
#     (cas1_df['HealthStatus'] == 'RECOVERED') & (pd.notna(cas2_df['DateRecover']))
#     ];

# cas4_df = cas3_df.drop(
#     cas3_df[
#         (cas3_df['HealthStatus'] == 'DIED') & (pd.isna(cas3_df['DateDied']))
#         ].index  
#     );

# cas5_df = cas4_df.drop(
#     cas4_df[
#         (cas4_df['DateSpecimen'] >  cas4_df['DateResultRelease']) |
#         (cas4_df['DateResultRelease'] >  cas4_df['DateRepConf'])
#         ].index
#     );

# query_plt1 = [
#                 'Query 3',
#                 'Query 4',
#                 'Query 5'
#                 ];
# query_plt2 = [
#                 math.log(len(cas2_df.index)-len(cas3_df.index)),
#                 math.log(len(cas3_df.index)-len(cas4_df.index)),
#                 math.log(len(cas4_df.index)-len(cas5_df.index))
#                 ];

# plt.bar(query_plt1,query_plt2);

# cas5_df = cas5_df.drop(
#     cas5_df[
#         (cas5_df['DateSpecimen'] >  cas5_df['DateResultRelease'])
#         ].index
#     );

# cas4_df = cas3_df[
#     (cas1_df['HealthStatus'] == 'DIED') & (pd.notna(cas3_df['DateDied']))
#     ];

# cas_agegrp = sorted(set(cas_key_df['AgeGroup']));
#data cleaning
# for index, row in cas_cln_df.iterrows():
#     for i in range(0,80,5):
#         cas_cln_df = cas_cln_df[
#             ((cas_cln_df['Age'] >= i) & (cas_cln_df['Age'] <= i+4)) & (cas_cln_df['AgeGroup'] == f'{i} to {i+4}')
#             ];

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

cas5_df = cas4_df.drop(
    cas4_df[
        (cas4_df['HealthStatus'] == 'DIED') & (pd.isna(cas4_df['DateDied']))
        ].index  
    );
cas6_df = cas5_df.drop(
    cas5_df[
        (cas5_df['HealthStatus'] == 'RECOVERED') & (pd.isna(cas5_df['DateRecover']))
        ].index  
    );

cas_adrs_df = cas_key_df1[['RegionRes',
                          'ProvRes',
                          'CityMunRes',
                          'BarangayRes'
                          ]];

cas_adrs_lst = cas_adrs_df.isna().sum(axis=1);
cas_adrs_lst1 = cas_adrs_lst.value_counts()

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

# for i in range(len(dat_lst)-1):
#     for j in range(len(datconf_lst1)-1):
#         if dat_lst['DateRepConf'][i] ==  datconf_lst1['DateRepConf'][j]:
#             dat_lst['Count'][i] =  datconf_lst1['Count'][j]

dat_lst1 = pd.merge(dat_lst,datconf_lst1,how='left',on='DateRepConf');
dat_lst2 = dat_lst1[['DateRepConf','Count_y']].fillna(0);
dat_lst2['Count_y'] = dat_lst2['Count_y'].astype(int);
dat_lst3 = [];
for i in range(len(dat_lst2)):
    dat_lst3.append(dat_lst2['Count_y'][i]+ sum(dat_lst2['Count_y'][:i]))

query_a = [
    ['Query 1',
     'Query 2',
     'Query 3',
     'Query 4',
     'Query 5',
     'Query 6'],
    [len(cas1_df),
     len(cas2_df),
     len(cas3_df),
     len(cas4_df),
     len(cas5_df),
     len(cas6_df)]
    ];
query_a = pd.DataFrame(query_a);
query_a = query_a.transpose();
query_a.to_csv('query_a.csv');
     
# plt.plot(dat_lst['DateRepConf'],dat_lst3)
# if dat_lst['DateRepConf'] == datconf_lst1['DateRepConf']:
#     dat_lst['Count'] = datconf_lst1['Count']

# dat_lst.intersection(datconf_lst1)

# cas_cln_df = cas_key_df[
#     (cas_key_df['RemovalType'] == 'RECOVERED') & (pd.isna(cas_key_df['DateRecover']) == True)
#     ];

# cas_val_df = cas_key_df[pd.isna(cas_key_df['ValidationStatus']) == ''];

#date  
# cas_keydat_df = cas_key_df[[key_lab_lst[0],key_lab_lst[3]]];
#min_keydat = min(cas_keydat_df[key_lab_lst[3]]);
#max_keydat = max(cas_keydat_df[key_lab_lst[3]]);
#import numpy as np;
#set_keydat_lst, set_countdat_lst = np.unique(cas_keydat_df[key_lab_lst[3]],return_counts=True);
#cas_keydat_lst = list(set(cas_keydat_df[key_lab_lst[3]]))
# cas_dat_df = cas_key_df[(cas_key_df[key_lab_lst[3]] >= min_keydat) & (cas_key_df[key_lab_lst[3]] <= max_keydat)];
# import numpy as np
# cas_cntdat_lst = np.unique(cas_keydat_df[key_lab_lst[3]],return_counts=True);
# set_keydat_lst = list(cas_cntdat_lst[0]);
# set_cntdat_lst = list(cas_cntdat_lst[1]);
# lim_keydat_lst = set_keydat_lst[set_keydat_lst.index(min_keydat):set_keydat_lst.index(max_keydat)];
# lim_cntdat_lst = set_cntdat_lst[set_keydat_lst.index(min_keydat):set_keydat_lst.index(max_keydat)];

# plt.bar(lim_keydat_lst,lim_cntdat_lst, 
#         width=0.3, 
#         facecolor = 'k', 
#         alpha=.5);
# #plt.xlim(set_keydat_lst[0],set_keydat_lst[210]);
# # plt.ylim()
# plt.xticks([min_keydat,max_keydat]);
# plt.xlabel("Date confirmed");
# plt.ylabel('Number of cases');
# plt.title("Daily no. of confirmed COVID-19 cases");

#sex
# cas_keyplt_df = cas_dat_df.groupby([key_lab_lst[2],key_lab_lst[3]])[key_lab_lst[0]].count();
# cas_keyplt_p_df = [];
# # sx_lst = ['MALE','FEMALE',''];
# # sx_l = input('Sex: ');
# sx_l = 'MALE';
# if sx_l == 'BOTH':
#     cas_keyplt_p_df =  cas_dat_df
# else:
#     cas_keyplt_p_df = cas_dat_df[cas_dat_df[key_lab_lst[2]] == sx_l];

# cas_keyplt_dfl = cas_keyplt_p_df.groupby(key_lab_lst[3])[key_lab_lst[0]].count();
# cas_keyplt_p_df_1 = cas_keyplt_dfl.index.values.tolist();
# cas_keyplt_p_df_2 = cas_keyplt_dfl.tolist();
# # cas_keyplt_f_df = cas_keyplt_df['FEMALE'].append(cas_keyplt_f_df);
# plt.bar(cas_keyplt_p_df_1,cas_keyplt_p_df_2, 
#         width=0.3, 
#         facecolor = 'k', 
#         alpha=.5);
# plt.xticks([min_keydat,max_keydat]);
# plt.xlabel("Date confirmed");
# plt.ylabel('Number of cases');
# plt.title("Daily no. of confirmed COVID-19 cases");
# cas_keysx_df = cas_key_df[[key_lab_lst[0],key_lab_lst[2]]];
# cas_cntsx_lst = np.unique(cas_keysx_df[key_lab_lst[2]],return_counts=True);

#Determining file name via features
#data_dat= '20230620';
#batch = '0';
#data_name = 'DOH COVID Data Drop_ 20230610 - 04 Case Information_batch_0.csv';
#sheet_n = 'DOH COVID Data Drop_ 20230610 - 02 Metadata - Sheets.csv';
#metadat_n = 'DOH COVID Data Drop_ 20230610 - 03 Metadata - Fields.csv';

#Reading CSV data
#covid_raw = pd.read_csv(f"{data_fold}{data_name}");
#cov_r = pd.read_csv(f"{data_fold}{metadat_n}");
#print labels, sample data, data type
#l1 = 'Sheet';
#l1_list = set(cov_r[l1]) #list of unique sheet data
#l2 = 'Field';
#l2_list = set(cov_r[l2]) #unique field data
#l3 = 'Description';
#l4 = 'Type';
#col_list = cov_r.groupby([l1])[l2].apply(list);
#col_list = col_list.to_list();
#col_list1 = col_list[0]; #label list for 04
#print(col_list1)

#Data sorting
#Label-based sorting
#Demography
#covid_demog = covid_raw[['CaseCode','Age','Sex']]; #float,boolean 
#covid_geog = covid_raw[['CaseCode','RegionRes','ProvRes','CityMunRes','CityMuniPSGC','BarangayRes']]; #string
#covid_status = covid_raw[['CaseCode','Admitted','HealthStatus','Quarantined']]; #boolean
#covid_date = covid_raw[['CaseCode','DateSpecimen','DateResultRelease','DateRepConf','DateDied','DateRecover']]; #date

#Data cleaning
#Omitting NaN/empty values for significant data
#Identified key data: CaseCode, Age, Sex, DateRepConf, RegionRes, HealthStatus
#covid_sample = covid_raw;
#k_lbl = ['DateSpecimen','CaseCode','Age','Sex','DateRepConf','RegionRes','HealthStatus'];
#covid_sample = covid_sample.dropna(subset=k_lbl);
#List key labels

#k = 'DateSpecimen'
#len(k_lbl);
#i = 0;
#k = 0
#while k < len(k_lbl) + 1:
#dt_n = pd.DataFrame(index=index, columns=column);
#for i in range(len(covid_sample)):
#    if pd.isnull(covid_sample.loc[i,k_lbl[0]]):
#        dt_n[] = (covid_sample.loc[i,:])
#    i = i+1;
#covid_test_1 = is_null(covid_sample);
#is_null(covid_raw);
#Omitting data with inconsistencies
#(DateDied<>null && HealthStatus<>DEATH)




