#The purpose of this program is to calculate the amount of sales tax in a current item
y=0.025 #the sales tax in the current county
x=.05   #The sales tax in the current state
print('Sales Tax calculator')
z=float(input('Enter the Purchase amount of the item purchased: '))
State=z*x
County=z*y
Total=State+County+z
print("The State Tax: ",format(State,",.02f"))
print("The County Tax: ", format(County,',.02f'))
print("The Total Price: ", format(Total,',.02f'))
