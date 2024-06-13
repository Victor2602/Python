
print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10,12 or 15? "))
split=int(input("How many people to split the bill? "))
percentage_tip=tip/100
final_price=bill*percentage_tip
split_number=((final_price+bill)/split)
#sn=round(split_number,2)#Aproximação decimal de 2 digitos.
sn="{:.2f}".format(split_number)
print(f"Each person should pay: {sn}")