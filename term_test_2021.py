'''
def f(L):
    L = [1, 2, 3]
    L[0] = 5
    print(L[0])

L1 = [4, 5, 6]
f(L1) #5
print(L[0])


def g(n):
    n = 3
    print(n)
m = 5
m = g(m)
print(m)

def h(L):
    L[1] = [7, 8]
    L[0] = [5, 6]
    L[0][0] = 9
    print(L)
L = [[1, 2], [3, 4]]
h(L)
print(L)
'''

L = [[[1, 2], [3, 4]]]
L1 = L[:]
L1[0][0] = 5
L1[0][1][0] = 6
print(L1)
print(L)