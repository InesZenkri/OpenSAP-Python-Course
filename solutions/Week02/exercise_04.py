initial_stock = int(input("Please enter the initial stock level: "))
num_months = int(input("Please enter the number of months to plan: "))

sales = [int(input("Please enter the planned sales quantity: ")) for month in range(num_months)]

current_stock = initial_stock
production_quantities = [0] * num_months

for i in range(num_months):
    if sales[i] > current_stock:
        production_quantities[i] = sales[i] - current_stock
    current_stock = max(0, current_stock - sales[i])

print("\nThe resulting production quantities are:")
for month, production in enumerate(production_quantities, start=1):
    print("Production quantity month ",month ,"-" ,production)