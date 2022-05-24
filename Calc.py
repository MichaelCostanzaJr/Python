# Calc.py
# Extreme calculator
# Michael

def menu():
    print("="*30)
    print("Extreme Calc")
    print("By Michael")
    print("="*30)
    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Mult")
    print("[4] Div")
    print("[Q] Exit")

option = ''

while option!="Q":
    menu()
    option = str(input('Please, select an option: '))

    num1 = float(input('enter the first number:'))
    num2 = float(input('enter the second number:'))

    result = 0

    if option=="1":
        result= num1+num2
        print(f"The result is: {result}")
    elif option=="2":
        result= num1-num2
        print(f"The result is: {result}")
    elif option=="3":
        result= num1*num2
        print(f"The result is: {result}")
    elif option=="4":
        if num2 !=0:
            result= num1/num2
            print(f"The result is: {result}")
        else:
            print("We can not divide by zero!!!")
    input('Press enter to continue...')


