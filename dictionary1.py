student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# Create an empty dictionary called student_grades.
student_grades={}
#Write your code below to add the grades to student_grades.👇
for score in student_scores :
  if (student_scores[score] >= 91) and (student_scores[score] <= 100):
      student_grades [score]= "Outstanding"
  if (student_scores[score] >= 81) and (student_scores[score] <= 90):
      student_grades [score]= "Exceeds Expectations"
  if (student_scores[score] >= 71) and (student_scores[score] <= 80):
      student_grades [score]= "Acceptable"
  if  (student_scores[score] <= 70):
      student_grades [score]= "Fail"
print(student_grades)