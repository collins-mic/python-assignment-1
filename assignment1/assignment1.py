first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operator = input("Enter an operator(+ - * /): ")
if operator == "+" :
    result = first_number + second_number
    print(f"{first_number} {operator} {second_number} = {result}")
elif operator == "-" :
    result = first_number - second_number
    print(f"{first_number} {operator} {second_number} = {result}")
elif operator == "*":
    result = first_number * second_number
    print(f"{first_number} {operator} {second_number} = {result}")
elif operator == "/":
    result= first_number / second_number
    print(f"{first_number} {operator} {second_number} = {result}")