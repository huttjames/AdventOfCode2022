import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#Read in input as a 2D array
with open('input.txt') as f:
    heights = f.readlines()

heights = [height.rstrip() for height in heights]
heights = [[*height] for height in heights]
heights = np.array(heights)

#Record start and end location 
startindex = (np.where(heights == "S")[0][0],np.where(heights == "S")[1][0])
endindex = (np.where(heights == "E")[0][0],np.where(heights == "E")[1][0])

#Calc size of grid 
(rows, cols) = heights.shape

#Convert to array of numerical heights - note end height is defined as 26
heightval = lambda x: max(ord(x) - 97, 0)
vfunc = np.vectorize(heightval)
numheights = vfunc(heights)
numheights[endindex[0],endindex[1]] = 26

#create list of desired edges
edges = []

for j in range(cols):
    for i in range(rows):
        nodeID = j * rows + i
        
        #check if can move right 
        if j < cols - 1:
            if numheights[i][j] + 1 >= numheights[i][j+1]:
                newEdge = (nodeID, nodeID + rows)
                edges.append(newEdge)
        # check if we can move left:
        if j > 0:
           if numheights[i][j] + 1 >= numheights[i][j-1]: 
               newEdge = (nodeID, nodeID - rows)
               edges.append(newEdge)
        # check if we can move down: 
        if i < rows - 1:
            if numheights[i][j] + 1 >= numheights[i+1][j]:
                newEdge = (nodeID, nodeID + 1)
                edges.append(newEdge)
        # check if we can move up:
        if i > 0:
            if numheights[i][j] + 1 >= numheights[i-1][j]:
                newEdge = (nodeID, nodeID - 1)
                edges.append(newEdge)


#Create a graph of a 2d lattice with the same shape. The size of each node when printed is the height value. The labels follow in sequence.
G = nx.grid_2d_graph(rows, cols)
labels=dict(((i,j),i + (cols-1-j)*rows) for i, j in G.nodes())
nx.relabel_nodes(G,labels,False) #False=relabel the nodes in place
inds=labels.keys()
vals=labels.values()
inds=[(cols-j-1,rows-i-1) for i,j in inds]

#Create the dictionary of positions for the grid
grid_pos=dict(zip(vals,inds)) #Format: {node ID:(i,j)}

#Copy this graph but remove all the edges and make it directed
emptyG = nx.create_empty_copy(G)
emptyG = emptyG.to_directed()

#The above steps contain some redundancy because it makes the graph plottable on a 2D grid so that we can visualise the paths which
#exist as we are adding them. A graph needn't actually have spatial position, but doing it likes this makes checking for errors easier.

#Add to desired edges to the graph 
emptyG.add_edges_from(edges)

'''
#Show the graph 
plt.figure()
nx.draw(emptyG,pos=grid_pos,with_labels=True,node_size=numheights.T.flatten())
plt.show()
'''

#Part1
startNodeID = startindex[0] + rows * startindex[1]
endNodeID = endindex[0] + rows * endindex[1]

pathlen = nx.shortest_path_length(emptyG, source = startNodeID, target = endNodeID)
print(pathlen)

#Part2
#Find the node indices of all points with height a/0
lowpoints=[]
for j in range(cols):
    for i in range(rows):
        if numheights[i][j] == 0:
            nodeID = j * rows + i
            lowpoints.append(nodeID)

#Find shortest path where all lowpoints are given as starting point
#Some points a are not connected to the end point. In this case the expection is raised, hence the error handling

pathlens = []
for start in lowpoints:
    try: 
        pathlen = nx.shortest_path_length(emptyG, source = start, target = endNodeID)
        pathlens.append(pathlen)
    except nx.NetworkXNoPath:
        pass

print(min(pathlens))