import os

def add(a,b):
    return a+b
def deff(a,b):
    return a-b
def multiply(a,b):
    return a*b
def devid(a,b):
    return a/b

operations_dict={
    "+":add,
    "-":deff,
    "*":multiply,
    "/":devid
}
def calculator():
    num1 = float(input("enter 1st number:"))
    flag = True
    while flag:
        for symbol in operations_dict:
            print(symbol)
        operation = input("enter the operation:")
        num2 = float(input("enter 2nd num:"))
        oper_funt = operations_dict[operation]
        result = oper_funt(num1, num2)
        print(f"{num1}{operation}{num2}={result}")

        continu = input(f"press 'y' if u wanna continue with {result},or press 'n',to exit press 'x':")
        if continu == 'y':
            num1 = result
        elif continu == 'n':
            flag = False
            os.system('cls')
            calculator()
        elif continu == 'x':
            flag = False

calculator()