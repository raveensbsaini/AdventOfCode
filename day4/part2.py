import sys
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
file = file.split("\n")[:-1]
matrix = [[i for i in row] for row in file]
return_ans = 0

def check(matrix,row_idx,col_idx):
    dx_dy = [(+1,+1),(-1,-1),(+1,-1),(+1,-1)]
    for dx,dy in dx_dy:
        if 0 <= row_idx +dx <len(matrix) and 0<= col_idx+dy < len(matrix[0]):
            pass
        else:
            return False
    if matrix[row_idx + 1][col_idx +1] == "S" and  matrix[row_idx -1][col_idx -1] == "M":
        if matrix[row_idx+1][col_idx -1] == "M" and matrix[row_idx-1][col_idx+1] == "S":
            return True
        elif matrix[row_idx+1][col_idx -1] == "S" and matrix[row_idx-1][col_idx+1] == "M":
                    return True
        else:
            return False
    elif matrix[row_idx + 1][col_idx +1] == "M" and  matrix[row_idx -1][col_idx -1] == "S":
        if matrix[row_idx+1][col_idx -1] == "M" and matrix[row_idx-1][col_idx+1] == "S":
            return True
        elif matrix[row_idx+1][col_idx -1] == "S" and matrix[row_idx-1][col_idx+1] == "M":
            return True
        else:
            return False
    else:
        return False

for row_idx,row in enumerate(matrix):
    for col_idx,ele in enumerate(row):
        if ele == "A":
            if check(matrix,row_idx,col_idx):
                return_ans += 1
print(return_ans)

    
