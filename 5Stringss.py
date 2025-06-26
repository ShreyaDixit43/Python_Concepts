#Strings

apple = "he wants to eat apple\n she wants to eat apple"
print("sentence: " + apple)
st = '''#Hii, My name is shreya
#computer science grad
'''
print(st)

#accesing characters of a string
name = "Shreya"
print(name[0])
print(name[1])

#looping through string
for character in name:
    print(character)

#string slicing
name = "shreya,priya"
print(len(name))
print(name[0:5])

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word")
print(fruit[1:4]) #including 1 but not 4
print(fruit[0:-3])
print(fruit[-1:-3]) #5-1=4 5-3=2 not a correct comdition
print(fruit[-3:-1])# here len(fruit) i.e, 5-3=2 is n and 5-1=4 4 is ignored and g is printed so,ng
print(fruit[-2:-1])
print(fruit[0:5])
nm = "Harry"
print(nm[-4:-2])

#string methods
#strings are immutuable but can change by copying the existing string into new string
a = "Shreya"
b = "shreya!!!!"
c = "shreya priya yash"
print(a.upper())
print(a.lower())
print(b.rstrip("!"))
print(a.replace("Shreya","priya"))
print(c.split(" "))

d = "hello"
print(d.capitalize())
print(d.center(50))

e = (" Shreya is excellent in python,"
     "Shreya aspire to become a python developer")
print(e.count("Shreya"))
print(e.count("python"))
print(e.endswith("r"))
print(e.endswith("is",4,10))
print(e.find("is")) #return index of "is" else it will return -1
print(e.index("is")) #return index of "is" else throws an exception error

f="WelcomeToPython"
print(f.isalnum())  #checks for A-Z,a-z,0-9
print(f.isalpha())  #checks for only A-Z,a-z and not 0-9
print(f.islower())
print(d.islower())
print(f.isprintable())
print(f.isspace())
print(f.startswith("Welcome"))
print(f.swapcase())



