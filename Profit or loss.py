actual_cost = float(input(" PLease Enter the actual cost of the the item: "))
sale_amount = float(input(" Please Enter the sale amount of the item: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit")