#this current program will be used to convert temprature
#This will purposely use the string literal to float
#conversion
print("This program will convert Celsius to Fahrenheit")
x=input("What is the Celsius Temperature you wish to convert: ")
y=float(x)  #converts the string literal into a floating point variable
F=float(((9.0//5.0)*y)+32.0)
print("The Celsius Temperature: ", format(F,'.02f'))
#THE FORMULA IN THE BOOK IS INCORRECT