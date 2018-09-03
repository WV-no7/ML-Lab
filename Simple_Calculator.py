def calculator(n):
    x=int(input("Enter the integer a : "))
    y=int(input("Enter the integer b : "))
    if(n==1):
        print("Sum is :",x+y)
    elif(n==2):
        print("Difference is :",x-y)
    elif(n==3):
        print("Product is :",x*y)
    elif(n==4):
        print("Quotient is :",x/y)
    else:
        print("Invalid option")
    return
z=True        
while(z):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Press 0 to exit")
    x=int(input("Enter the option : "))
    if(x==0):
        z=False
    else:    
        calculator(x)
