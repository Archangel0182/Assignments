#append(): This method adds an element to the end of a list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

#pop(): This method removes and returns the last element from a list, or the element at a specified index.
fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop()
print(removed_fruit)  # Output: "cherry"
print(fruits)  # Output: ['apple', 'banana']

#remove(): This method removes the first occurrence of a specified element from a list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']

#sort(): This method sorts the elements of a list in ascending order.
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3]