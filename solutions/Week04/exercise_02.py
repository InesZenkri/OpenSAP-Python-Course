with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

even_numbers = [str(num) + '\n' for num in numbers if num % 2 == 0]

with open("even_numbers.txt", "w") as even_file:
    even_file.writelines(even_numbers)
print("List of even numbers created!")