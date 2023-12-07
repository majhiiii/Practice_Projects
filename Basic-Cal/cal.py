import math

class AdvancedCalculator:
    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero is not allowed."
        return x / y

    def exponentiate(self, x, y):
        return x ** y

    def square_root(self, x):
        if x < 0:
            return "Error! Square root of a negative number is not allowed."
        return math.sqrt(x)

    def memory_store(self, value):
        self.memory = value

    def memory_recall(self):
        return self.memory

    def clear_memory(self):
        self.memory = 0
        print("Memory cleared.")

    def run_calculator(self):
        print("Welcome to Advanced Calculator!")

        while True:
            print("\nChoose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Square Root")
            print("7. Memory Store")
            print("8. Memory Recall")
            print("9. Clear Memory")
            print("10. Exit")

            choice = input("Enter your choice (1-10): ")

            if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result:", self.add(num1, num2))
                elif choice == '2':
                    print("Result:", self.subtract(num1, num2))
                elif choice == '3':
                    print("Result:", self.multiply(num1, num2))
                elif choice == '4':
                    print("Result:", self.divide(num1, num2))
                elif choice == '5':
                    print("Result:", self.exponentiate(num1, num2))
            elif choice == '6':
                num = float(input("Enter a number: "))
                print("Result:", self.square_root(num))
            elif choice == '7':
                value = float(input("Enter the value to store in memory: "))
                self.memory_store(value)
                print("Value stored in memory.")
            elif choice == '8':
                print("Memory Value:", self.memory_recall())
            elif choice == '9':
                self.clear_memory()
            elif choice == '10':
                print("Exiting the Calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    calc = AdvancedCalculator()
    calc.run_calculator()
