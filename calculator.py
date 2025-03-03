logo=['''
  _____________________
 |  _________________  |
 | | JO           0. | |
 | |_________________| |
 |  ___ ___ ___   ___  |
 | | 7 | 8 | 9 | | + | |
 | |___|___|___| |___| |
 | | 4 | 5 | 6 | | - | |
 | |___|___|___| |___| |
 | | 1 | 2 | 3 | | x | |
 | |___|___|___| |___| |
 | | . | 0 | = | | / | |
 | |___|___|___| |___| |
 |_____________________|''']

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error! Division by zero."

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
   
    n1 = float(input("Enter your first number: "))
    while True:
        while True:
            o = input("Enter the operator (+, -, *, /): ")
            if o in operations:
                break
            else:
                print("Invalid operator. Please enter +, -, *, or /.")
        n2 = float(input("Enter your next number: "))
        answer = operations[o](n1, n2)
        print(f'{n1} {o} {n2} = {answer}')
        
        while True:
            choose = input("Enter 'yes' to continue with the current answer, or 'no' to start a new calculation: ").lower()
            if choose in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        if choose == "yes":
            n1 = answer
        else:
            print('\n' * 20)
            calculator()
            break

calculator()
