nb1 = int(input("Please enter the first number: "))
nb2 = int(input("Please enter the second number: "))
nb3 = int(input("Please enter the third number: "))
max = 0

if nb1 > nb2:
    max = nb1
else:
    max = nb2

if nb3 > max:
    max = nb3

print("The largest number is", max)