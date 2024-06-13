#if/else statements.
#print(5%2). % módulo com resto, no caso 5%2=1;
number=int(input('Choose a number:\n'))
if number%2==int():
    print('This is an even number.')
else:
    print('This is an odd number.')
condition=True
if condition:#If the 'condition' is true, goes to nested if/else(line 11-13), if not goes to else(line 15)
    another_condition=True
    if another_condition:#If the 'another_condition' is true, goes to print('Do this.')(line 12), else goes to print('Do not do this.')
        print('Do this.')
    else:
        print('Do not do this.')
else:
    print('Finish the program.')
#Ou seja, se 'condition'==True segue para o if/else identado, senão segue para o else(linha 15).
#LOGICAL OPERATORS:
# a and b == True, only when both are true.
# a or b == False, only when both are false.
# not a == True, when a == False, meaning that invert the boolean value of a. 