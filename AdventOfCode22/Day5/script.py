import pandas as pd 
import numpy as np

file  = open("Starter.txt","r")

df = []

for line in file:
    if line != "\n":
        df.append(line)
    else:
        print("There are blanks")
  
file.close()

## Read in crates

height = int(len(df)) - 1
width = 9
crates_list = {}
# would have been better to use crates_dict = {i: [] for i in range(1,10)}

for i in range(width):
    key = i + 1
    crates_list[key] = []
    for j in range(height):
        # Noting that the letters are every 4th character taking account of the spaces and brackets between them
        location = 4*i + 1
        if df[j][location] != " ":
            box = df[j][location]
            crates_list[key].append(box)


for i in range(width):
    crates_list[i+1].reverse()



## Read in instructions 

file2  = open("Instructions.txt","r")

instructions = []

for line in file2:
    if line != "\n":
        instructions.append(line)
    else:
        print("There are blanks")
  
file2.close()

instructions = np.array(instructions)
instructions = instructions.T
instructions = pd.DataFrame(instructions, columns = ['Instruction'])

instructions['Instruction'] = instructions['Instruction'].str.split(" ", expand = False)
instructions = pd.DataFrame(instructions['Instruction'].to_list(), columns=['move', 'quantity','spare', 'start','spare2', 'end'])
instructions = instructions.replace(r'\n','', regex=True) 
instructions = instructions.drop(["move","spare","spare2"], axis = 1)

# def the function for updating the crates

def movecrates(input_dict, quantity, start, end):
    counter = 0 

    dict = input_dict

    """
    while counter < quantity: 

        mover = dict[start].pop()

        dict[end].append(mover)

        counter += 1
    """

    # Move them as a block by copying

    mover = []
    mover = mover + dict[start][-quantity:]
    dict[end] = dict[end] + mover

    # Remove them from original location 

    while counter < quantity:
        dict[start].pop()
        counter += 1
    
    return dict


instructions_length = len(instructions)

for i in range(instructions_length):

    quantity = int(instructions["quantity"][i])
    start = int(instructions["start"][i])
    end = int(instructions["end"][i])

    movecrates(crates_list, quantity, start, end)


for i in range(1,10):
    print(crates_list[i][-1],end="")
    # end specifies what follows each print statement. Default is \n