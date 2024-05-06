# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# p=position
# if p=='A1':
#   line1[0]='X'
# elif p=='A2':
#   line2[0]='X'
# elif p=='A3':
#   line3[0]='X'
# else:
#   None
# if p=='B1':
#   line1[1]='X'
# elif p=='B2':
#   line2[1]='X'
# elif p=='B3':
#   line3[1]='X'
# else:
#   None
# if p=='C1':
#   line1[2]='X'
# elif p=='C2':
#   line2[2]='X'
# elif p=='C3':
#   line3[2]='X'
# else:
#   None
# print(f"{line1}\n{line2}\n{line3}")

########################################################################
#efficient code

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
p=position
let=p[0].lower()
list=['a','b','c']
l_index=list.index(let)
num_index=int(p[1])-1
map[num_index][l_index]='X'
print(f"{line1}\n{line2}\n{line3}")