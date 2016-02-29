"""

"""


def matrix_multiply(A, B):
    result = []
    for row in range(3):
        result_row = []
        for col in range(3):
            element = 0
            for i in range(3):
                element += A[row][i] * B[i][col]
            result_row.append(element)
        result.append(result_row)
    return result


if __name__ == "__main__":
    A = [[2, 5, 8],
         [3, 1, 9],
         [-1, -3, 7]]
    B = [[4, 6, 0],
         [-2, -4, -5],
         [-9, -6, -3]]
    print ("The resulting matrix is:")
    res = matrix_multiply(A, B)
    for row in res:
        print (row)

