s = {2,4,5,6}
print(type(s))
print(s)

info = {"shreya", 19, False, 8.9, 90}
print(info)

#to use empty set use set()
shreya = set()
print(type(shreya))

#acces set items
# using loop
for value in info:
    print(value)

#set methods

#union
s1 = {1,2,3,4}
s2 = {3,6,8}
print(s1.union(s2))

#update
s1.update(s2)
print(s1, s2)

s2.update(s1)
print(s1, s2)

# #intersection
s3 = s1.intersection.update(s2)
print(s3)

#symmetric difference
cities = {"tokyo","madriad","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madriad"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)
cities.symmetric_difference_update(cities2)
print(cities)

cities3 = cities.difference(cities2)
print(cities3)

#isdisjoint
print(cities.isdisjoint(citiies2))
