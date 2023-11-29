import random
import math

random_x = [random.random() for n in range(10000)]
random_y = [random.random() for n in range(10000)]
count = 0
for i in range(len(random_x)):
    if (random_x[i]**2 + random_y[i]**2) < 1:
        count += 1
calc_p = 4*count/len(random_x)

print("Calculated value of π:", calc_p)
print("Value of π from math library:", math.pi)
print("Difference:", math.pi - calc_p)