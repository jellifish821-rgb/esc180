def sum_nums(L):
    s = 0
    for num in L:
        s += num
    return s

L = [1,2,3,4,5,6,7,8]
def count_evens(L):
    even_num = 0
    for i in range(len(L)):
        if L[i] % 2 == 0:
            even_num += 1
        i += 1
    return even_num

print(count_evens(L))

## 2
lis = [1,2,3]
def list_to_str(lis):
    str_lis = "["
    for i in lis:
        i = str(i)
        str_lis += i
        if i != str(lis[-1]):
            str_lis += ", "
        else:
            str_lis += "]"

    return str_lis

print(list_to_str(lis))

##3
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [1,2,3]
def lists_are_the_same(list1, list2):
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False

        return True
    else:
        return False

print(lists_are_the_same(list1, list3))



##4
# lis_name = []
# while True:
#     name = input("Enter a name: ")
#     if name == "END":
#         break
#     else:
#         lis_name.append(name)
# lis_name = str(lis_name).replace("[", "").replace("]", ""). replace("'","")
#
# print("The names are:", lis_name)

##5
num_terms = 0
n_sigfigs = 1
import math

def calc_pi():
    res = 0
    global num_terms
    for i in range(num_terms+1):
        leb = ((-1)**i)/(2*i + 1)
        res = res + leb
    return 4*res

print

while True:
    calc_pi()
    print(calc_pi()*(10**n_sigfigs))
    print(int(math.pi*(10**n_sigfigs)))
    if int(calc_pi()*(10**(n_sigfigs-1))) == int(math.pi*(10**(n_sigfigs-1))):
        break
    num_terms += 1

print(num_terms)


##6
#a)
def gcd(n, m):
    d = 1
    for i in range(n):
        if n%(i+1) == 0 and m%(i+1) == 0:
            d = i + 1
    return d

print(gcd(15, 25))

#b)
def gcd_efficent(n, m):
    d = 1
    for i in range(n, 0, -1):
        if n%(i+1) == 0 and m%(i+1) == 0:
            d = i + 1
    return d

print(gcd_efficent(15, 25))





















