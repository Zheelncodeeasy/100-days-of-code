print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


# Calculating total bill amount with the tip included
total_bill_amount =  bill * (1 + tip / 100)

# Dividing the total bill amount by number of people
amount_per_person = total_bill_amount / people

# Using f-strings to print the amount rounded to two decimal places to be paid per person
print(f"Each person should pay ${amount_per_person:.2f}")

