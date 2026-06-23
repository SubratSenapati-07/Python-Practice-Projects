# 💡 Level 2: NumPy Basics 

#1. Create a NumPy array from a Python list [1,2,3,4,5] and print its type and shape.
import numpy as np

arr = np.array([1,2,3,4,5])
print(f"Type :{type(arr)} and shape :{arr.shape}")

#2. Generate a 2D NumPy array of size (3×3) filled with random integers between 10 and 50.
arr = np.random.randint(10,50,size=(3,3))
print("2D Array:",arr)

#3. Create a 1D NumPy array and find its mean, median, and standard deviation.
arr1D = np.arange(1,11)
mean = np.mean(arr1D)
median = np.median(arr1D)
std_dev = np.std(arr1D)
print(f"Mean: {mean}, Median: {median}, Standard Deviation: {round(std_dev,3)}")


#4. Create two arrays a = [1,2,3] and b = [4,5,6] and perform:
# Addition
# Multiplication
# Dot product

a = [1,2,3]
b = [4,5,6]
add = np.add(a,b)
mul = np.multiply(a,b)
dot = np.dot(a,b)
print(f"addition: {add},\nMultiplication: {mul},\ndot :{dot}")


#5. Create a 3×3 identity matrix using NumPy.
arr = np.identity(3)
print("Indentity matrix:",arr)