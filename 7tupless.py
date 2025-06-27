tup = (1,2)
print(type(tup), tup)

tupp = (1,2,"shreya",6,8,9)
print(tupp)
print(tupp[0])
print(tupp[1])
print(tupp[2])

print(tupp[-3])

if 345 in tup:
    print("yes")
else:
    print("no")
#
tup1 = tupp[1:4]
print(tup1)

tup2 = tupp[1:4:2]
print(tup2)

#operations

fruits = ["apple","mango","pineapple","grapes"]
temp = list(fruits)
temp.append("orange")
temp.pop(2)
temp[2] = "mango"
fruits = tuple(temp)
print(fruits)

#we can concatenate two tuples
mom = ["kind","caretaker","love"]
dad = ["silentsupport","respect","love"]
parents = mom+dad
print(parents)


