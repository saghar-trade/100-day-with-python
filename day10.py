
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b
    

operation={
'+':add ,
'-':subtract,
'*':multiply ,
'/':divide
}

num_1 = float(input("enter first number\n"))
should_continue=True
while should_continue:
    num_2 = float(input("next number\n"))
    operator =input("enter your operator (+ - * / )\n")
    if operator not in operation:
        print("Invalid operator. Please try again.")
        continue
    if operator in operation:
        function=operation[operator]
        result=function(num_1 , num_2)
    print(f"{num_1}{operator}{num_2}: {result}")
    user_choice = input("Do you want to continue? Type 'y' to continue or 'n' to exit: ").lower()
    if user_choice == 'y':
        if isinstance(result, (int, float)):
            num_1 = result
        else:
            print("Result is not a number. Restarting.")
            num_1 = float(input("Enter a new first number:\n"))
    else: 
        should_continue=False

   