def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

def calculate_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = calculate_lcm(num1, num2)
hcf = calculate_hcf(num1, num2)

print("LCM:", lcm)
print("HCF:", hcf)