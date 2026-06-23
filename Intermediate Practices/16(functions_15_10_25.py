#1>>> Enamerate function:
nummbers = ["apple","banana","orange","guava"]
i=1
for i,item in enumerate(nummbers,start=1):
    print(i,item)


#2>>> list comprehension
list1 = [12,24,2,23,21,9,3,21,5,7,8]
list2 = [item for item in list1 if item>15]
print(list2)


#3>>> map:
values = [ 1,2,3,4,5]
def square(x):
    return x**2
square_of_values = map(square,values)
print(list(square_of_values))

# # Another way:
sq_of_val = list(map(lambda x:x**2 , values))
print(sq_of_val)


#4>>> Filter:
a_list = [2,3,4,6,7,8,9]
new_lst = list(filter(lambda i:i>5 , a_list))
print(new_lst)

#5>>> Reduce :
from functools import reduce
sr_lst = [1,2,3,4,5]
sr_lst_2 = reduce(lambda i1 ,i2: i1+i2 ,sr_lst)
print(sr_lst_2)