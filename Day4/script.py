import pandas as pd 
import numpy as np


file  = open("input.txt","r")

df = []

for line in file:
    if line != "\n":
        df.append(line)
    else:
        print("There are blanks")
  
file.close()

df = np.array(df)
df = df.T
df = pd.DataFrame(df, columns = ['Pair'], dtype = "str")

df['Pair'] = df['Pair'].str.split(",", n = 1, expand = False)
df = pd.DataFrame(df['Pair'].to_list(), columns=['Elf1', 'Elf2'])
df = df.replace(r'\n','', regex=True) 

df['Elf1'] = df['Elf1'].str.split("-", n = 1, expand = False)
df['Elf2'] = df['Elf2'].str.split("-", n = 1, expand = False)

df1 = pd.DataFrame(df['Elf1'].to_list(), columns=['Start1', 'End1'])
df2 = pd.DataFrame(df['Elf2'].to_list(), columns=['Start2', 'End2'])

df['Start1'] = df1['Start1']
df['End1'] = df1['End1']
df['Start2'] = df2['Start2']
df['End2'] = df2['End2']

def my_intersection(start1, end1, start2, end2):
    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)
    end2 = int(end2)
    list1 = range(start1, end1 + 1)
    list2 = range(start2, end2 + 1)

    flag = 0 

    if(all(x in list1 for x in list2)):
        flag = 1

    if(all(x in list2 for x in list1)):
        flag = 1

    return flag


df['Subset'] = df.apply(lambda row : my_intersection(row['Start1'], row['End1'], row['Start2'], row['End2']), axis = 1)

print(sum(df['Subset']))


#Part 2

def my_overlap(start1, end1, start2, end2):
    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)
    end2 = int(end2)
    list1 = range(start1, end1 + 1)
    list2 = range(start2, end2 + 1)

    flag = 0 

    overlap = list(set(list1) & set(list2))

    if overlap != []:
        flag = 1

    return flag

df['Overlap'] = df.apply(lambda row : my_overlap(row['Start1'], row['End1'], row['Start2'], row['End2']), axis = 1)

print(sum(df['Overlap']))