def Calculator():
 while True:
    
    print("\n Choose an operation:")
    print("1. ADDITION ")
    print("2. SUBSTRACTION ")
    print("3. MULTIPLICATION ")
    print("4. DIVISION ")
    print("5. MODULUS ")

    number1 = float(input("\nENTER FIRST NUMBER: "))
    choice = input("\nEnter Choice: ")
    number2 = float(input("\nENTER SECOND NUMBER: "))
    
    add = (number1 + number2)
    sub = (number1 - number2)
    mul = (number1 * number2)
    div = (number1 / number2)
    mod = (number1 % number2)

    if choice == '1':
        print("\n RESULT: ",add)
    elif choice == '2':
        print("\n RESULT: ",sub)
    elif choice == '3':
        print("\n RESULT: ",mul)
    elif choice == '4':
        print("\n RESULT: ",div)
    elif choice == '5':
        print("\n RESULT: ",mod)
    else:
        print("\nINVALID CHOICE!!!")
        
Calculator()

    