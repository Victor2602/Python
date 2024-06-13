# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n]) # type: ignore
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height=0
for height in student_heights:
    total_height+=int(height)
print('total height = {}'.format(total_height))
total_students=0
for students in student_heights:
    total_students+=1
print('number of students = {}'.format(total_students))
average_height=round(total_height/total_students)
print('average height = {}'.format(average_height))