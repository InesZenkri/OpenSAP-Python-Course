stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]

sell_list = []

for stock in stocks:
    change_percentage = (stock[2] / stock[1]) * 100 
    if change_percentage > 5:
        sell_list.append(stock[0]) 

print("Stocks to consider selling due to more than +5% change:", sell_list)