# Which year do you want to check?
year = int(input("enter year\n"))
y=year
if y%4==0:
  if y%100==0:
    if y%400==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

