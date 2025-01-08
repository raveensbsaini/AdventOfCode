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
# print(ord)
# print(seq)
# assert False

def check(seq,ord_dict):
    # print(seq)
    for i in range(len(seq) -1):
        if f"{seq[i+1]}|{seq[i]}" in ord_dict:
            # print(False)
            return False
    # print(True)
    return True
def swap(list1,idx1,idx2):
    print("swapping")
    a = list1[idx1]
    list1[idx1] = list1[idx2]
    list1[idx2]  = a
    return list1
def can_correct(seq,ord_dict):
    new_seq = seq.copy()
    for i in range(len(seq)):
        last_idx_problem = None
        for t in range(1,len(seq)):
            check_string = f"{new_seq[t]}|{new_seq[i]}"
            if check_string in ord_dict:
                last_idx_problem = t
        if last_idx_problem:
            new_seq_first_idx = new_seq[0]
            new_seq = new_seq[1:]
            new_seq.insert(last_idx_problem,new_seq_first_idx)
            print(new_seq)
    print("new seq",new_seq)
    if check(new_seq,ord_dict):
        return (True,new_seq)
    else:
        return (False,new_seq)
            
# def can(seq):
#     return True
ord_dict = {}
for i in ord:
    i = i.split("|")
    x = int(i[0])
    y = int(i[1])
    ord_dict[f"{x}|{y}"] = True
# print("ord_dict",ord_dict)
# assert False,"ord_dict"
    
main_seq = []
correct_seq = []
uncorrect_seq = []
can_seq = []
# print(seq)
for line in seq[:-1]:
    li = line.split(",")
    li = [int(i) for i in li]
    main_seq.append(li)
# print(main_seq)
for seq in main_seq:
    print("original seq",seq)
    if check(seq,ord_dict):
        print("correct")
        correct_seq.append(seq)
    else:
        print("uncorrect",seq)
        uncorrect_seq.append(seq)
        print("uncorrect_seq",uncorrect_seq)
        result  = can_correct(seq,ord_dict)
        print("uncorrect_seq",uncorrect_seq)
        print(result)
        if result[0]:
            print("can correct")
            can_seq.append(result[1])
print("correct",correct_seq)
print("uncorrect",uncorrect_seq)
print("can_seq",can_seq)

            
    
