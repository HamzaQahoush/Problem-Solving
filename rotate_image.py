
def rotate_image(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    # matrix.reverse()
    # print(matrix)
    # for i in range(len(matrix)):
    #     for j in range(i):
    #         print("m[i][j]-->",matrix[i][j] , "m[j][i]-->", matrix[j][i])
    #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    
    
    r=zip(*matrix[::-1])
    for idx, arr in enumerate(r):
        matrix[idx] = list(arr)
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate_image(matrix))