try:
    a = int(input("enter the value: "))
    b = int(input("enter the value: "))
    print("what kind of operation do you want \n press + for addition \n press - for subtraction \n press / for divison \n press * for multiplication")
    o = input("enter the operation: ")
    match o:
        case "+":
            print(f"the result is {a+b}")
        case "-":
            print(f"the result is {a-b}")
        case "/":
            print(f"the result is {a/b}")
        case "*":
            print(f"the result is {a*b}")
        case default:
            print(f"there was an error")

except Exception as e:
    print("enter the valid value for a and b")


