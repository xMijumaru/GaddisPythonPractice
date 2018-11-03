#this program displays the roulette wheel colors
pocket=int(input("Enter a Roulette Pocket number: "))

if pocket==0:
    print ("Pocket 0 is green ")
elif pocket>=1 and pocket <=10:
    if pocket%2==0:
        print("The pocket is black")
    else:
        print("The pocket is red")
elif pocket>=11 and pocket<=18:
    if pocket%2==0:
        print("The pocket is red")
    else:
        print("The pocket is black")
elif pocket>=19 and pocket <=28:
    if pocket%2==0:
        print("The pocket is black")
    else:
        print("The pocket is red")
elif pocket>=29 and pocket<=36:
    if pocket%2==0:
        print("The pocket is red")
    else:
        print("The pocket is black")
else:
    print("Invalid number chosen")