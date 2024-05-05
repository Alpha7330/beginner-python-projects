print("Thank you for choosing Python Pizza Deliveries!")
size = input("enter size\n") # What size pizza do you want? S, M, or L
add_pepperoni = input("enter Y or N\n") # Do you want pepperoni? Y or N
extra_cheese = input("enter Y or N\n") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
s=size
a=add_pepperoni
e=extra_cheese
bill=0
if s=='S':
  bill+=15
elif s=='M':
  bill+=20
elif s=='L':
  bill+=25
else:
  None
if a=='Y' and s=='S':
  bill+=2
elif a=='Y' and (s=='M' or s=='L'):
  bill+=3
else:
  None
if e=='Y':
  bill+=1
else:
  None
print(f"Your final bill is: ${bill}.")  
  

  
  