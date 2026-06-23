# 2. Write a Python function that takes a 2D NumPy array and returns:
# ⦁	The sum of each row.
# ⦁	The sum of each column.

import numpy as np

def Sum_rows_cols(arr):
    
    sum_rows = np.sum(arr,axis = 1)
    sum_cols = np.sum(arr,axis = 0)

    return f"Sum of rows: {sum_rows}\nSum of columns: {sum_cols}"




row = int(input("Enter number of rows:"))
col = int(input("Enter number of columns:"))

lst = []
for i in range(row):
    r = list(map(int,input(f"Enter {col} elements for row {i+1} :").split()))
    lst.append(r)

arr_2D = np.array(lst)

# function calling:
out = Sum_rows_cols(arr_2D)
 
print(out)
