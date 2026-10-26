'''Write a function that takes in a square 2 × 2 matrix A (represented as a
list of lists) and returns a matrix B of the same size where every entry is
one of −2, −1, 1, or 2, such that the sum of the squared entries that
are not on the top-left-to-bottom-right diagonal of the product A · B
is as small as possible'''

#find minimum product
def determine_sum_squared(A, B):
    top_right = A[0][1]* B[0][0] + A[1][1]*B[0][1]
    bottom_left = A[0][0]*B[1][0] + A[1][0] * B[1][1]

    sum_squared = top_right**2 + bottom_left**2
    return sum_squared


#try combinations util it matches minimum

def min_sum_squared(A):
    B = [[1,1],[1,1]]
    min_sum_B = determine_sum_squared(A,B)

    possible_values = [1,-1,2,-2]
    for B_0_0 in possible_values:
        for B_0_1 in possible_values:
            for B_1_0 in possible_values:
                for B_1_1 in possible_values:
                    B_test = [[B_0_0, B_0_1], [B_1_0, B_1_1]]
                    min_sum_B_test = determine_sum_squared(A,B_test)

                    if min_sum_B_test < min_sum_B:
                        B = B_test
    return B


if __name__ == "__main__":
    A = [[-3, 1],[0, 2]]
    B = min_sum_squared(A)
    print(B)