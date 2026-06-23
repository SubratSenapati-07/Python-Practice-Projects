#1. Write a program to count vowels in a string.

word = input("Enter a String: ")
vowels = "aeiouAEIOU"
c = 0
for i in word:
    if i in vowels:
        c = c+1

print(f"Vowel chracter :{c}") 



#2. Given a list [2,5,7,3,8,1], write code to create a new list of squares using list comprehension.

list = [2,5,7,3,8,1]
new_list = [ i**2 for i in list ]
print(f"Square list:{new_list}")


#3. Write a Python program to find the largest element in a list without using max().

list = [10,13,12,52,52,34]
largest = list[0]
for i in list:
    if (largest < i):
        largest = i
print(f"Largest item in list:{largest}")
# print(max(list))


#4. Create a dictionary of 5 students with marks. Print the student with the highest marks.

friends = {"Subrat": 75 , "Subh": 80, "Sagar": 76, "Sonali": 98, "Sristi": 95}

topper = ""
highest_mark = 0

for name, mark in friends.items():
    if mark > highest_mark:
        highest_mark = mark
        topper = name

print(f"{topper} has the highest mark i.e. {highest_mark}")

