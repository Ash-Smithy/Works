x = int(input("Enter first value: "))
y = int(input("Enter second value: "))

def add():
    print("Sum = ",x+y)
def subtract():
    print("Difference = ",x-y)
def multiply():
    print("Product = ",x*y)
def divide():
    print("Div = ",x/y)
print("Select option \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide\n")
selection = int(input())
if selection == 1:
    add()
elif selection == 2:
    subtract()
elif selection == 3:
    multiply()
elif selection == 4:
    divide()
else:
    print("Invalid selection")
    