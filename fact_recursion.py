#factorial-recursion
# what is the smalllest version of this problem to solve? - when n = 0
#how to get closer to the smallest version of this problme? fact(n) = n*fact(n-1)

def fact(n):
    #base
    if n== 0:
        return 1

    #recursive
    return n*fact(n-1) # needs fact(n-1) --> calls funtion for (n-1) continuously until reaches base case

print(fact(4))