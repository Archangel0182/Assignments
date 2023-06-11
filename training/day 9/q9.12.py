physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))
biology = float(input("Enter marks in Biology: "))
mathematics = float(input("Enter marks in Mathematics: "))
computer = float(input("Enter marks in Computer: "))

total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("Percentage:", percentage)
print("Grade:", grade)
