#https://www.geeksforgeeks.org/python-list-exercise/
#Given a list, write a Python program to swap first and last element of the list.
list= [12, 35, 9, 56, 24]
el1=list.pop()
list.pop(0)
el2=list.insert(0,24)
el3=list.insert(len(list),12)
print(list,'\n')
##
##
list2=[10,20,30,40,50]
elf1=list2.clear()
l=[50,20,30,40,10]
elf2=list2.extend(l)
print(list2)