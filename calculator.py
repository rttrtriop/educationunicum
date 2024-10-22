while True :
    num1 = int(input())
    operation = input()
    num2 = int(input())

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "^":
        print(num1 ** num2)
    elif operation == "/":
        if num2 == 0:
            print("на ноль делить нельзя")
        else :
            print(num1 / num2)
    else:
        print("некорректная операция введите одну из следующих : +,-,/,^ или *")

    print("____________________________________________________________________________________________________")
