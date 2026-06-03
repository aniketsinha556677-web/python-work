# Number Analyzer

# Global Variable
app_name = "Number Analyzer"

# Function
def analyze_number(num):

    # Control Flow + Operators
    if num > 0:
        print("The number is Positive")
    elif num < 0:
        print("The number is Negative")
    else:
        print("The number is Zero")

    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")


print("Welcome to", app_name)

# While Loop
while True:

    number = int(input("\nEnter a number: "))

    # Function Call
    analyze_number(number)

    # For Loop
    print("\nCounting from 1 to", abs(number))

    for i in range(1, abs(number) + 1):
        print(i)

    # Loop Control
    choice = input("\nTry another number? (yes/no): ")

    if choice.lower() == "no":
        break

print("\nThank you for using Number")