with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]
numbers.sort(reverse=True)
for i in range(3):
    print(numbers[i])