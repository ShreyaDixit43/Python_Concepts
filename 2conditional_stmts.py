#conditional statements

a = int(input("Enter your age ="))
print("your age is :", a)

#conditionl operators
# print(a<18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>8):
   print("you can drive")
else:
   print("you cannot drive")
print("yay!")

applePrice = 210
budget = 200
if(applePrice <= budget):
   print("add 1kg Apples to the cart")
else:
   print("do not add Apples")


#elif statements
num = int(input("enter the value of num"))
if(num < 0):
   print("Number is negative")
elif(num == 0):
   print("Number is zero")
else:
   print("Number is positive")


num = int(input("enter the value of num"))
if(num<0):
   print("num is negative")
elif(num > 0):
   if(num <= 10):
      print("number is between 1-10")
   elif(num > 10 and num <= 20):
      print("Number is between 11-20")
   else:
      print("Number is greater than 20")
else:
   print("Number is zero")


import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)



#match-case statments

x = int(input("enter the number"))
match x:
   case 0:
      print("x is zero")
   case 4:
      print(x,"case is 4")
   case _ if x!=90:
      print(x, "is not 90")
   case _ if x!=80:
      print(x, "is not 80")
   case _:
      print(x)

#if... else in one line
a = 20
b = 30
print("A") if a > b else print("=") if a == b else print("B")

c=9 if a>b else 0
print(c)