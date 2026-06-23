#1. Write a Python program to reverse a string using slicing.
string = input("Enter a String: ")
rev = string[::-1] 
print(rev)

#2. Write a function remove_duplicates(lst) that removes duplicate elements from a list.

#drawback : it change the order of elements.
# def remove_duplicates(lst):
#     rem_dup = set(lst)
#     print("Without duplicate list:",rem_dup)

# let_a_list = ["Sonali","Subh","Subrat","Sagar","Subrat","Subh","Ayush"]
# remove_duplicates(let_a_list)
    
def remove_duplicates(lst):
    not_dup = []
    for item in lst:
        if item not in not_dup:
            not_dup.append(item)
    return not_dup

l = ["Sonali","Subh","Subrat","Sagar","Subrat","Subh","Ayush"]
print("List without Duplicates element:",remove_duplicates(l))

# Input from user:
def remove_dup(lst):
    no_dup =[]
    for i in lst:
        if i not in no_dup:
            no_dup.append(i)
    return no_dup
user_list = list(input("Enter element just a space separated:").split())
print("List without containg Duplicate value:",remove_dup(user_list))