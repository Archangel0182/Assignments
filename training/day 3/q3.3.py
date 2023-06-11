friends = ["A", "B", "C", "D", "E"]

print(friends)  # Output: ["A", "B", "C", "D", "E"]

print(friends[0])  # Output: A
print(friends[2])  # Output: C

friends[1] = "B2"
print(friends)  # Output: ["A", "B2", "C", "D", "E"]

friends.append("C2")
print(friends)  # Output: ["A", "B2", "C", "D", "E", "C2"]

friends.remove("C")
print(friends)  # Output: ["A", "B2", "D", "E", "C2"]

index = friends.index("D")
print(index)  # Output: 2

count = friends.count("E")
print(count)  # Output: 1

friends.sort()
print(friends)  # Output: ["A", "B2", "C2", "D", "E"]

friends.reverse()
print(friends)  # Output: ["E", "D", "C2", "B2", "A"]
