day_of_week = input("Enter the day of the week: ").lower()   
print(day_of_week)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter the Operation: +,-,*,/" )

if choice == "+" :
    sum = num1 + num2
    print("Addition:", sum)
elif choice == "-":
    diff = num1 - num2
    print("Subtraction:", diff)
elif choice == "*":
    multi = num1 * num2
    print("Multiplication:", multi)
elif choice == "/":
    div = num1 / num2
    print("Divison:", div)
else:
    print("Invalid Operation")