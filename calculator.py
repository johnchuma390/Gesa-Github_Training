# Chuma Calculator
# Author: John Chuma

def chuma_calculator():
    print("=" * 40)
    print("      ✨ Welcome to Chuma Calculator ✨     ")
    print("=" * 40)

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("\n🙏 Thank you for using Chuma Calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("⚠️  Invalid input! Please enter numbers only.")
                continue

            if choice == '1':
                result = num1 + num2
                print(f"✅ Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"✅ Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"✅ Result: {num1} × {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("⚠️  Division by zero is not allowed!")
                else:
                    result = num1 / num2
                    print(f"✅ Result: {num1} ÷ {num2} = {result}")
        else:
            print("⚠️  Invalid choice! Please select 1–5.")

# Run the calculator
if __name__ == "__main__":
    chuma_calculator()
