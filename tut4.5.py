##Q6
def check_repeat(str):
    instances = {}
    for elem in str:
        if elem in instances.keys():
            instances[elem] += 1
        else:
            instances[elem] = 1
    for char, count in instances.items():
        if count > 2:
            return True
    return False

possible_values = ("a", "b", "c", "d")
for one in possible_values:
    for two in possible_values:
        for three in possible_values:
            for four in possible_values:
                string = one + two + three + four
                if check_repeat(string) == False:
                    print(string)


##Q4
def is_symmetric(L):
    half = 0
    if len(L)%2 == 0:
        half = len(L)/2
    else:
        half = (len(L) - 1)/2

    for i in range(int(half)):
        if L[i] == L[-i]:
            continue
        else:
            return False
    return True

print(is_symmetric([1,0,1,1]))

##Q3
matrix = [
[12, 5, 18, 3],
[7, 29, 11, 4],
[15, 2, 9, 21],
[8, 17, 6, 13]
]

maximums = {} #row:max value
for row in range(len(matrix)):
    row_max = matrix[row][0]
    for i in range(len(matrix[row])):
        if matrix[row][i] > row_max:
            row_max = matrix[row][i]
    maximums[row] = row_max

largest_max = maximums[0]
for row, max in maximums.items():
    if max > largest_max:
        largest_max = max
        position = row

for i in range(len(matrix[position])):
    if matrix[position][i] > largest_max:
        largest_index = i

for i in range(len(matrix)):
    print(f"Row: {i} Maximum: {maximums[i]}")
print(f"Largest_value: {largest_max}")
print(f"Row index: {largest_index}")

