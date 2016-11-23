import pandas as pd
import numpy as np
import time
import os

start = time.time()

#storing bodyparts info in a pandas dataframe
df_bodyparts = pd.read_csv('BodyParts.csv')
#setting its index as code for easier decoding 
df_bodyparts = df_bodyparts.set_index('Code')
#print df_bodyparts

#getting the dataset into a pandas dataframe
df_main = pd.read_csv('NEISS2014.csv')

#grouping the results by body part in a groupby object
group_main = df_main.groupby('body_part')

#performing the count aggregation on the groupby object on the body_part column
count_frame= group_main.count()

#getting rid of the other columns and only retaining the count column with body part index and the following line renames the columns
count_frame = count_frame.ix[:, 0:1] 
count_frame.rename(columns={'CPSC Case #': 'Count'}, inplace=True)
#sorting in ascending order of count and then resetting the index to slice the most and least frequently represented body parts
count_frame = count_frame.sort('Count') 
count_frame = count_frame.reset_index()

#print count_frame

#slicing the count frame to get most and least frequently represented body parts in the dataset
least_frequent = count_frame.ix[0:3,]
most_frequent = count_frame.ix[count_frame.shape[0]-3:,]
most_frequent = most_frequent.sort('Count', ascending=False)
#print least_frequent
#print count_frame.columns.values
#count_frame.to_csv('testcount.csv')

print "the top 3 most frequently represented body parts in the data set are: "
for x in most_frequent['body_part'].tolist():
    print df_bodyparts['BodyPart'][x]
print '\n' 

#removing "not recorded" body parts from the result because it is meaningless
least_frequent_list = least_frequent['body_part'].tolist()
least_frequent_list.remove(87)

print "the top 3 lest frequently represented body parts in the data set are: "
for y in least_frequent_list:
    print df_bodyparts['BodyPart'][y]

end = time.time()
print '\n total time elapsed: ', (end-start), 'seconds'