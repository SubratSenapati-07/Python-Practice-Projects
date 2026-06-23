#1

check = input("Enter a sentence here: ")
check1 = check.find("  ")
if check1 == -1:
    print("Double Space not founded")
else:
    print("Double Space founded")


#2

a = int(input("Enter no. : "))
b = int(input("Enter no. : "))
c = int(input("Enter no. : "))
lst = [a,b,c]
print("IN sort manner: ",sorted(lst))

#3

list = sum([12,45,89,32,11])
print("Sum: ",list)

#4
ls = [1,0,3,7,9,0,0,0,4,5,2,9,2,2,2,0,5]
print("No. of zeros: ",ls.count(0))

#5
hn_words = { "Orange": "Santra","Potato" : "Aalu"}
ur_inp = input("Enter your key: ")

print(hn_words.get(ur_inp))
