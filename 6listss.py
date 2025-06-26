l = [2,3,4,"shreya", True , 6 , 7]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])

print(l[-3])
print(l[-2])

if 7 in l:
    print('yes')
else:
    print('no')

#sams thing applies to strings
if "hreya" in "Shreya":
    print("yes")

print(l[1:8])
print(l[1:8:2])


# #list comprehension
lst=[i*i for i in range(4)]
print(lst)
#

lst=[i*i for i in range(10) if i%2==0]
print(lst)

lst=[7,2,3,6,8,10]
print(lst[1:4])
print(lst[1:5:2])

#list methods
l = [11,45,1,2,4,6,1]
print(l)
l.append(7)
l.sort()
l.sort(reverse=True) #in descending order
l.reverse()
print(l.index(1))
print(l.count(1))

m = l.copy()
m[0] = 0
print(l)

l.insert(1, 899)
print(l)

m = [100,200,300]
l.extend(m)
print(l)

k = l+m
print(k)

#get user input and split it into list
user = input("enter elements:").split()
print("List:",user)

#get user input using loops
a=[]
n = int(input("enter the number of elements"))
for i in range(n):
    elements = input(f"enter element{i+1}:")
    a.append(elements)
print("List:",a)

#get list using map
#get input,split it, and convert to integers
user = list(map(int, input("enter numbers separated by space:").split()))
print("List:", user)

#using loop and input()
n = int(input("enter the number of elements:"))
a = [input(f"Enter elements {i+1}:")for i in range(n)]
print("List:", a)

#accepting a nested list input
user = [x.split(",")for x in input("Enter nested list(use comma and semicolon):").split(";")]
print("Nested List",user)