def dueAmount(bill,paid_amount):
    return bill - paid_amount

bill=5000
paid_amount=int(input("Enter paid amount: "))
due=(dueAmount(bill,paid_amount))

if due>0:
    print("Due amount is:",due)
else:
    pass 
print("Thank you for paying the bill on time.")