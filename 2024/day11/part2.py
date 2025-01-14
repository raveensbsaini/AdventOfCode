import sys
from functools import cache
assert len(sys.argv) > 1,"Enter argument more than 1"
filepath = sys.argv[1]
with open(filepath,"r")  as file:
    file = file.read()
file = file.split("\n")[0]
file = file.split(" ")
if file[-1] == "":
    file = file[:-1]
return_ans = 0
print("file",file)

for i in file:
    print(i)
# assert False
# @cache

d = {}
def func(pebble,blink):
    # print("pebble",pebble,"blink",blink)
    if blink == 75:
        return 1
    else:
        if (pebble,blink) in d:
            return d[(pebble,blink)]
        ans = 0
        if pebble == "0":
            ans += func("1",blink+1)
        elif len(pebble)%2 == 0:
            first_half = pebble[:len(pebble)//2]
            second_half = pebble[len(pebble)//2:]
            ans += func(first_half,blink+1) 
            ans += func(str(int(second_half)),blink+1) 
        else:
            ans += func(str(int(pebble)*2024),blink+1)
    # print("pebble",pebble,"ans",ans)
    d[(pebble,blink)] = ans
        
    return ans


for i in file:
    result = func(i,0)
    print("return",result)
    return_ans += result
print(return_ans)
    
