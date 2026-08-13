## Secret Santa App v2 -- Graph Theory Boogaloo!

from math import *

## NOTE: This app will be CASE and SPELLING sensitive! --  Sara, sara, and Sarah  are 3 different people!

## A Hamiltonian Cycle or Circuit in a graph G is a cycle that 
## visits each vertex of G exactly once and returns to the starting vertex.
## Hopefully, we haven't added so many exclusions to our graph that it is non-Hamiltonian. 
## If the graph is Hamiltonian, we have found a solution. Otherwise, we will need to split the graph
## into multiple cycles (each of which is Hamiltonian.)

## 0) Import graph from CSV file
from secret_santa import * ## get the exclusion list from the user provided CSV file.
from secret_santa import exclusions ## graph

## 0.1) Create index:name dictionary to make it easier to map graph and vis versa
name_index = {}
index_name = {}
#Initialize adjacent edges matrix at the same time 
adj_edges = [[1 for _ in range(len(exclusions.items()))] for _ in range(len(exclusions.items()))]

c = 0
for key, _ in exclusions.items():
    name_index.update({c:key})
    index_name.update({key:c})
    adj_edges[c][c] = 0 
    c+=1

## 0.2) Update adjacent matrix to describe the edges of the graph (i.e., add 0 for all excluded edges)
## This graph is directional, so [x,y] = 0, does not imply [y,x] = 0.
for key, values in exclusions.items():
    giver = index_name[key]
    for val in values:
        excluded = index_name[val]
        adj_edges[giver][excluded] = 0

print(name_index)

## 1) Check if graph is Hamiltonian using Depth First Search (Backtracking Method)
## NOTE: If we know the graph is Hamiltonian (i.e., no exclusions at all), we have the Traveling
## Salesman Problem (TSP). If this is the case, DFS isn't necessary (as it is O(n!) and very slow) and
## a faster algorithm like Dijkstra's or A* can be used, but let's assume that's not agiven.
def isSafe(vertex, adjMat, path, pos):

    # The vertex must be adjacent to the previous vertex
    if adjMat[path[pos - 1]][vertex] == 0:
        return False

    # The vertex must not already be in the path
    for i in range(pos):
        if path[i] == vertex:
            return False

    return True

def depth_first_search(adjMat, path, pos, n):
    # Case 1: All vertices on Hamiltonian cycle
    if pos == n:
        # Check if there's an edge from last to first vertex
        return adjMat[path[pos-1]][path[0]] == 1
    
    # Else: Try all possible vertices as next candidate
    for v in range(1, n):
        if isSafe(v, adjMat, path, pos):

            path[pos] = v

            if depth_first_search(adjMat, path, pos + 1, n):
                return True

            # Backtrack if v doesn't lead to a solution
            path[pos] = -1

    return False


def hamiltonian_cycle_check(adj_matrix):
    n = len(adj_matrix)
    path = [-1]*n

    # Start at 0
    path[0] = 0

    if not depth_first_search(adj_matrix, path, 1, n):
        return [-1]
    return path

### This actually runs the DSF on our graph

path = hamiltonian_cycle_check(adj_edges)

if path[0] == -1:
    print("Hamiltonian Cycle of Size N DNE. Need to find disjoint Cycles instead...")
else:
    print(path)

    for i in range(len(path)):
        giver
        try:
            print(name_index[path[i]]+" DREW "+ name_index[path[i+1]])
        except:
            print(name_index[path[i]]+" DREW "+ name_index[path[0]])

## 4) If DFS proves our graph is non-Hamiltonian, we will remove the sub-n length Hamiltonian Cycle 
## we just found from consideration, and attempt to make a another Hamiltonian Cycle from the remaining nodes. 
if path[0] == -1:
    pass ## TODO