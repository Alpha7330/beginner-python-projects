import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("play with 0 for rock, 1 for paper, 2 for scissors\n")

play=int(input())
com=random.randint(0,2)
if play==0:
    print(rock)
elif play==1:
    print(paper)
elif play==2:
    print(scissors)   
else:
    None
print(f"computer chose {com}")    
if com==0:
    print(rock)
elif com==1:
    print(paper)   
elif com==2:
    print(scissors)    
else:
    None
if play==0 and com==2:
    print("You Win")
elif play==2 and com==0:
    print("You Lose")    
elif play>com:
    print("You Win") 
elif play==com:
    print("Draw")
elif play<com:
    print("You Lose")
else:
    None
