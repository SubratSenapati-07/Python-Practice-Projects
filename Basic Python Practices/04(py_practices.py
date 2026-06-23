#1
 
for item in range(8):
    z = {int(input("Enter a number:"))}
    
#2
evenOdd = lambda n: n/2==0 
z = evenOdd(4)
print(z)

#3
a = "{} is a good boy!".format("Subrat")
print(a)

b = "{1} is a good boy! {0}".format("Subrat","okay")
print(b)