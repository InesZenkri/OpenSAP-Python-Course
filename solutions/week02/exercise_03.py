num_rows = int(input("Please enter the number of rows in the matrix: "))
num_cols = int(input("Please enter the number of columns in the matrix: "))

matrix = []
print("Enter the matrix values:")
for i in range(num_rows):
    row = [] 
    for j in range(num_cols):
        value = int(input("Value:"))
        row.append(value) 
    matrix.append(row) 

for i, row in enumerate(matrix):
    row_sum = sum(row)
    print("Sum of row ",i+1,":", row_sum)