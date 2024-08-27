def add(numb_1, numb_2):
    return numb_1 + numb_2

def subtract(numb_1, numb_2):
    return numb_1 - numb_2

def divide(numb_1, numb_2):
    return numb_1 / numb_2

def multiply(numb_1, numb_2):
    return numb_1 * numb_2

operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply
}


while True:
    numb_1 = float(input("What's the first number?: "))
    print('+\n-\n*\n/')
    op_input = input('Pick an operation: ')
    numb_2 = float(input("What's the second number?: "))

    operation = operations[op_input]
    final_value = operation(numb_1, numb_2)
    cont = input(f"Type 'y' to continue calculating with {final_value}, type 'n' to start a new calculation: ")

    if cont == 'y':
        while cont == 'y':
            numb_1 = final_value
            print('+\n-\n*\n/')
            op_input = input('Pick an operation: ')
            numb_2 = float(input("What's the second number?: "))

            operation = operations[op_input]
            final_value = operation(numb_1, numb_2)
            cont = input(f"Type 'y' to continue calculating with {final_value}, type 'n' to start a new calculation: ")
