#the purpose of this program is to calculate the discount of software sales/
print("This specific piece of software sells for $99: ")
x=float(input("How many would you like to purchase: "))
total=99*x      #the total number of packages with respect with price
if x<10:
    print("The price is $", format(total,',.02f'),sep='')
elif x>10 and x<19:
    a=0.10*total
    newTot=total-a
    print("The discount taken was:", format(.1,'.0%'))#zero sets precision
    #ex) '.2%' prints 10.00 percent and no num prints outs a precision of 5
    print("The price is $", format(newTot,',.02f'),sep='')
elif x>=20 and x<50:
    a=.20*total
    new=total=a
    print("The discount taken was:", format(.2,'.0%'))
    print("The price is $", format(new,',.02f'), sep='')
elif x>=50 and x<100:
    a=.30*total
    tot=total-a
    print("The discount taken was:", format(.3,'.0%'))
    print("The price is $",format(tot,',.02f'), sep='')
elif x>=100:
    last=.40*total
    tot=total-last
    print("The discount taken was:",format(.4,'.0%'))
    print("The price is $", format(tot,',.02f'),sep='')
else:
    print("Invalid Option chosen")

