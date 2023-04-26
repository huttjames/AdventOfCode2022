import pandas as pd 
import numpy as np
from textwrap import wrap

import time
start_time = time.time()

file  = open("input.txt","r")

df = []

for line in file:
    if line != "\n":
        df.append(line)
    else:
        print("There are blanks")
  
file.close()

def my_intersection(str1, str2):
    res = ''.join(sorted(set(str1) &
         set(str2), key = str1.index))
    return res

def calc_priority(character):
    x = ord(character)
    # Z is 90, the capital letters come first. So if x < 91 it means its a capital letter 
    if x < 91: 
        x -= 38
    else: 
        x -= 96
    return x


df = np.array(df)
df = df.T
df = pd.DataFrame(df, columns = ['Contents'])
df = df.replace(r'\n','', regex=True) 

df ['HalfLen'] = df.apply(lambda row : int(len(row['Contents']) * 0.5), axis = 1)
df ['Split'] = df.apply(lambda row : wrap(row['Contents'], row['HalfLen']), axis = 1)


df1 = pd.DataFrame(df['Split'].to_list(), columns=['Comp1', 'Comp2'])
df1 ['Intersect'] = df1.apply(lambda row : my_intersection(row['Comp1'],row['Comp2']), axis = 1)
df1 ['Priority'] = df1.apply(lambda row : calc_priority(row['Intersect']), axis = 1)

print(sum(df1['Priority']))

# Part 2
df2 = pd.DataFrame()
df_temp = df['Contents']
M1 = df_temp[df_temp.index % 3 == 0].reset_index()
M2 = df_temp[df_temp.index % 3 == 1].reset_index()
M3 = df_temp[df_temp.index % 3 == 2].reset_index()

M1 = M1['Contents']
M2 = M2['Contents']
M3 = M3['Contents']

df2['M1'] = M1
df2['M2'] = M2
df2['M3'] = M3

df2['Intersect1'] = df2.apply(lambda row : my_intersection(row['M1'],row['M2']), axis = 1)
df2['Intersect2'] = df2.apply(lambda row : my_intersection(row['Intersect1'],row['M3']), axis = 1)
df2['Priority'] =  df2.apply(lambda row : calc_priority(row['Intersect2']), axis = 1)

print(sum(df2['Priority']))
print("--- %s seconds ---" % (time.time() - start_time))