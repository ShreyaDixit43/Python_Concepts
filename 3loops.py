#for loops
'''
#iterating over a string
name = 'Shreya'
for i in name:
  print(i)
  if(i=="b"):
      print("something special")


#iterating over a list
colors = ["color", "green", "blue", "yellow"]
for x in colors:
    print(x)
    for i in x:
        print(i)'''

#range
# #
# for k in range(5):
#     print(k+1)
# for k in range(1,9):
#     print(k)

# for k in range(1,12,3):
#     print(k)

#while loop

# i = 0
# while(i<=5):
#     print(i)
#     i = i + 1

# i = int(input("enter"))
# while(i<=20):
#     i = int(input("enter"))
#     print(i)
# print("done")

# count = 4
# while(count>0):
#     print(count)
#     count = count - 1
# else:
#     print("im inside else")

#break stmts

# for i in range(0,11):
#     print("5 X", i+1, "=", 5 * (i+1))
#     if(i == 10):
#         break  //skip the loop
# print("loop ko chod")
#
# for i in range(12):
#     if (i == 10):
#         print("skip the iteration")
#         continue
#     print("5 X", i+1, "=", 5 * (i+1))

#for loops with else
#
# for i in []:
#     print(i)
# else:
#     print("Sorry")

#example
for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i")

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("out of the loop")