
import numpy as np

with open('input.txt') as f:
    trees = f.readlines()

for row in range(len(trees)):
    trees[row] = trees[row].rstrip()
    trees[row] = [*trees[row]]
    trees[row] = list(map(int, trees[row]))

trees = np.array(trees)

height = len(trees)
width = len(trees[0])
visibletrees = np.zeros_like(trees)

def linesofsight(array2d, i, j):
    if array2d.ndim != 2:
        print("wrong sized array - only takes 2d arrays")
        return

    left = array2d[i, 0:j]
    right = array2d[i, j+1:]
    up = array2d[0:i, j]
    down = array2d[i+1:,j]

    return [left, right, up, down], [max(left, default=-1), max(right, default=-1), max(up, default=-1), max(down, default=-1)]


for i in range(height):
    for j in range(width):
        blockers = linesofsight(trees,i,j)[1]
        tree = trees[i,j]
        if tree > min(blockers):
            visibletrees[i, j] = 1

# Part 1 - note np sum returns the sum of all elements, whereas sum would return the row-wise sum
print(np.sum(visibletrees))


# Part 2 
# There is probably a generalizable function which looks something like 
# 1. For left and up reverse the list 
# 2. Input to function the value of the tree and the list 
# 3. Return the argument of the first element in the list which is >= the value of the tree
# 4. This could then be applied to each of the lines of sight, rather than rewriting the calculation

scenictrees = np.zeros_like(trees)

for i in range(height):
    for j in range(width):

        views = linesofsight(trees,i,j)[0]
        tree = trees[i,j]

        leftscore = 0 
        left = views[0]
        if len(left) != 0:
            leftscore = 1
            for k in range(1, len(left)):
                if tree > left[-k]:
                    leftscore += 1
                else:
                    break
                
        rightscore = 0
        right = views[1]
        if len(right) != 0:
            rightscore = 1
            for k in range(0, len(right) - 1):
                if tree > right[k]:
                    rightscore += 1
                else:
                    break

        upscore = 0
        up = views[2]
        if len(up) != 0:
            upscore = 1
            for k in range(1, len(up)):
                if tree > up[-k]:
                    upscore += 1
                else:
                    break

        downscore = 0
        down = views[3]
        if len(down) != 0:
            downscore = 1
            for k in range(0, len(down) - 1):
                if tree > down[k]:
                    downscore += 1
                else:
                    break

        scenictrees[i,j] = leftscore * rightscore * upscore * downscore

print(np.max(scenictrees))


