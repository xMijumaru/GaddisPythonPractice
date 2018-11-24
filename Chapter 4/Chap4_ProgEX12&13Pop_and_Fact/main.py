#does the factorial and population problem
x=int(input("Enter 1 to calculate a Factorial\nPress 2 for the Population problem\nYour Choice: "))
while(x<1 or x>2):
    x=int(input("Invalid Option, Please try again: "))
if x==1:
    total=1
    factorial=int(input("What Factorial would you like to Calculate: "))
    for fact in range(factorial):
        total*=(fact+1)
    print(format(total,',.0f'))
if x==2:
    #does the population increase
    start=int(input("Starting Number of Organisms: "))
    y=int(input("Average Daily increase: "))
    z=int(input("Number of Days they will multiply: "))

    print("Day Approximate Population")
    total=x
    for pop in range(z):
        print(pop+1,end='   ')
        print(total)
        Inc=total*(y*1e-2)
        total+=Inc
