student_scores = input("enter students score \n").split(",")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
temp=student_scores[0]
for i in student_scores:
  if i>temp:
    temp=i
    
print(f"The highest score in the class is: {temp}") 