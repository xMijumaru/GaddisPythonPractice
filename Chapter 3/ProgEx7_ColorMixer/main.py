#the purpose of this program is to run a color mixer
x=input("Enter the first color you wish to mix: ")
y=input("Enter the second color you wish to mix: ")

if x=="red" and y=="blue" or x=="blue" and y=="red":
    print("you get purple")
elif x=="red" and y=="yellow" or x=="yellow" and y=="red":
    print("You get Yellow")
elif x=="blue" and y== "yellow" or x=="yellow" and y== "blue":
    print ("You get green")
else:
    print ("Invalid options chosen")