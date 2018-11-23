#the purpose of this program is to check the amount of resturants available
x=input("Is anyone in your party a vegetarian?: ")
y=input("Is anyone in your party a Vegan?: ")
z=input("Is anyone in your party gluten-free?: ")
print("Here are your restaurant choices: ")
s1="Joe's Gourmet Burgers"
s2="Main Street Pizza Company"
s3="Corners Cafe"
s4="Mama's Fine Italian"
s5="The Chefs Kitchen"
if x=="yes" or x=="Yes":
    a=1
elif x=="No" or x=="no":
    a=0
else:
    a=2

if y=="yes" or y=="Yes":
    b=1
elif y=="No" or y=="no":
    b=0
else:
    b=2

if z == "yes" or z == "Yes":
        c = 1
elif x == "No" or x == "no":
        c = 0
else:
    c = 2

if a==1 and b==1 and c==1:
    print(s5,'\n',s3)
elif a==0 and b==0 and c==0:
     print(s1)
elif a==1 and b==0 and c==0:
    print(s2,'\n',s3,'\n',s4,'\n',s5)
elif a==0 and b==1 and c==0:
    print(s3,'\n',s5)
elif a==0 and b==0 and c==1:
    print(s2,'\n',s3,'\n',s5)
elif a==1 and b==1 and c==0:
    print(s5,'\n',s3)
elif a==0 and b==1 and c==1:
    print(s5,'\n',s3,'\n')
elif a==1 and b==0 and c==1:
    print(s2,'\n',s3,'\n',s5)

