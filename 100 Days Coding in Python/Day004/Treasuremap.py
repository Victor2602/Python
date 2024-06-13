line1 = ["a1","b1","c1"]
line2 = ["a2","b2","️c2"]
line3 = ["a3","b3","c3"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
#column1=line1[0] or line2[0] or line3[0]
#column2=line1[1] or line2[1] or line3[1]
#column3=line1[2] or line2[2] or line3[2]
#if position=="A1":
#    x_1=line1.remove(line1[0])
#    x1=line1.insert(0,"X")
#elif position=="A2":
#    x_2=line2.remove(line2[0])
#    x2=line2.insert(0,"X")
#elif position=="A3":
#    x_3=line3.remove(line3[0])
#    x3=line3.insert(0,"X")
#elif position=="B1":
#    y_1=line1.remove(line1[1])
#    y1=line1.insert(1,"X")
#elif position=="B2":
#    y2=line2.insert(1,"X")
#elif position=="B3":
#    y_3=line3.remove(line3[1])
#    y3=line3.insert(1,"X")
#elif position=="C1":
#    z_1=line1.remove(line1[2])
#    z1=line1.insert(2,"X")
#elif position=="C2":
#    z_2=line2.remove(line2[2])
#    z2=line2.insert(2,"X")
#else:
#    z_3=line3.remove(line3[2])
#    z3=line3.insert(2,"X")
letter=position[0].upper()
abc=["A","B","C"]
letter_position=abc.index(letter)
number=position[1]
number_position=int(number) - 1
map[number_position][letter_position]="X"




# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

