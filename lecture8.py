
def sum67():
    sum = 0
    ignore = False

    for i in range(len(L)):
        if L[i] == 6:
            ignore = True
        elif L[i] == 7 and ignore:
            ignore = False
        elif not ignore:
            sum += L[i]

    return sum

if __name__=="__main__":
    L = [1,2,3,6,8,9,7,10]
    print(sum67())