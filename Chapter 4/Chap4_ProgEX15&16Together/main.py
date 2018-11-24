#combines the 2 shapes and problems into 1 program
x=int(input("Press 1 to run Problem 14\nPress 2 to run Problem 15\nYour choice: "))
while x<1 or x>2:
    x=int(input("Invalid option again, please try again: "))
if x==1:
    star=int(input("Enter the number of rows and columns you wish to see: "))
    for row in range(star, 0, -1):
        for col in range(row):
            print('*', end='')
        print()
else:
    num=int(input("Enter the amount of rows and columns you wish to see: "))
    count=1                 #runs the counter to print the pound
    for row in range(num):
        for col in range (num+1):
            if (col==0 or col==count):
                print("#", end='')
            else:
                print(" ", end='')
        print()
        count+=1