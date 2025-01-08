def dueamt(p,g):
    change= g - p
    return change

price= int(input("Enter the price: "))
given= int(input("Enter the given amount: "))

print(f"The change recieved is: {dueamt(price, given)}")