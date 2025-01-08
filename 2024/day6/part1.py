import sys
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
file = file.split()
print(file,len(file))
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
unique = {}
while 0<= cur_row < len(matrix) and 0<= cur_col < len(matrix[0]):
    print(cur_row,cur_col)
    if (cur_row,cur_col) not in unique:
        unique[(cur_row,cur_col)] = True
    dx,dy = direction[cur_dir]
    next_row,next_col = cur_row+dx,cur_col+dy 
    try:
        next_ele = matrix[next_row][next_col]
    except:
        print("entering out of the map")
        break
    if  next_ele != "#":
        cur_row,cur_col = next_row,next_col
    elif next_ele == "#":
        cur_dir = right_direction[cur_dir]
        print(cur_dir,cur_row,cur_col)
print(len(unique))

    

            

            
    

