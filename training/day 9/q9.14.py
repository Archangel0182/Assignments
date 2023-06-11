units = float(input("Enter the electricity units consumed: "))

if units <= 50:
    total_bill = units * 0.5
elif units <= 150:
    total_bill = 25 + (units - 50) * 0.75
elif units <= 250:
    total_bill = 100 + (units - 150) * 1.2
else:
    total_bill = 220 + (units - 250) * 1.5

total_bill *= 1.2  # Adding 20% surcharge

print("Total Electricity Bill:", total_bill)
