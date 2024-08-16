class Calculator:
    def add(self, a, b):
        pass

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        pass

    def multiply(self, a, b):
        pass

def main():
    calc = Calculator()
    print("Welcome to the Simple Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Thank you for using the Simple Calculator!")
            break
        
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if choice == '1':
            result = calc.add(a, b)
        elif choice == '2':
            result = calc.subtract(a, b)
        elif choice == '3':
            result = calc.divide(a, b)
        elif choice == '4':
            result = calc.multiply(a, b)
        else:
            print("Invalid choice!")
            continue
        
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
