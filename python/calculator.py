def get_number(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print(f"Error: {user_input} is not valid number. Try again.")

def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        if num2 == 0:
            print("Error: division by zero is not allowed.")
        else:
            return num1 / num2
    elif op == "*":
        return num1 * num2

def main():
    valid_ops = ['+', '-', '/', '*']
    while True:
        op = input("Enter an operator:")
        if op not in valid_ops:
            print(f"Error: {op} is not valid operator. Try again.")
        else:
            break
    num1 = get_number("Enter first number:")
    num2 = get_number("Enter sedcond number:")
    result = calculate(num1, op, num2)
    print(result)

if __name__ == "__main__":
    main()