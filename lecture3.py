def main():
    print(a) # error
    print(disc) #error
    print(has_roots(1,2,3))

def has_roots(a,b,c):
    disc = b**2 - 4*a*c
    #disc is a local variable
    if disc == 2:
        return 2
    elif disc == 1:
        return 1
    else:
        return None



