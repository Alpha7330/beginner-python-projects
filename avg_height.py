# Input a Python list of student heights
student_heights = input("enter student heights \n").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total=0
n=len(student_heights)
for i in student_heights:
  total+=i
  
avg_height=total/n
avg_height=round(avg_height)
print(f"total height = {total}")
print(f"number of students = {n}")
print(f"average height = {avg_height}")