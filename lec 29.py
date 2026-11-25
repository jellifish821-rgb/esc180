#lec 29
#deepcopy
def deep_copy(L):
    #base
    if type(obj) != list:
        return obj

    copy = []
    for elem in obj:
        copy.append(deep_copy(elem))
    return copy

# could break down when not a list - i.e other mutable datatypes like dictionaries, or if circular say original = [1,2,3] original.append(original), or extensively nested, that memeory cannot hold all the recursive calls required

