from __future__ import division
import pandas as pd
import numpy as np
import time
import os
import seaborn as sns
import matplotlib.pyplot as plt
import datetime


#creating a mapping function for ages greater than 200 (which are actually months)
def age_conv(n):
    if (n<200):
        return n
    else:
        return round(((n-200)/24), 3)

start = time.time()


#storing disposition info in a pandas dataframe
df_disp = pd.read_csv('Disposition.csv')
#setting its index as code for easier decoding 
df_disp = df_disp.set_index('Code')

#storing diagnosis info in a pandas dataframe
df_diag = pd.read_csv('DiagnosisCodes.csv')
#setting its index as code for easier decoding 
df_diag = df_diag.set_index('Code')

#getting the dataset into a pandas dataframe
df_main = pd.read_csv('NEISS2014.csv')
#applying the mapping function to the age column of the data set for accurate visualization
df_main['age'] = df_main['age'].apply(lambda x: age_conv(x))


################################################################################################################
#grouping the dataset based on disposition, sex, 
group = df_main.groupby(['weight', 'disposition', 'sex'])
#getting the count for each group for further analysis
count_group = group.count()
count_group = count_group.reset_index()
count_group = count_group.ix[:,0:4]
count_group.rename(columns={'CPSC Case #': 'Number of Reported Injuries'}, inplace=True)
#count_group.to_csv('q5.csv')


#plotting the grouped data
g = sns.FacetGrid(count_group, col="disposition",  row="sex")
g = g.map(plt.scatter, "weight", "Number of Reported Injuries", edgecolor="w")


################################################################################################################
#grouping the dataset based on disposition, sex, 
group_r2 = df_main.groupby(['weight', 'trmt_date', 'sex'])
#getting the count for each group for further analysis
count_group_r2 = group_r2.count()
count_group_r2 = count_group_r2.reset_index()
count_group_r2 = count_group_r2.ix[:,0:4]
count_group_r2.rename(columns={'CPSC Case #': 'Number of Reported Injuries', 'trmt_date': 'Date'}, inplace=True)
#print count_group_r2[]
count_group_r2['Date']=count_group_r2['Date'].apply(lambda x:datetime.datetime.strptime(x, '%m/%d/%y').strftime('%Y-%m-%d') )
count_group_r2 = count_group_r2.sort(['Date'])
#count_group_r2.to_csv('q5_r2.csv')


#getting the list of unique dates from the dataset for setting the xtick labels
d_list = np.unique(count_group_r2['Date'].tolist())
d_list2 = []
tc = 0
for a in d_list:
    tc=tc+1
    if (tc%12==0):
        d_list2.append(a)
    else:
        d_list2.append(' ')
#print len(d_list2)


#strip factor plot categorized by male/female
g2 = sns.factorplot( x="Date",y="Number of Reported Injuries",data=count_group_r2, kind="strip", hue="sex")
g2.set_xticklabels(d_list2, rotation=45)


################################################################################################################
#race vs disposition grouping
group_r3 = df_main.groupby(['race', 'disposition', 'sex'])
#getting the count for each group for further analysis
count_group_r3 = group_r3.count()
count_group_r3 = count_group_r3.reset_index()
count_group_r3 = count_group_r3.ix[:,0:4]
count_group_r3.rename(columns={'CPSC Case #': 'Number of Reported Injuries'}, inplace=True)
#count_group_r3.to_csv('q5_r3.csv')

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))
# Plot the number of reported injuries grouped by race
sns.set_color_codes("pastel")
g4 = sns.barplot(x="Number of Reported Injuries", y="race", data=count_group_r3, hue="sex",
             color="red")
g4.set_yticklabels(np.unique(count_group_r3['race'].tolist()), rotation=45)

################################################################################################################
#grouping the dataset based on diagnosis, sex, 
group_r4 = df_main.groupby(['weight', 'diag', 'sex'])
#getting the count for each group for further analysis
count_group_r4 = group_r4.count()
count_group_r4 = count_group_r4.reset_index()
count_group_r4 = count_group_r4.ix[:,0:4]
count_group_r4['diag']=count_group_r4['diag'].apply(lambda x:df_diag['Diagnosis'][x] )
count_group_r4.rename(columns={'CPSC Case #': 'Number of Reported Injuries'}, inplace=True)
#count_group_r4.to_csv('q5_r4.csv')
#generating the plot 
g5 = sns.FacetGrid(count_group_r4, col="sex",  hue="diag")
g5 = (g5.map(plt.scatter, "weight", "Number of Reported Injuries", edgecolor="w")
       .add_legend())

sns.plt.show()



end = time.time()
print '\n total time elapsed: ', (end-start), 'seconds'