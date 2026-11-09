##Q1
import numpy as np
M1 = [[1,2,3],[4,5,6],[7,8,9]]
def print_matrix(M_1o1):
    M = np.array(M_1o1)
    print(M)

print_matrix(M1)


##Q2
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i

    return len(row)

print(get_lead_ind([0,0,0,0]))

##Q3
def get_row_to_swap(M, start_i):
    most_left_lead_i = get_lead_ind(M[start_i])
    row_index = start_i

    for i in range(start_i, len(M)):
        if get_lead_ind(M[i]) < most_left_lead_i:
            row_index = i

    return row_index

M2 = [[5, 6, 7, 8],
[0, 0, 1, 1],
[0, 0, 5, 2],
[0, 1, 0, 0]]
print(get_row_to_swap(M2, 2))

##Q4
def add_rows_coefs(r1, c1, r2, c2):
    new_r1 = [0]*len(r1)
    new_r2 = [0]*len(r2)
    new_row = [0]*len(r1)
    # multiply r1
    for i in range(len(r1)):
         new_r1[i] = r1[i]*c1
    # multiply r2
    for i in range(len(r2)):
        new_r2[i] = r2[i]*c2
    # add
    for i in range(len(r1)):
        new_row[i] = new_r1[i] + new_r2[i]

    return new_row

print(add_rows_coefs([5,6,7], 1, [1,2,3], 2))

##Q5
def eliminate(M, row_to_sub, best_lead_ind):
    coeff = M[row_to_sub][best_lead_ind]
    for i in range(row_to_sub + 1, len(M)):
        factor = - (M[i][best_lead_ind] / coeff)
        new_row = add_rows_coefs(M[i], 1, M[row_to_sub], factor)
        M[i] = new_row
    return M

M3 = [[5, 6, 7, 8],
[0, 0, 1, 1],
[0, 0, 5, 2],
[0, 0, 7, 0]]
print(eliminate(M3, 1, 2))


##6
def forward_step(M):
    for i in range(len(M)):
        i_swap = get_row_to_swap(M, i)
        M[i], M[i_swap] = M[i_swap], M[i]
        print_matrix(M)
        print(f"swap row{i} with row{i_swap}")

        eliminate(M, i, get_lead_ind(M[i]))
        print_matrix(M)
        print(f"eliminate rows below row {i} by subtracting a multiple of row{i} from rows below it")
    return M

M4 = [[5, 6, 7, 8],
[0, 0, 1, 1],
[0, 0, 5, 2],
[0, 9, 7, 9]]
print(forward_step(M4))


##7
def backward_step(M):
    for i in range(len(M)-1, -1, -1):
        eliminate(M, i, get_lead_ind(M[i]))

        for j in range(len(M[i])):
            coeff = M[i][get_lead_ind(M[i])]
            M[i][j] = M[i][j]/coeff


    return M

M5 = [[5, 6, 7, 8],
[0, 0, 1, 1],
[0, 0, 5, 2],
[0, 9, 7, 9]]
backward_step(M5)



##8
def solve(M,b):
    x = []
    for i in range(len(M)):
        M[i].append(b[i])

    M = forward_step(M)
    M = backward_step(M)

    for i in range(len(M)):
        x.append(M[i][i])

    return x






















