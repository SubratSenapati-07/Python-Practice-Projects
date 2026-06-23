# 5. Generate 100 random numbers (1–100), find:
# ⦁	Mean, median, standard deviation
# ⦁	How many numbers are above the mean

import numpy as np 

ran_no = np.random.randint(1,100,size=100)
mean = np.mean(ran_no)
median = np.median(ran_no)
std_dev = np.std(ran_no)
print(f"mean:{mean}\nmedian:{median}\nStandard deviation:{round(std_dev,3)}")

ab_mean = np.array([])
for i in ran_no:
    if(i>mean):
        ab_mean = np.append(ab_mean,i)

print("Values that are greater than mean:",ab_mean)
print("Number of values greater than mean:",len(ab_mean))
    
# above_mean = ran_no[ran_no > mean]
# print(f"Count:{len(above_mean)}")