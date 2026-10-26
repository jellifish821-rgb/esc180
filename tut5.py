##1
L = [["CIV", 92],
["180", 98],
["103", 99],
["194", 95]]
for i in L:
    for elem in i:
        if elem == 99:
            print("99")

##2
def get_nums(L):
    L_nums = []
    for i in L:
        L_nums.append(i[1])
    return L_nums

print(get_nums(L))

##3
def lookup(L, num):
    for lis in L:
        if lis[1] == num:
            return lis[0]

print(lookup(L, 99))

##4
recent_stores = ["Store A", "Store B", "Store A", "Store C"]
recent_purchases = [15, 20, 10, 8]

dictionary = {}
for i in range(len(recent_stores)):
    if recent_stores[i] in dictionary:
        dictionary[recent_stores[i]] += recent_purchases[i]
    else:
        dictionary[recent_stores[i]] = recent_purchases[i]

print(dictionary)

##Q5
#see ttt.py