# Program to display first 10 numbers in geometric series

a = int(input("Enter first number : "))
r = int(input("Enter common ratio : "))

print("The first 10 numbers of the geometric series are : ")

for i in range(10):
    x = a * (r**i)
    print(x)



