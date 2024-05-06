import random
name_string=input("enter names with ,\n")
names=name_string.split(",")
names=list(names)
b=random.choice(names)
print(f"{b} is going to the bill today!")
