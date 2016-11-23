from __future__ import division
import pandas as pd
import numpy as np
import time
import os

start = time.time()

#getting the dataset into a pandas dataframe
df_main = pd.read_csv('NEISS2014.csv')

#setting count of injuries involving skateboard to 0 (will increment if the injury involves skateboard), male count , female count, age count
count_sb=0
count_male = 0
count_female = 0
count_age = 0
#exclude longboarding,  walking up
for index, row in df_main.iterrows():
    if (('SKATEBOARD' in row['narrative'] or 'SKATE BOARD' in row['narrative'] or 'SKATEBOAD' in row['narrative']) and 'LONG' not in row['narrative'] and 'WALKING UP' not in row['narrative'] ):
        count_sb=count_sb+1
        #print row['narrative']
        #checking if there are erroneous numbers provided in age because there are some (but not in the ones involving skateboard)
        #if (row['age']>40):
            #print row['age'], row['narrative']
        count_age = count_age+row['age']
        if (row['sex'] == 'Male'):
            count_male=count_male+1
        else:
            count_female=count_female+1

#print count_age
#print count_male, count_female, count_male+count_female
print 'number of injuries in this dataset involving a skateboard are: ', count_sb
print 'percentage male: ', (count_male/count_sb)*100, '%'
print 'percentage Female: ', (count_female/count_sb)*100,  '%'
print 'average age: ', count_age/count_sb


end = time.time()
print '\n total time elapsed: ', (end-start), 'seconds'