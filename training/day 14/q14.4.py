total_students = 10
roll_numbers = []
marks = []

for i in range(total_students):
    while True:
        roll_number = int(input(f"Enter roll number for student {i+1}: "))
        if roll_number >= 1000 and roll_number <= 9999:
            break
        print("Invalid roll number. Please enter again.")

    roll_numbers.append(roll_number)

    total_marks = 0
    for j in range(3):
        marks_input = int(input(f"Enter marks for subject {j+1}: "))
        if marks_input >= 40:
            total_marks += marks_input

    marks.append(total_marks)

total_above_200 = 0
highest_total = 0
highest_roll_number = 0

for i in range(total_students):
    if marks[i] > highest_total:
        highest_total = marks[i]
        highest_roll_number = roll_numbers[i]

    if marks[i] > 200:
        total_above_200 += 1

print("Total students with total marks above 200:", total_above_200)
print("Roll number of student with highest total marks:", highest_roll_number)
