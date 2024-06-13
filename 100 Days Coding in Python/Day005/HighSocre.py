# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n]) # type: ignore

# Write your code below this row 👇
max_score=max(student_scores)
print(max_score)
#
#
# Or
highest_score=0
for s in student_scores:
  if s>highest_score: # type: ignore
    highest_score=s
print('The highest score in the class is: {}'.format(highest_score))  