# Program to perform arithmetic operation menu driven approach

def ar():
    print("1. Press 1. for addition\n2. Press 2. for subtrction"
          "\n3. Press 3. for Multiplication\n4. Press 4. for division\nPress 0 to exit.")
    c = int(input("Enter your choice : "))
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    if c == 1:
        print("Addition of {0} and {1} is : ".format(a,b), a + b)
    elif c == 2:
        print("Subtraction of {0} and {1} is : ".format(a,b), a - b)
    elif c == 3:
        print("Multiplication of {0} and {1} is : ".format(a, b), a * b)
    elif c == 4:
        print("Division of {0} and {1} is : ".format(a, b), a / b)
    elif c == 0:
        exit(1)
    else :
        print("Invalid choice ")




while True:
    ar()