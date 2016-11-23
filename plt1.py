from __future__ import division
import pandas as pd
import numpy as np
import time
import os
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt


#creating a mapping function for ages greater than 200 (which are actually months)
def age_conv(n):
    if (n<200):
        return n
    else:
        return round(((n-200)/24), 3)

start = time.time()


#getting the dataset into a pandas dataframe
df_main = pd.read_csv('NEISS2014.csv')

#applying the mapping function to the age column of the data set for accurate visualization
df_main['age'] = df_main['age'].apply(lambda x: age_conv(x))

#getting the list of unique ages from the dataset for setting the xtick labels
age_list = np.unique(df_main['age'].tolist())
age_list2 = []
#print len(age_list)
tc = 0
for a in age_list:
    tc=tc+1
    if (tc%5==0):
        age_list2.append(a)
    else:
        age_list2.append(' ')


#grouping the dataset based on disposition and diagnosis
group_age = df_main.groupby(['age'])
group_age_count = group_age.count()

group_age_count = group_age_count.reset_index()
#group_age.count().to_csv('age_group_count.csv')
group_age_count.rename(columns={'CPSC Case #': 'Number of Reported Injuries', 'age': 'Age (years)'}, inplace=True)

#generating a seaborn factorplot to show the relationship of age vs number of incidents reported in the dataset
g = sns.factorplot(data=group_age_count, x="Age (years)", y="Number of Reported Injuries")
axes = g.axes
axes[0,0].set_ylim(-50,2300)
g.set_xticklabels(age_list2, rotation=45)
g.fig.suptitle('FactorPlot - Number of Reported Injuries vs. Age')

#generating seaborn regplot for the same dataset
chart2, ax2 = plt.subplots()
g2 = sns.regplot(x="Age (years)", y="Number of Reported Injuries", data=group_age_count, color='red', ax=ax2);

sns.plt.show()

end = time.time()
print '\n total time elapsed: ', (end-start), 'seconds'