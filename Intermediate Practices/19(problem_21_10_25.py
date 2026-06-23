#1. Write a Python program to check palindrome (like "madam" → True).
n = str(input("Enter to check palindrome or not:")).lower()
rev = n[::-1]
if(n==rev):
    print(f"{n} is palindrome")

else:
    print(f"{n} is not palindrome")


#2. Create a Python program that prints the Fibonacci series up to 100.
# 0, 1, 1, 2, 3, 5, 8, 13,..........
a = 0
b = 1
print("Fibonacci series up to 100:")
while(a<=100):
    print(a,end=',')
    next = a+b
    a = b
    b = next


