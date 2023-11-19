# Working with python
i = 1
while i == 1:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    while i == 1:
        if i == 1:
            print("Select an option: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Change Numbers \n 6. Exit")
            selection = int(input())
            if selection == 1:
                print("Sum = ",x+y)
            elif selection == 2:
                print("Difference = ",x-y)
            elif selection == 3:
                print("Product = ",x*y)
            elif selection == 4:
                print("On Dividing = ", x/y)
            elif selection == 5:
                break
            elif selection == 6:
                print ("You chose to exit")
                i=0
                break
            else:
                print("Invalid selection please try again")
        else:
            print("Error")
            i = 0
