from __future__ import division
import pandas as pd
import numpy as np
import time
import os

start = time.time()


#storing disposition info in a pandas dataframe
df_disp = pd.read_csv('Disposition.csv')
#setting its index as code for easier decoding 
df_disp = df_disp.set_index('Code')
#print df_disp

#storing diagnosis info in a pandas dataframe
df_diag = pd.read_csv('DiagnosisCodes.csv')
#setting its index as code for easier decoding 
df_diag = df_diag.set_index('Code')
#print df_diag

#getting the dataset into a pandas dataframe
df_main = pd.read_csv('NEISS2014.csv')

#grouping the dataset based on disposition and diagnosis
group_disp_diag = df_main.groupby(['disposition', 'diag'])
#getting the count for each group for further analysis
count_disp_diag = group_disp_diag.count()
count_disp_diag = count_disp_diag.reset_index()
count_disp_diag = count_disp_diag.ix[:,0:3]
#setting index back to disposition for easier slicing of dataframe
count_disp_diag = count_disp_diag.set_index('disposition')
#count_disp_diag.to_csv('disp_diag_test.csv')

#storing hospitalization cases in a separate frame
hosp = count_disp_diag.ix[2:5,:]
hosp = hosp.sort('CPSC Case #', ascending=False)
hosp = hosp.reset_index()
#storing the highest hospitalization rate in another dataframe
highest_hosp = hosp.ix[0:0,:]

print df_diag['Diagnosis'][highest_hosp['diag'][0]], 'has the highest hospitalization rate \n'
#hosp.to_csv('hospitalized.csv')

#storing left without seeing cases in a separate frame
nosee = count_disp_diag.ix[6,:]
nosee = nosee.sort('CPSC Case #', ascending=False)
nosee=nosee.reset_index()

#storing the highest left without seen rate in another dataframe
highest_nosee=nosee.ix[0:3,:]
#print highest_nosee
print df_diag['Diagnosis'][highest_nosee['diag'][1]], 'diagnosed incidents were most often left without being seen  \n'



end = time.time()
print '\n total time elapsed: ', (end-start), 'seconds'