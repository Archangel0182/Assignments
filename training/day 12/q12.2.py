# Prompt the user for four integer inputs
x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))
z = int(input("Enter the value for z: "))
n = int(input("Enter the value for n: "))

# Create lists with values ranging from 0 to x, y, and z respectively
list1 = [i for i in range(x + 1)]
list2 = [j for j in range(y + 1)]
list3 = [k for k in range(z + 1)]

# Print the values of list1, list2, and list3
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

# Create a list of combinations where the sum of i, j, and k is not equal to n
list4 = [[i, j, k] for i in list1 for j in list2 for k in list3 if (i + j + k) != n]

# Print the resulting list of combinations
print("List of combinations (excluding sum equal to n):")
print(list4)
