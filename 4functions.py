def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

a=6
b=8
if(a>b):
    print("first number is greater")
else:
    print("second number is greater or equal")
calculateGmean(a, b)

c = 8
d = 7
if(c>d):
    print("first number is greater")
else:
    print("second number is greater or equal")
calculateGmean(c, d)


def isGreater(a, b):
    if (a > b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

a=6
b=8
isGreater(a, b)
calculateGmean(a, b)
c=9
d=4
isGreater(c, d)
calculateGmean(c, d)

def isLesser(a, b):
    pass

#function argumnets

def average(a, b):
    print("The average is", (a+b)/2)
average(4, 6)

def average(a=9, b=1): #default arguments
    print("The average is", (a+b)/2)
average(1, 5)

#keyword arguments
def name(fname, mname, lname):
    print("hello",fname, mname, lname)
name("Peter", "Ego", "quill")

#arbitary arguments
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:" , sum /len(numbers))
average(5, 6)

#keyword arbitary arguments
def name(**name):
    print("Hello!",name["fname"],name["mname"],name["lname"])
name(mname="Subhash", lname="Dixit", fname="Shreya")

#recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))




