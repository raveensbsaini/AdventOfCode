import sys
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
file = file.split("\n")
if file[-1] == "":
    file = file[:-1]
matrix =[ [int(i) for i in (list(row))] for row in file]
directions = [(-1,0),(+1,0),(0,+1),(0,-1)]

def check_rating(row,col,matrix,height):
    global rating
    if height == 9:
        rating += 1
        return
    else:
        for dx,dy in directions:
            new_row,new_col = row+dx,col+dy
            if 0<= new_row < len(matrix) and 0<= new_col < len(matrix[0]) and matrix[new_row][new_col] == height + 1:
                check_rating(new_row,new_col,matrix,height+1)
count = 0
for row_idx,row in enumerate(matrix):
    for col_idx,ele in enumerate(row):
        if ele == 0:
            rating = 0
            check_rating(row_idx,col_idx,matrix,0)
            count += rating
print("count",count)

