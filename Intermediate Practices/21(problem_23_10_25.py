#1. Create a 4×4 array of random numbers and extract the 2×2 middle sub-matrix.
import numpy as np
ran_arr = np.random.randint(1,51,size=(4,4))
print(ran_arr[1:3,1:3]) 

#arr[row_start:row_end, col_start:col_end]


#2. Create a 5×5 identity matrix and replace the diagonal elements with the values [10,20,30,40,50].
identity_matrix = np.identity(5)
np.fill_diagonal(identity_matrix, [10,20,30,40,50])
print(identity_matrix)

#3. Create an array of 10 elements and replace all even numbers with -1.
arr = np.arange(1,11)
arr[arr % 2 == 0] = -1
print(arr)