print("Welcome to tip calculator")
import math
# Get the values
bill = float(input("What was the total bill? $"))
percentage = int(input("How much tip you like to give? 10, 12, 15 or 0? "))
peoples = int(input("How many people to split the bill? "))

# Calculate total
total_tip = bill * percentage / 100
total_with_tip = bill + total_tip
bill_person = total_with_tip / peoples
total = round(bill_person, 2)

message = f"Each person should pay: ${total}"
print(message)
