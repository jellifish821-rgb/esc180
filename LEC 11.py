## iterating nested loops
numbers = [[1,2,3,], [4,5,6,], [7,8,9]]

for i in range(len(numbers)):
    for j in  range(len(numbers[i])):
        print(numbers[i][j])

for row in numbers:
    for num in row:
        print(num)


##
alphabet = ["a", "b", "c", "d", "e", "f"]
for letter1 in alphabet:
    for letter2 in alphabet:
        print(letter1 + letter2)

## sudoku check
square = [[2,9,4], [1,5,6], [7,8,3]]

print(square)

def convert_square_to_list(square):
    L = []
    for i in range(3):
        for j in range(3):
            L.append(square[i][j])
    return L

L = convert_square_to_list(square)
print(L)

def check_duplicates(L):
    sorted_L = sorted(L)
    for i in range(len(sorted_L)):
        if sorted_L[i] != i+1:
            return True
    return False

## check square
def is_square(L):
    height = len(L)
    for row in L:
        if len(row) != height:
            return False
    return True
