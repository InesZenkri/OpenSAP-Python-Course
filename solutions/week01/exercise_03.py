angle1 = int(input("Please enter the first angle: "))
angle2 = int(input("Please enter the second angle: "))
angle3 = int(input("Please enter the third angle: "))

if angle1 <= 0 or angle2 <= 0 or angle3 <= 0 or angle1 + angle2 + angle3 != 180:
    print("The entered values are not valid.")

if angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("The triangle is a right triangle.")
elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    print("The triangle is an obtuse triangle.")
else:
    print("The triangle is an acute triangle.")