with open("secret.txt", "r") as file1:
    secret_list = [line.strip() for line in file1]
with open("key.txt", "r") as file2:
    key_list = [int(line.strip()) for line in file2]

col, row = key_list 
grid = []
pos = 0
while pos < len(secret_list):
    row_chars = []
    for _ in range(col):
        if pos < len(secret_list):
            row_chars.append(secret_list[pos])
            pos += 1
    grid.append(''.join(row_chars))
with open("public.txt", "w") as file3:
    for row in grid:
        file3.write(row + '\n')