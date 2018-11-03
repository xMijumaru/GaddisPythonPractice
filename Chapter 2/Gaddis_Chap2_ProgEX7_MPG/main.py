#the purpose of this program is to calculate the MPG of a vehicle
print('This program is designed to calculate the total MPG of '
      'a vehicle')
miles=float(input("How many miles were driven?: "))
Gal=float(input("How many Gallons were used?  : "))
total=miles/Gal
print("The Total MPG of the Vehicle is: ",
      format(total,',.02f'), "mile(s)")