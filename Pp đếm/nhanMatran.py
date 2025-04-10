def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return("Number of columns in matrix A must equal number of rows in matrix B.")
    
    # tao matran luu ket qua
    result =[[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]


    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            result[i][j] = 0
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

res = multiply_matrices([[1,2,3], [4,5,6]], [[7,8,9], [10,11,12], [3,2,1]])
print(res)