import sys
import copy
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
file = file.split()
# print(file,len(file))
matrix = [list(row) for row in file]
cur_dir = None
cur_row,cur_col = None,None

# print(matrix# finding initial direction and starting points to start
for row_idx,row in enumerate(matrix):
    for col_idx,ele in enumerate(row):
        if ele == "^":
            cur_dir = "north"
            cur_row,cur_col = row_idx,col_idx
            break
        elif ele == ">":
            cur_dir = "east"
            cur_row,cur_col = row_idx,col_idx
            break

        elif ele == "<":
            cur_dir = "west"
            cur_row,cur_col = row_idx,col_idx
            break
        else:
            if ele != "." and ele != "#":
                cur_dir = "south"
                cur_row,cur_col = row_idx,col_idx
                break
            
            
print(cur_dir,cur_row,cur_col)
direction = {
    "north":(-1,0),
    "south":(+1,0),
    "east":(0,+1),
    "west":(0,-1)
            }            
right_direction = {
    "north":"east",
    "east":"south",
    "south":"west",
    "west":"north"
            }
count = 0

def check(row_idx,col_idx,mat,cur_row,cur_col,cur_dir):
    d = {}
    while 0<= cur_row < len(matrix) and 0<= cur_col < len(matrix[0]):
        if (cur_row,cur_col) not in d:
            d[(cur_row,cur_col)] = [cur_dir]
        else:
            if cur_dir in  d[(cur_row,cur_col)]:
                print("infinate loop found")
                return True
            else:
                d[(cur_row,cur_col)] += [cur_dir]
            
        dx,dy = direction[cur_dir]
        next_row,next_col = cur_row+dx,cur_col+dy 
        try:
            next_ele = matrix[next_row][next_col]
        except:
            print("entering out of the map")
            return False
        if  next_ele != "#":
            cur_row,cur_col = next_row,next_col
        elif next_ele == "#":
            cur_dir = right_direction[cur_dir]
            # print(cur_dir,cur_row,cur_col)
    return False

# print(matrix)
# assert False
for row_idx,row in enumerate(matrix):
    for col_idx,ele in enumerate(row):
        if ele != "#":
            matrix[row_idx][col_idx] = "#"
            print("row",row_idx,"col",col_idx)
            # new_matrix_object = copy.deepcopy(matrix)
            # print(new_matrix_object[0][0] is matrix[0][0])
            # assert matrix != new_matrix_object,"object are same"
            print("cur_row_and_column",cur_row,cur_col)
            result = check(row_idx,col_idx,matrix,cur_row,cur_col,cur_dir)
            matrix[row_idx][col_idx] = "."
            print("row and column",cur_row,cur_col)
            # assert False
            print(result)
            if result:
                count += 1
print("count",count)
