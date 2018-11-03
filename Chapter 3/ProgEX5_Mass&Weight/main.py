#The purpose of this program is to calculate weight using newtons
x=float(input("What is the the mass of the object in KG: "))
weight=x*9.8;   #the equation in the textbook
y= "Newtons"
print("The object weights :",format(weight,'.02f'), y)
if weight>500:
    print("The object is too heavy")
elif weight<100:
    print("The weight is too light")
else:
    print ("The weight is within range")