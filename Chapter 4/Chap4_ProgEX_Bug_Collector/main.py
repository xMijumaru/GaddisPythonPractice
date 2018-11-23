#Checks the number of bugs collected by the catcher in 5 days
MAX=int(input("How many days did you collect: "))
print("Enter the number of bugs collected on ", end='')
total=0.0
for collect in range(MAX):
    print("Day ", collect + 1, end='')
    day=float(input(': '))
    total+=day
print("The total amount of Bugs caught for", MAX, "days =", total) #sep=' ')

