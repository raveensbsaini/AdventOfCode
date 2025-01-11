import sys
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
file = file.split("\n")
if file[-1] == "":
    file = file[:-1]
file =file[0]
file_number = 0

main_list = []
for i,u in enumerate(file):
    if i % 2 == 0:
        for a in range(int(u)):
            main_list.append(str(file_number))
        file_number += 1
    else:
        for a in range(int(u)):
            main_list.append(".")
        
empty_idx_list = []
for i,u in enumerate(main_list):
    if u == ".":
        try:
            while main_list[-1] == ".":
                main_list.pop()
            main_list[i],main_list[-1] = main_list[-1],main_list[i]
            main_list.pop()
        except:
            break

count = 0
for i,u in enumerate(main_list):
    count += i*int(u)
print("count",count)
