print("The Love Calculator is calculating your score...")
name1 = input("enter name1\n") # What is your name?
name2 = input("enter name2\n") # What is their name?
n=name1+name2
n=n.lower()
t=n.count('t')
r=n.count('r')
u=n.count('u')
e=n.count('e')
c1=t+r+u+e
l=n.count('l')
o=n.count('o')
v=n.count('v')
e=n.count('e')
c2=l+o+v+e
a=int(str(c1)+str(c2))
if a<10 or a>90:
  print(f"Your score is {a}, you go together like coke and mentos.")
elif a>40 and a<50:
  print(f"Your score is {a}, you are alright together.")
else:
  print(f"Your score is {a}.")
