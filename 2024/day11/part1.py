import sys
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
file = file.split("\n")
file = file[0].split(" ")
file = [int(i) for i in file]
print(file)
def gen(a):
    for i in a:
        yield i
def modify_file(file):
    return_file = []
    for i in gen(file):
        if i == 0:
            return_file.append(1)
        elif len(str(i))%2 == 0:
            string = str(i)
            first_half = string[:len(string)//2]
            second_half = string[len(string)//2:]
            first_half,second_half = int(first_half),int(second_half)
            # print(first_half,second_half)
            return_file.append(first_half)
            return_file.append(second_half)
        else:
            return_file.append(i*2024)
    return gen(return_file)
stones = 0
for i in gen(file):
    # print(file)
    print("i",i)
    a = [i]
    # print("a",a)
    for blink in range(75):
        print("blink",blink)
        a = modify_file(a)
        # assert False
        # print(a)
    stones += len(a)
    print(len(a))
    # assert False
print(stones)

