num = int(input("Enter the number of terms: "))

fibonacci_sequence = [0, 1]

if num <= 0:
    print("Enter a positive integer")
elif num == 1:
    print("Fibonacci sequence:", fibonacci_sequence[0])
elif num == 2:
    print("Fibonacci sequence:", fibonacci_sequence)
else:
    for i in range(2, num):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    print("Fibonacci sequence:", fibonacci_sequence)
