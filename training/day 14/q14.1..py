def single_digit(num):
    digit_sum = sum(int(digit) for digit in str(num))
    if digit_sum < 10:
        return digit_sum
    return single_digit(digit_sum)

num = int(input("Enter a number: "))
result = single_digit(num)
print("Sum of digits (single digit):", result)
