# Calculate Profit or Loss
# Input cost price and selling price. Display either:
# Profit and amount, or
# Loss and amount, or
# No Profit No Loss

print("Enter Cost of item;")
cost=float(input("Enter Cost: "))
selling=float(input("Enter Selling price: "))
if cost>selling:
    print("Loss")
elif cost<selling:
    print("profit")
else:
    print("no profit no loss")    
    