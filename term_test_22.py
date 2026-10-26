##Q7
'''
L = [1, [2, 3], 4 ]
L1 = L[:]
L[0] = 7
L[1][0] = 8
L1[1][1] = 9
print(L)
print(L1)
'''

#e
'''
def greeting(s):
    global s
    s = "Happy " + s
    print(s)

res = greeting(s)
print(res)
'''

##Q6
#Write a function that, when called, returns the next digit of π (approx 3.14159...). You may assume that the function will not be called more than 10 times
import math


global digit
digit = -1

def next_digit_pi():
    global digit
    digit += 1
    pi = str(math.pi).replace(".", "")
    for i in range(len(pi)):
        if i == digit:
            print(pi[i])

next_digit_pi()
next_digit_pi()
next_digit_pi()
next_digit_pi()

## Q5
def luckiest_kid(haul_dataset):
    num_dataset = {}
    for house in haul_dataset.values():
        for name, candies in house.items():
            candy_count = len(candies)
            if name not in num_dataset.keys():
                num_dataset[name] = 0
            num_dataset[name] += candy_count

    max_count = 0
    luckiest_kid = ""
    for name, count in num_dataset.items():
        if count > max_count:
            max_count = count
            luckiest_kid = name

    return luckiest_kid


halloween_haul = {"house1": {"Annie": ["snickers", "mars"],
"Johnny": ["snickers"] },
"house2": {"Annie": ["coffee break", "mars"],
"Jackie":["coffee break"]}
}

print(luckiest_kid(halloween_haul))

##Q4
#Write a function that takes in two matrices stored as lists of lists of numbers,and returns the sum of the two matrices, stored as a list of lists. If the two matrices cannot be added because of a dimension mismatch,return the string"ERROR"

def matrix_sum(A,B):
    columns_A = len(A)
    rows_A = len(A[0])
    columns_B = len(B)
    rows_B = len(B[0])

    if columns_A == columns_B and rows_A == rows_B:
        sum = []
        for row in range(rows_A):
            sum_row = []
            for elem in range(columns_A):
                sum_elem = A[row][elem] + B[row][elem]
                sum_row.append(sum_elem)
            sum.append(sum_row)
        return sum

    else:
        return "Error"

A = [[1,1], [1,1]]
B = [[2,2], [2,2]]
print(matrix_sum(A,B))

##Q3
'''
count = 0
while True:
    order = input("What is your order? ").lower()
    if order == "pumpkin spice latte":
        print(count)
        break
    else:
        count += 1
'''

##Q2
#a
def prod(L):
    prod = 1
    for i in L:
        prod = prod*i
    return prod

print(prod([2,3,4]))
#b
def duplicates(list0):
    value = list0[1:]
    for elem in list0:
        prev_value = value
        value = elem
        if prev_value == value:
            return True
        else:
            pass

print(duplicates(["a","d","s","s"]))

##Q1
def get_perfect_squares(n):
    perfect_sqr=[]
    for i in range(n):
        if i**2 <= n:
            perfect_sqr.append(i**2)
    return perfect_sqr

print(get_perfect_squares(36))







