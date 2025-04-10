oprator = input("Enter the oprator (+,-,*,/) : ")
num1 = float(input("enter the 1st number : "))
num2 = float(input("enter the 2nd number : "))
if oprator == "+":
    result = num1 + num2
    print(result)
if oprator == "-":
    print(result)
    result = num1 - num2
    print(result)
if oprator == "*":
    result = num1 * num2
    print(result)
if oprator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{oprator} is not oprator valid")
   
