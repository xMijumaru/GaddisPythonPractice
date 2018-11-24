#This program will account for the sum of all numbers
print("Enter a list of positive numbers, and enter -1 when finished")
x=0
counter=1           #checks the counter for the variables
total=0             #checks the total amount
while(x>=0):
    print("Enter Number",counter,": ", end='')
    x=int(input())
    if (x>0):
        total+=x
        counter+=1
    else:
        print("The sum of the values =", total)



