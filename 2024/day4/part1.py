import sys
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
file = file.split("\n")[:-1]
matrix = [[i for i in row] for row in file]
def check(matrix,row_idx,col_idx):
    count = 0
    horizontal = [(0,+1),(0,-1)]
    vertical = [(+1,0),(-1,0)]
    diagonal = [(+1,+1),(-1,-1),(+1,-1),(-1,+1)]
    for dx,dy in horizontal + vertical + diagonal:
        row ,col = row_idx,col_idx
        buffer_list = ["M","A","S"]
        check = True
        while check:
            if 0<= row+dx < len(matrix) and 0 <= col+dy < len(matrix[0]) and len(buffer_list) >0 and matrix[row+dx][col+dy] == buffer_list[0] :
                buffer_list.pop(0)
                row = row+dx
                col = col+dy
            else:
                check = False
                break
        if len(buffer_list) == 0:
            count += 1
    return count
            
            

return_ans = 0
# for row in matrix:
#     print(row)
for row_idx,row in enumerate(matrix):
    for col_idx,ele in enumerate(row):
        if ele == "X":
            return_ans += check(matrix,row_idx,col_idx)
print(return_ans)

    

    
