# matrix index
def matrix_index(val):
    # i = row index, j = column index
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == val:
                return (i,j)



# matrix addition
def matrix_add(M1, M2):
    res = []
    for i in range(len(M1)):
        new_row = []
        for j in range(len(M1[0])):
            new_row.append(M1[i][j] + M2[i][j])
        res.append(new_row)
    return res

def matrix_add2(M1, M2):
    res = []
    for i in range(len(M1)):
        res.append([0]*len(M1[0]))
        # do not do res = [0]*len(M1[0])*len(M1); each list is an alias of the first one - when modifying later in alters all the rows
    for i in range(len(M1)):
        for j in range(len(M1[0])):
            res[i][j] = M1[i][j] + M2[i][j]
    return res

#multiplication
def matrix_mult(M1, M2):
    # check validity
    if len(M1[0]) != len(M2):
        return

    res  = []
    for i in range(len(M1)):
        res.append([0]*len(M2[0]))

    for i in range(len(res)):
        for j in range(len(res[0])):
            for k in range(len(M1[0])): # k is dot prod index
                res[i][j] += M1[i][k]*M2[k][j]


    return res


# converting sparse matrix
def convert(M_sparse, dim):
    res = []
    for i in range(dim[0]):
            res.append([0]*dim[1])

    for coord, value in M_sparse.items():
        for i in range(len(res)):
            for j in range(len(res[0])):
                if i == coord[0] and j == coord[1]:
                    res[i][j] = value


