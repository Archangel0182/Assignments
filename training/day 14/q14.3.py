n = int(input("Enter a number: "))

for num in range(1, n + 1):
    if num % 3 != 0:
        continue
    print(num ** 3)