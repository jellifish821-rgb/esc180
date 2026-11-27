##1
#A: base=a; recursive is a+a+a... b times so recursive call b-1

def times(a,b):
    if b == 1:
        return a

    return times(a, b-1) + a

print(times(2,3))
# D: O(n)

##2
def digit_sum(n):
    if len(str(n)) == 1:
        return n

    return digit_sum(n//10) + n%10

print(digit_sum(123))

##3
def remainder(a,b):
    if a < b:
        return a

    return remainder(a-b,b)

print(remainder(10,3))

##4
def linear_search(L, e):
    if L[0] == e:
        return 0

    return linear_search(L[1:], e) + 1

L = [1,2,3,4,5]

print(linear_search(L, 5))

##5
def interleave(L1, L2):
    if len(L1) == 1:
        return [L1[0], L2[0]]

    new_ls = interleave(L1[:-1], L2[:-1])
    new_ls.append(L1[-1])
    new_ls.append(L2[-1])
    return new_ls
L1 = [1,2,3]
L2 = ["a", "b", "c"]
print(interleave(L1, L2))


##6
def reverse_rec(L):
    L = helper(L, 0, len(L)-1)
    print(L)


def helper(L, left, right):
    if left >= right:
        return L
    L[left], L[right] = L[right], L[left]
    return helper(L, left + 1, right - 1)

L = [1,2,3]

print(reverse_rec(L))
##7
def zigzag1(L):
    if len(L) == 0:
        print()
    elif len(L)%2 != 0:
        print(L[len(L)//2], end=" ")
        zigzag1(L[:(len(L)//2)] + L[len(L)//2 + 1:])
    else:
        print(L[len(L)//2 - 1], L[len(L)//2], end=" ")
        zigzag1(L[:(len(L)//2 - 1)] + L[len(L)//2 + 1:])



L = [0,1,2,3,4,5,6]
zigzag1(L)

##8


##9
def split_list(L, seps):
    for i in range(len(L)):
        if L[i] in seps:
            L[i] = seps[0]
    new_ls = split_list1(L, seps[0])
    return new_ls

def split_list1(L, sep):
    new_ls = []
    end = 0
    for i in range(len(L)):
        if L[i] == sep:
            new_ls.append(L[end:i])
            end = i + 1
    new_ls.append(L[end:])
    return new_ls
L=[1, 2, 6, 4, 5, 3, 7]
print(split_list(L, [3,6]))






















