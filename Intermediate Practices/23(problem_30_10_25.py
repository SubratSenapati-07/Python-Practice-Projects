#1. 1.	Create a NumPy array of 20 random integers between 1 and 100, then:
# ⦁	Find the average of only even numbers.
# ⦁	Replace all values greater than the average with 0.

import numpy as np
ran_20 = np.random.randint(1,101,size=20) #20 Random int..
print("Random 20 integer between 1 to 100:",ran_20)

even_no = np.array([item for item in ran_20 if item%2 == 0]) # even of ran_20 
# even_no = ran_20[ran_20 % 2 == 0]  
avg_even_no = np.mean(even_no) # avg of even number 
print("Average of Even numbers:",round(avg_even_no,3))


ran_20[ran_20>avg_even_no] = 0
print("Replace by 0,values that greater than average:",ran_20)