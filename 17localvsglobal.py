#local variable is a variable accesible within the function
#whereas global varible is a variable that is defined outside the function

# x = 10
#
# def my_func():
#     y = 5 #local
#     print(y)
#
# my_func()
# print(x)
# print(y)# this we cause error bexc y is a local variable and is not accessible outside of the function

#using global keyword
x = 10
def my_func():
    global x
    x=4
    y = 5 #local
    print(y)

my_func()
print(x)
# print(y)
