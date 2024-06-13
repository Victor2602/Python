target = int(input("Put a number:")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
n1=0
for p in range(0,target+1,2):
    n1+=p
print(n1)