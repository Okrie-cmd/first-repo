def main():
    print("Calculator (q to quit)")
    while True:
        try:
            x = input(">>>")
        except (KeyboardInterrupt, EOFError):
            break
        
        if x == "q":
            break
        
        try:
            result = eval(x)
            print(result)
        except (SyntaxError, ZeroDivisionError, TypeError, NameError, OverflowError):
            continue

if __name__ == "__main__":
    main()