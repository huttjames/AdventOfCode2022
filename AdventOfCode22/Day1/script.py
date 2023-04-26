import pandas as pd 
import numpy as np


file  = open("starter.txt","r")

df = []
df_elf = []

for line in file:
    if line != "\n":
        df_elf.append(int(line))
    else:
        df.append(df_elf)
        df_elf = []
  
df.append(df_elf)
file.close()

elf_totals = []

for elf in range(len(df)):
    total = sum(df[elf])
    elf_totals.append(total)

'''
elf_totals = np.array(elf_totals)
elf_totals = np.sort(elf_totals)
'''

elf_totals.sort()

print(sum(elf_totals[-3:]))



