import re
import sys
assert len(sys.argv) > 1
filepath = sys.argv[1]
ans = 0

with open(filepath,"r") as file:
    file = file.read()
main_list = []
pattern = r"mul\(\d+,\d+\)"
for match in re.finditer(pattern,file):
    # print(match)
    # print(match.group())
    # print(match.start())
    # print(match.end())
    main_list.append([match.group(),match.start(),match.end()])

for match in re.finditer(r"do\(\)",file):
        # print(match)
        # print(match.group())
        # print(match.start())
        # print(match.end())
        main_list.append([match.group(),match.start(),match.end()])
for match in re.finditer(r"don't\(\)",file):
        # print(match)
        # print(match.group())
        # print(match.start())
        # print(match.end())
        main_list.append([match.group(),match.start(),match.end()])
# print(row)
main_list.sort(key= lambda x: x[1])
assert main_list.sort(key=lambda x:x[1]) == main_list.sort(key=lambda x: x[2])

for i in main_list:
    print(i)
# assert False
enable = True
disable = False
for i in main_list:
    print(i)
    if i[0] == "do()":
        print("this is do()")
        enable= True
        disable = False
    elif i[0] == "don't()":
        print("this is don't()")
        enable,disable = False,True
    else:
        print("this is mul()")
        if enable == True and disable == False:
            m = re.search(r"(\d+),(\d+)",i[0])
            a = m.group(1)
            b = m.group(2)
            print("a",a)
            print("b",b)
            mul= int(a) * int(b)
            print(mul)
            ans += mul
        else:
            print("ignored")
            pass
    # a = input("Enter anythong to continue")
    print("ans",ans)
print("ans",ans)    


