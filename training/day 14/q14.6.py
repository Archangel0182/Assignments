num = int(input("Enter a number: "))
reverse = 0
temp = num

while temp != 0:
    remainder = temp % 10
    reverse = reverse * 10 + remainder
    temp //= 10

print("Reverse:", reverse)
print("Double of reverse:", reverse * 2)
