def rotateMat(mat):
    n = len(mat)
    for i in range(n*n//2):
        mat[i//n][i%n], mat[n-i//n-1][n - i%n - 1] = mat[n-i//n-1][n - i%n - 1] , mat[i//n][i%n]

    return mat