import sys
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
    
file = file.split("\n")
if file[-1] == "":
    file = file[:-1]


# print(file)
main_list = []
for row in file:
    row = row.split(": ")
    # print(row[0])
    value = int(row[0])
    equ  = row[1].split(" ")
    equ = [int(i) for i in equ]
    # print(equ)
    main_list.append([value,equ])
# print(main_list)

count = 0


def check(value,equ,ans,d):
    # print("value",value,"equ",equ,"ans",ans)
    if len(equ) == 0:
        # print("equ is empty",ans)
        if ans == value:
            d[ans] = True
        return
    else:
        if ans == None:
            a  = equ[0]*equ[1]
            b = equ[0]+equ[1]
            check(value,equ[2:],a,d)
            check(value,equ[2:],b,d)
        else:
            check(value,equ[1:],ans+equ[0],d)
            check(value,equ[1:],ans*equ[0],d)
    
for i in main_list:
    d = {}
    check(i[0],i[1],None,d)
    # print(d)
    if i[0] in d:
        # print("i",i)
        # print("value",i[0])
        count += i[0]
    d = {}
print("count",count)
