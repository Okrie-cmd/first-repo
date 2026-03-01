import re

def tokenize(x):
    tokens = re.findall(r'\d+\.?\d*|[+\-/*]', x)
    if len(tokens) == 0:
        return None
    result = []
    for token in tokens:
        if token in "+-/*":
            result.append(token)
        else:
            result.append(float(token))
    return result

def validate(tokens):
    if len(tokens) < 3:
        return False
    if len(tokens) % 2 == 0:
        return False
    for i, token in enumerate(tokens):
        if i % 2 == 0:
            if not isinstance(token, float):
                return False
        else:
            if token not in {"+", "-", "/", "*"}:
                return False
    return True

def apply_op(num1, op, num2):
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2
    if op == "/":
        if num2 == 0:
            return None
        else:
            return num1 / num2
    raise ValueError(f"Unknown operator: {op}")

def calculate(tokens):
    first_step = [tokens[0]]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = tokens[i + 1]
        if op in "/*":
            prev_num = first_step[-1]
            result = apply_op(prev_num, op, num)
            first_step[-1] = result
            if result is None:
                return None
        else:
            first_step.append(op)
            first_step.append(num)
        i += 2

    result = first_step[0]
    i = 1
    while i < len(first_step):
        op = first_step[i]
        num = first_step[i + 1]
        result = apply_op(result, op, num)
        i += 2
    return result

def main():
    print("Calculator (q to quit)")
    while True:
        x = input(">>>")
        if x == "q":
            break
        tokens = tokenize(x)
        if tokens is None:
            continue
        if not validate(tokens):
            continue
        result = calculate(tokens)
        print(result)

if __name__ == "__main__":
    main()