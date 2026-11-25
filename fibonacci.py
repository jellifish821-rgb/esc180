#fibonacci
def fib(n):
    #base case
    if n<=2:
        return 1
    #rec
    return fib(n-1)+fib(n-2)

print(fib(3))

# is even
def is_even(n):
    if n == 0:
        return True
    if n == -1:
        return False

    return is_even(n-2)


def is_even(n):
    if n == 0:
        return True
        #either evalue true here if even
    return not is_even(n-1) #or since the even number before it returns true, it will return false for n is odd


# runtime complexity for fibonacci
# bound lowest and highest number of calls
# logest branch is n-1 branch as it decreases by 1 reach call
#results in sum of 2^i; using formula and taking strongest term --> O(2^n)
#shortest branch -- > subtract by 2 each time so sum of 2^i/2 calls --> )(root(2^n))
