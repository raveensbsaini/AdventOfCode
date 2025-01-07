import sys
assert len(sys.argv) > 1
filepath = sys.argv[1]
with open(filepath,"r") as file:
    file = file.read()
file = file.split("\n\n")
ord  = file[0]
seq = file[1]
ord = ord.split("\n")
seq = seq.split("\n")

def check(seq,ord_dict):
    ans = True
    for i in range(len(seq) -1):
        if ord_dict[seq[i]] == seq[i+1]:
            pass
        else:
            return False
    return True
        
            
def can(seq):
    return True
ord_dict = {}
for i in ord:
    i = i.split("|")
    x = int(i[0])
    y = int(i[1])
    ord_dict[x] = y
print(ord_dict)
    
main_seq = []
correct_seq = []
uncorrect_seq = []
can_seq = []
for line in seq:
    li = line.split(",")[:-1]
    li = [int(i) for i in li]
    main_seq.append(li)
for seq in main_seq:
    if check(seq,ord_dict):
        correct_seq.append(seq)
    else:
        uncorrect_seq.append(seq)
        # if can(seq):
        #     can_seq.append(seq)
print(len(correct_seq))

            
    
