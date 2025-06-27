marks = [12, 23, 45, 98, 45, 1, 47]

index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("Harry, awesome!")
    index += 1

#use of enumerate
for index, mark in enumerate (marks):
    print(mark)
    if(index == 3):
        print("Harry, awesome!")

#using enumerate in list
fruits = ['apple', 'banana', "mango"]
for index, fruit in enumerate(fruits):
    print(index, fruits)

#changing the start index
fruits = ['apple', 'banana', "mango"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruits)
