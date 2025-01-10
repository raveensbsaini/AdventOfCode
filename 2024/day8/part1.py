import sys
from collections import defaultdict
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
file = file.split("\n")
if file[-1] == "":
    file = file[:-1]
matrix = [list(row) for row in file]

d = defaultdict(list)
for row_idx,row in enumerate(matrix):
    for col_idx,ele in enumerate(row):
        if ele != ".":
            d[ele].append([row_idx,col_idx])

antinode_loc = {}


def possible(list1):
    return_list = []
    for i,u in enumerate(list1[:-1]):
        for x,y in enumerate(list1[i+1:]):
            return_list.append((u,y))
    return return_list
def mode(a):
    if a >= 0:
        return a
    else:
        return -a
def count_location(pair,antinode_loc,matrix):
    x = pair[0]
    y = pair[1]
    row_diff  = (x[0] -y[0])
    col_diff = (x[1] - y[1])
    location_1 = [y[0] - row_diff,y[1]-col_diff]
    location_2 = [ row_diff+x[0],col_diff+x[1]]
    if 0 <= location_1[0] < len(matrix) and 0 <= location_1[1] <len(matrix[0]) :
        antinode_loc[tuple(location_1)] = True
    if 0 <= location_2[0] < len(matrix) and 0 <= location_2[1] <len(matrix[0]) :
        antinode_loc[tuple(location_2)] = True


for i in d:
    pos_pair = possible(d[i])
    for pair in pos_pair:
        count_location(pair,antinode_loc,matrix)   
print(len(antinode_loc))
