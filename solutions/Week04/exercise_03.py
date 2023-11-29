with open("invoice_data.txt", "r") as file:
    list_tuples = [line.split() for line in file]
for item in list_tuples:
    print(f"{item[0]:15s}{int(item[1]):3d}{float(item[2]):7.2f}{(float(item[1])*float(item[2])):8.2f}")