## Using range()
# range() can be used to create lists using the same rules that we know
# range() with 1 argument:
L1 = list(range(10))
print(L1)

# range() with 2 arguments:
L2 = list(range(5, 15))
print(L2)

# range() with 3 arguments:
L3 = (list(range(10, 100, 10)))
print(L3)


# Note that we can use range() with a negative step size
L4 = list(range(100, 90, -1)) # goes to 91

# But be aware of setting valid start/end points
# non valid - returns empty list

## List slicing
# Let's say we have a list L, and we want to take a subset of this list
L = [0,1,2,3,4,5,6,7,8,9]

# Basic slicing syntax: L[m:n:k]
# Similar to arguments in range()
L_slice = L[2:5:2]
print(L_slice)


# Can also have a negative step size


# LIST SLICING VARIANTS
# Omitting the step size is valid, since it's set to 1 by default


# We can omit the start/end points


# If step size is specified and start/end points are not, they will be inferred
# based on the sign of the step size
# Positive step size -> traverse fowards


# Negative step size -> traverse backwards


# We can even omit both start AND end points, specifying only the step size


# NOTE: L[::-1] is commonly used to reverse a list

# What if we omit all 3 arguments?


## Manual list slicing with loops
# What if we don't have access to the built-in Python slicing function?
# Let's write functions to do so using loops

def manual_slice(L, start, end, step):
    '''Return L[start:end:step]. Assume start,end are ints >= 0 and < len(L).'''
    res = []
    for ind in range(start, end, step):
        res = res.append(L[ind])
    return res

# Try with while loop instead
def manual_slice_while(L, start, end, step):
    '''Return L[start:end:step]. Assume start,end are ints >= 0 and < len(L).'''
    res = []
    ind = start
    if step > 0:
        while ind < end:
            res.append(L[ind])
            ind += step #prevent infinite loop
    elif step < 0:
        while ind > end: # swap this to > to reverse traversal
            res.append(L[ind])
            ind += step
    else:
        print("Invalid step size")
        return None
    return res

if __name__ == '__main__':
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test positive step
    start = 0
    end = 5
    step = 1
    print(manual_slice(L, start, end, step))

    if (L[start:end:step]) == manual_slice(L, start, end, step):
        print("test case passed")


    # Test negative step
    start = 8
    end = 1
    step = -1



## list.extend()
# Let's say we want to append multiple elements to a list
# Can do this using list.extend()


# Equivalent to repeatedly append individual elements using a loop



# What happens if we try to append with a list rather than extend with it?



# As it turns out, using += with lists does the same thing as list.extend()


## Sorting lists using list.sort()
# list.sort() will modify the order of elements in the list
# For lists containing numeric types, they will be sorted in ascending order
L = [3,1,100,-5,29,50,0.1,-10]


# The job of list.sort() is to modify a list, and it does not have a return value



# For lists containing strings, they will be sorted in lexicographical order
#     (similar to alphabetical order)
courses = ["Praxis", "CIV", "Physics", "180", "103", "Calc"]



# What happens with lists of mixed types?
courses_mixed = ["Praxis", "CIV", "Physics", 180, 103, "Calc"]


# What if we want to sort a list in descending order instead?



## Sorting lists using sorted()
# We can also use sorted() to sort a list without modifying the original list
L = [3,1,100,-5,29,50,0,-10]


## Missing k example
# Suppose we have an unsorted list containing all the ints between 1 and n,
# but one of them is missing. (The list is of length n-1).
# What is the missing integer?

def missing_k(L):
    N = len(n) + 1
    for k in range(1, N):
        if k not in L:
            #this is the missing int
            return k
    return None

if __name__ == '__main__':
    L = [10,3,5,6,7,1,2,4,8] # 9 is missing
    print(missing_k(L))

## Missing k example without using not in
# Imagine we don't have access to the not in operator. Let's write a helper
# function that accomplishes the same thing

def elem_in_list(elem, L):
    '''Return True iff elem is in L'''
    pass

def missing_k(L):
    pass

if __name__ == '__main__':
    L = [10,3,5,6,7,1,2,4,8] # 9 is missing
    print(missing_k(L))

# Bonus question: can you think of a more efficient way of doing this?