
import pandas as pd 
import numpy as np

# Can skip all the rigmarole down to where I have the 2 column df that I want with: df = pd.read_csv("input.txt", delimiter=" ", header=None, names = ['Opponent', 'Self'])

df = pd.read_csv("input.txt", delimiter=" ", header=None, names = ['Opponent', 'Self'])

'''
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
df = pd.DataFrame(df, columns = ['Opponent'])

df['Opponent'] = df['Opponent'].str.split(" ", n = 1, expand = False)
df = pd.DataFrame(df['Opponent'].to_list(), columns=['Opponent', 'Self'])
df = df.replace(r'\n','', regex=True) 

'''


# Create the scoring matrics 

self_score = {'X' : 1,
              'Y' : 2,
              'Z' : 3}

game_score = {
    'A' : {
        'X' : 3,
        'Y' : 6,
        'Z' : 0   
     },
    'B' : {
        'X' : 0,
        'Y' : 3,
        'Z' : 6   
     },
    'C' : {
        'X' : 6,
        'Y' : 0,
        'Z' : 3   
     }
    }

def calc_score(opponent, self):
    points = 0 
    points += self_score[self]
    points += game_score[opponent][self]
    return points


df ['Points'] = df.apply(lambda row : calc_score(row['Opponent'], row['Self']), axis = 1)

print(sum(df['Points']))

# Part 2 - Reinterpret strat guide 

game_choice = {
    'A' : {
        'X' : 'Z',
        'Y' : 'X',
        'Z' : 'Y'   
     },
    'B' : {
        'X' : 'X',
        'Y' : 'Y',
        'Z' : 'Z'   
     },
    'C' : {
        'X' : 'Y',
        'Y' : 'Z',
        'Z' : 'X'   
     }
    } 

def choose_action(opponent, self):
    action = game_choice[opponent][self]
    return action

df['Choice'] = df.apply(lambda row : choose_action(row['Opponent'], row['Self']), axis = 1)
df ['Points2'] = df.apply(lambda row : calc_score(row['Opponent'], row['Choice']), axis = 1)


print(sum(df['Points2']))