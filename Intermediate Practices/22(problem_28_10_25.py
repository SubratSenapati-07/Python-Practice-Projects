#1. Create a 2D array and find the maximum value of each row and column.

import numpy as np
arr_2D = np.array([[2,4,6],
                   [1,3,5],
                   [6,2,3]])
print("Maximum value of Row: ",np.max(arr_2D,axis=1))
print("Maximum value of Column: ",np.max(arr_2D,axis=0))



#2. Reshape a 1D array of 12 elements into shape (3×4).

arr_1d = np.arange(1,13)
arr_2d = arr_1d.reshape(3,4)
print("Reshaped Array: ",arr_2d)



#3. Write a NumPy program to sort an array in both ascending and descending order.

arr1 = np.array([[13,21,81],
                 [74,85,95],
                 [21,9,35]])
ascending = np.sort(arr1, axis=None)
descending = np.sort(arr1, axis=None)[::-1]

print("Ascending Order:",ascending)
print("Descending Order:",descending)