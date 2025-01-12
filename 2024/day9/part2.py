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
main_dict = {}
idx_dict = {}
main_list = []
for i,u in enumerate(file):
    if int(u) == 0:
        continue
        assert False

    if i % 2 == 0:
        main_list.append( [file_number]*int(u))
        file_number += 1
    else:
        if u == 0:
            continue
        main_list.append(["."]*int(u))
                     
# print(main_list)
file_num  = 0
for i,u in enumerate(main_list):
    if u[0] == ".":
        main_dict[i] = [len(u),0]
    else:
        idx_dict[file_num] = i
        file_num += 1

    
# assert False
# print(main_dict)
print(file_number)
# print(idx_dict)
# assert False

def printx(*args,**kwargs):
    return
def update_list(main_list,main_dict,idx_dict,file_number):
    for i in range(file_number-1,-1,-1):
        print(i)
        idx_number_of_file = idx_dict[i]
        file = main_list[idx_number_of_file]
        # print("idx_number_of_file",idx_number_of_file)
        # print(file)
        for idx in main_dict:
            # print("idx",idx,"space required",len(file),"space have",main_dict[idx][0])
            if idx < idx_number_of_file:
                if main_dict[idx][0] >= len(file):
                    main_dict[idx][0] -= len(file)
                    # print("list",main_list[idx])
                    main_list[idx_number_of_file] = ["."]*len(file)
                    start_idx = main_dict[idx][1]
                    # print(start_idx,"start_idx")
                    start =main_list[idx][:start_idx]
                    # print("start",start) 
                    main_dict[idx][1] = start_idx+len(file)
                    middle = [i]*len(file)
                    # print("middle",middle)
                    end = main_list[idx][start_idx+len(file):]
                    main_list[idx] = start+middle+end
                    # print("end",end)
                    # print("main_list",main_list)
                    # assert False

                    # print("new_main_list",main_list)
                    # assert False,"found here"
                    break
    return_list = []
    for buffer in main_list:
        return_list += buffer
    # print(return_list)
    return return_list
        

main_list = update_list(main_list,main_dict,idx_dict,file_number)
count = 0
for i,u in enumerate(main_list):
    try:
        count += i*int(u)
    except:
        pass
print("count",count)
