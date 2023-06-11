N = int(input(" Enter the number of commands to be executed: "))
i = 0
l = []

while i < N:
    comm, *args = input().split()
    args = [int(x) for x in args]  # Convert arguments to integers

    if comm == 'insert':
        l.insert(args[0], args[1])  # Insert an element at the specified index in the list
    elif comm == 'print':
        print(l)  # Print the current state of the list
    elif comm == 'remove':
        l.remove(args[0])  # Remove the first occurrence of the specified element from the list
    elif comm == 'append':
        l.append(args[0])  # Add an element at the end of the list
    elif comm == 'sort':
        l.sort()  # Sort the list in ascending order
    elif comm == 'pop':
        l.pop()  # Remove and return the last element from the list
    elif comm == 'reverse':
        l.reverse()  # Reverse the order of elements in the list

    print(l)  # Print the updated list
    i += 1
