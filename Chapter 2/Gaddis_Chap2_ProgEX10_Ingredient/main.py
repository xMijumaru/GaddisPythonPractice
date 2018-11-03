#this program will run the ingredients needed to produce cookies
amount=int(input('How many cookie(s) do you wish to make: '))
#this is the amount that makes 48 cookies
sugar=1.5/48.0
butter=1/48.0
flour=2.75/48.0
#reminder that // is int division and / is float division
print("Amount to make ",amount, " cookie(s)")
print("Sugar:  ", format(sugar*amount, ',.02f'), "cups")
print("Butter: ", format(butter*amount,',.02f'), "cups")
print("Flour: ", format(flour*amount,',.02f'), "cups")