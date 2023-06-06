import pandas as pd

### Part 1 
## Section: Reading in the input (description of rock lines) and making them operable 

with open('input.txt') as f:
    rocks = f.read().splitlines()

# Takes in 1 line of instructions and returns a tuple each element of which is a tuple containing the
# start and end coordinates of the rock line

def coordsFromString(string, lines):
    string = string.split(" -> ")
    for i in range(len(string) - 1):
        start = string[i].split(",")
        startTup = (int(start[0]), int(start[1]))
        end = string[i+1].split(",")
        endTup = (int(end[0]), int(end[1]))
        line = ((startTup, endTup))
        lines.append(line)
    return lines

# Find the max and min coordinates for the rock lines 

def findBounds(lines):
    minX, minY, maxX, maxY = lines[0][0][0], lines[0][0][1], lines[0][0][0], lines[0][0][1] #Sets min and max values to the first point

    for i in range(len(lines)):
        # Looks at the starting point of all the lines
        if lines[i][0][0] > maxX:
            maxX = lines[i][0][0]
        if lines[i][0][1] > maxY:
            maxY = lines[i][0][1]
        if lines[i][0][0] < minX:
            minX = lines[i][0][0]
        if lines[i][0][1] < minY:
            minY = lines[i][0][1]
        # Looks at the end point of all lines - could be more efficient as many points are being checked twice
        if lines[i][1][0] > maxX:
            maxX = lines[i][1][0]
        if lines[i][1][1] > maxY:
            maxY = lines[i][1][1]
        if lines[i][1][0] < minX:
            minX = lines[i][1][0]
        if lines[i][1][1] < minY:
            minY = lines[i][1][1] 
    return(minX, minY, maxX, maxY)

# Read in the input file and put everything into a list of lines of rock
rockLines = []
for i in range(len(rocks)):
    rockLines = coordsFromString(rocks[i], rockLines)
bounds = findBounds(rockLines)   

## Section: Setting up the model of the cave with space and rock lines 

# Create an image of a cave 
height = bounds[3] + 1 #MaxY + 1 to zero index
xAxis = range(bounds[0], bounds[2] + 1) #MinX to MaxX inclusive 
cave = pd.DataFrame(".", index=range(height), columns=xAxis)

# Add a row below the lowest layer of rock indicating that everything past this point is lost to the abyss
newRow = ["~"] * len(xAxis)
cave.loc[len(cave)] = newRow
# Add columns on either side showing that anything past this point is lost to the abyss
newMinX = bounds[0] - 1
newMaxX = bounds[2] + 1
newCol = ["~"] * (height + 1)
cave.insert(0, newMinX, newCol, True)
cave[newMaxX] = newCol

# Def the function to add the rock lines
def addRockLine(rockLine, cave):
    if rockLine[0][0] == rockLine[1][0] and rockLine[0][1] != rockLine[1][1]: # Is a vertical line
         x = rockLine[0][0]
         for i in range(min(rockLine[0][1], rockLine[1][1]), max(rockLine[0][1], rockLine[1][1]) + 1):
             cave[x][i] = "#"
    elif rockLine[0][0] != rockLine[1][0] and rockLine[0][1] == rockLine[1][1]: #is a horizontal line
        y = rockLine[0][1]
        for i in range(min(rockLine[0][0], rockLine[1][0]), max(rockLine[0][0], rockLine[1][0]) + 1):
            cave[i][y] = "#"
    return cave
# Add the rock lines
for i in range(len(rockLines)):
    cave = addRockLine(rockLines[i], cave)

## Section: Simulating the sand falling into the cave 

# Some global variables 
startingPos = (500,0)
abyss = False
blocked = False

def sandFall(startingPos, cave):
    global abyss
    global blocked
    falling = True
    # This if condition is only relevant for Part 2 where we are checking if the starting position is already blocked before adding a new sand
    if cave[500][0] == "o":
        falling = False
        blocked = True  
        return cave
    # Part 1 always hits this else condition. 
    else: 
        sandPos = startingPos
    
    def isFree(cave, pos):
        global abyss 
        if cave[pos[0]][pos[1]] == ".":
            return True
        elif cave[pos[0]][pos[1]] == "o" or cave[pos[0]][pos[1]] == "#":
            return False
        elif cave[pos[0]][pos[1]] == "~":
            print("ABYSS!!!!")
            abyss = True
            return False

    while(falling):
        # Check if sand can fall vertically
        newPos = (sandPos[0], sandPos[1] + 1)
        if isFree(cave, newPos):
            sandPos = newPos
        # Else check if sand can fall diagonally left
        else:
            newPos = (sandPos[0] - 1, sandPos[1] + 1)
            if isFree(cave, newPos):
                sandPos = newPos
            # Else check if sand can fall diagonally right
            else:  
                newPos = (sandPos[0] + 1, sandPos[1] + 1)
                if isFree(cave, newPos):
                    sandPos = newPos
                # Otherwise sand can't move so we update and print
                else:
                    cave[sandPos[0]][sandPos[1]] = "o"
                    # print(cave)
                    falling = False
                    return(cave)

## Section: Answers

# Part 1
counter = 0
while(not(abyss)):
    counter += 1
    cave = sandFall(startingPos, cave)

print(counter - 1)
print(cave)


### Part 2 

## Section: Setting up a new, bigger cave

# Create an image of the cave allowing maximum width for sand to flow into 
height = bounds[3] + 2 #MaxY + 1 to zero index and + 1 for the air gap above the floor. We later add a row for the floor. 
newMinX = 300
newMaxX = 700
xAxis = range(newMinX + 1, newMaxX) # Guess at how wide it needs to be before reaching the ceiling. Ran with a smaller cave and observed hitting 
# the edge with the abyss flag so made bigger. It might be possible with a slightly smaller cave
cave2 = pd.DataFrame(".", index=range(height), columns=xAxis)

# Add the floor 
newRow = ["#"] * len(xAxis)
cave2.loc[len(cave2)] = newRow

# Add columns on either side showing that anything past this point is lost to the abyss - and will therefore need a wider cave
newCol = ["~"] * (height + 1)
cave2.insert(0, newMinX, newCol, True)
cave2[newMaxX] = newCol

# Add rock lines 
for i in range(len(rockLines)):
    cave2 = addRockLine(rockLines[i], cave2)

## Section: Answers

counter = 0
# Need to reset abyss which was changed in part 1
abyss = False

while(not(abyss or blocked)):
        counter += 1
        cave2 = sandFall(startingPos, cave2)

print(counter - 1)
print(cave2)
