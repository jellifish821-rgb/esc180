def merge(L1, L2):
    i, j = 0, 0
    merged = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[i]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1

    merged.extend(L1[i:])
    merged.extend(L1[j:])

    return merged

L1 = [1, 5, 355]
L2 = [3, 7, 8]
print(merge(L1, L2))

# base case is when list only has one element
#then merge adjacent (in order)

def merge_sort(L):
    #base
    if len(L) <= 1:
        return L[:]

    #recursive
    mid = len(L) // 2
    return merge(merge_sort(L[:mid])), merge_sort(L[mid:])


