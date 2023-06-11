n = int(input(" Enter the number of students: "))
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input()
tot=0.00
if query_name in student_marks:
    for i in student_marks[query_name]:
        tot+=i
n1=len(student_marks[query_name])
avg=tot/n1
print("%.2f" %avg)