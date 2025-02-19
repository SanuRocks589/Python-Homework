def change(amount, given):
    return given-amount

amount = int(input("Enter total bill amount:"))
given = int(input("Enter the amount of money you gave:"))
print("Your change is", change(amount, given)) 
