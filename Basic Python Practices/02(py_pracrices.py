#1

inp = int(input("Enter a nummber : "))
rem = inp % 2
print("Reminder : ",rem)

#2
n = int(input("Enter no. :"))
print("Square: ",(n*n))

#3
def greet():
    take = input("Enter name: ")
    print(f"Good morning {take}")

greet()

#4
v = input("Enter a sentence: ")
print(v.replace("  "," "))