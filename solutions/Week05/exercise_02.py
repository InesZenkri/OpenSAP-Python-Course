def is_even(number):
    return number % 2 == 0

for x in range(100):
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is not even")