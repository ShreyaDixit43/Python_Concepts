a = input("Enter teh number")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1, 11):
        print(f"{int(a)}X {i}={int(a)*i}")
except:
    print("Invalid")

try:
    num = int(input("Enter an integer"))
    a = [6,3,2,1,13]
    print(a[num])
except ValueError:
    print("Invalid")

except IndexError:
    print("Index Error")


# finally keyword
def fun():
    try:
        l= [1,2,2,4,5,7]
        i = int(input("Enter the index"))
        print(l[i])
        return 1
    except:
        print("error")
        return 0
    finally:
        print("Im always executed")

x=fun()
print(x)

#raising custom errors
a = int(input("Enter any value betn 5 & 9"))
if(a<5 or a>9):
    raise ValueError("throw error")

salary = int(input("Enter the salary amount"))
if not 2000<salary<=8000:
    raise ValueError("not valid")
print("good Salary")

salary1 = int(input("Enter the salary amount"))
if not 2000<salary<=8000:
    raise ValueError("not valid")
print("good Salary")

