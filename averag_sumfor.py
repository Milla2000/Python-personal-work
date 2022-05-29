student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

students= 0
for s in student_heights:
    students += s
print(f"{students}") 
no = 0
for t in student_heights:
    no +=1
average=round(students/no)
print(f"{average}")