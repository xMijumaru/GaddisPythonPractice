#the purpose of this program is to calculate the sales given a 23% profit

print("The total amount of profit this quarter is estimated"
      " to be 23%")
x=float(input("\nEnter the amount of projected sales made "
               "this quarter: "))

profit=x*0.23

#display the amount of profit made
print("The Total Profit this quarter: $", format(profit,',.2f'))
total=x+profit
print("The total amount of sales made this quarter: $", format(total,',.2f'))

