def find_type(number):
    return "Even" if number % 2 == 0 else "Odd"


try:
    value = input("Enter an integer: ")
    number = int(value)

    print(find_type(number))

except ValueError:
    print("Invalid input")