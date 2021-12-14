def add(number_1,number_2):
    addition = number_1 + number_2
    return addition

def subtract(number_1,number_2):
    sub = number_1, number_2
    return sub

def multiply(number_1,number_2):
    mul = number_1*number_2
    return mul

def divide(number_1,number_2):
    div = number_1/number_2
    return div

operations = {"+": add,
              "-": subtract, 
              "*": multiply,
              "/":divide}


def calculator():
    num1 = int(input("What is the first number?: "))
    for operator in operations:
        print(operator)
    operations_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What is the second number?: "))
    operation = operations[operations_symbol]
    first_result = operation(num1,num2)
    print(f"{num1} {operations_symbol} {num2} = {first_result}")




    end_calculation = False

    while not end_calculation:

        
    
        another_operation = input(f"Type 'y' to continue calculating with {first_result} or type 'n' to exit.: ").lower()
        if another_operation == "y":
            operations_symbol =input("Pick another operation: ")
            num3 = int(input("What is the next number?: "))
            operation = operations[operations_symbol]
            second_result = operation(first_result,num3)
            print(f"{first_result} {operations_symbol} {num3} = {second_result}")
        elif another_operation =="n":
            end_calculation = True
            calculator() # recursion, instead of exiting the program, you call the function again and start from the beginning

calculator()