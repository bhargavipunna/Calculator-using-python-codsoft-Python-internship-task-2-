def get_numbers():
    global num
    num = []
    print("Enter numbers for calculation (type 'done' when finished):")
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            num.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return num


def calculate(op, numbers):
    if op == 1:
        result = sum(numbers)
        print("The result of Addition is:" + str(result))
    elif op == 2:
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        print("The result of Subtraction is:" + str(result))
    elif op == 3:
        result = 1
        for n in numbers:
            result *= n
        print("The result of Multiplication is:" + str(result))
    elif op == 4:
        result = numbers[0]
        try:
            for n in numbers[1:]:
                result /= n
            print("The result of Division is:" + str(result))
        except ZeroDivisionError:
            return "Error: Division by zero."
    else:
        return "Invalid operation."


print("..........")
print("Calculator")
print("..........")
while True:
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n-1. Exit")
    op = int(input("Enter your choice:"))
    if op == -1:
        print("Exiting")
        break
    numbers = get_numbers()


    if len(numbers) < 2:
        print("Please enter atleast two numbers to perform operations")
    else:
        calculate(op, numbers)
