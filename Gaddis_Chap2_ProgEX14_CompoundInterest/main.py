#the purpose of this program is to calculate the compunt interest
#made within a bank
#A=P(1+rn)nt
P=float(input("Enter the amount of principal originally deposited into the account: "))
R=float(input("Enter the annual interest rate paid by the account: "))
T=float(input("Enter the number of years the account will be left to earn interest: "))
N=float(input("Enter the numbers of times per year that the interest will be compounded: "))
NewR=R*(0.01)
compInt=P*(1+(NewR*N))**(N*T)
print("The amount of money that will be deposited after", T, "years: $",format(compInt,',.02f'))