import math
import numpy as np


with open('input.txt') as f:
    instructions = f.readlines()

# Modify instruction format to get each instruction as a list of [direction, distance]
instructions = [instruction.rstrip() for instruction in instructions]
instructions = [instruction.split() for instruction in instructions]

for i in instructions:
    i[1] = int(i[1])

# Def movement function 
def move(positionpath, instruction):
    position = positionpath[-1]
    direction = instruction[0]
    steps = instruction[1]

    for i in range(steps):
        if direction == "U":
            position = (position[0],position[1] + 1)
            positionpath.append(position)
        elif direction == "D":
            position = (position[0],position[1] - 1)
            positionpath.append(position)
        elif direction == "R":
            position = (position[0] + 1,position[1])
            positionpath.append(position)
        elif direction == "L":
            position = (position[0] - 1,position[1])
            positionpath.append(position)
        else:
            print("There are other directions")
    return positionpath

H = [(0,0)] # positions as tuple not list because they are immutable
T = [(0,0)]

# Create path of H 
for instruction in instructions:
    H = move(H, instruction)

# Create path of T
for i in range(1, len(H)):
    Hpos = H[i]
    Tpos = T[-1]
    dist = math.dist(Hpos, Tpos)

    if dist < 1.5:
        # This means touching, because diagonally touching has dist root(2) = 1.41
        T.append(Tpos) # stays where it is 
    else: 
        vector = [(Hpos[0] - Tpos[0]), (Hpos[1] - Tpos[1])] # Direction from T to H
        stepvector = np.sign(vector) # Converts this to +1, 0 or -1 
        Tpos = (Tpos[0] + stepvector[0], Tpos[1] + stepvector[1]) # Updates T
        T.append(Tpos)

Tvisits = len(dict.fromkeys(T)) #calculates number of distinct tuples
print(Tvisits)

# Part 2 

# Define a generic movement fucntion 
def follow(Hpos, Tpos): 

    dist = math.dist(Hpos, Tpos)

    if dist < 1.5:
        newT = Tpos #stays where it is 
    else: 
        vector = [(Hpos[0] - Tpos[0]), (Hpos[1] - Tpos[1])] # Direction from T to H
        stepvector = np.sign(vector) # Converts this to +1, 0 or -1 
        newT = (Tpos[0] + stepvector[0], Tpos[1] + stepvector[1]) # Updates T

    return newT

positions = [[(0,0) for i in range(10)]] #The positions of H,1,2,3,4,5,6,7,8,9

for i in range(1, len(H)):
    positionsPostStep = []
    currentH = H[i]
    positionsPostStep.append(currentH) # first item in the list is H position which is already calculated
    for j in range(1,10):
        leader = positionsPostStep[-1]
        follower = positions[-1][j] # the position of the knot in question at the end of the last step 
        newPos = follow(leader, follower)
        positionsPostStep.append(newPos) # calcs the new positions of knots 1 to 9 and adds them to the list of positions post step 
    positions.append(positionsPostStep)


tailPositions = []
for i in range(len(positions)):
    tailPos = positions[i][-1] #Where is the tail 
    tailPositions.append(tailPos)

T9visits = len(dict.fromkeys(tailPositions)) #calculates number of distinct tuples
print(T9visits)