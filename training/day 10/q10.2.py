start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Multiples of 3 and 5:")
for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
