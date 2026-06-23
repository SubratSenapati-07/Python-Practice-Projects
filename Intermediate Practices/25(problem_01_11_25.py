#3. Given two lists of equal length, convert them into NumPy arrays and compute:
# ⦁	Element-wise multiplication
# ⦁	Mean of the resulting array

import numpy as np

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
# user_ip = list(map(int,input("Enter 5 elements of list separated by space:").split()))

l1_arr = np.array(l1)
l2_arr = np.array(l2)

mult = l1_arr * l2_arr
mean = np.mean(mult)

print(f"Element-wise multiplication: {mult}\nMean of the resulting array: {mean}")



#4. Create a NumPy array of shape (5,5) with random numbers, and:
# ⦁	Replace the diagonal elements with their square values.


arr = np.random.randint(1,100,size=(5,5))
i = np.diag_indices(5)
arr[i,i] = arr[i,i]**2

print("Diagonal elements with their square values:\n",arr)