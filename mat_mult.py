
import numpy as np 

def mat_mult(mat1,mat2):
    return np.array(mat1)*np.array(mat2)

mat_first=[[1,2,3],[4,5,6]]
mat_sec=[[7,8,9],[11,12,13]]

print(mat_mult(mat_first,mat_sec))